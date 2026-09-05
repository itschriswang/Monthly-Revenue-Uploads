"""Rebuild the guide's data payload from the review workbook and the latest Envizi export."""
import json, datetime, warnings, csv, os
import pandas as pd, openpyxl
warnings.filterwarnings("ignore")

ROOT = "/home/user/RevenueAndUnallocated"
OUTDIR = f"{ROOT}/Large Market Certificates"
WB = f"{OUTDIR}/Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx"
EXPORT = f"{ROOT}/Electricity download after the first Claude in Chrome batches.xlsx"   # 4-5 Sep 26, 42 certificate accounts live
ACC = f"{ROOT}/FY27/Extract_for_Accounts 05 Sep 26.csv"
OLD = os.path.join(os.path.dirname(__file__), "guide_data.json")
DST = OLD

ELEC, GREEN, CERT = "Electricity [kWh]", "Electricity - Green [kWh]", "Certificates - Location [kWh]"
RENEWAL = datetime.datetime(2026, 7, 1)
MONTHS = ["Jun 26", "Jul 26", "Aug 26"]
LM = ("Electricity Large Market", "Energetics - Large Market")
ZERO = "30 Dec 1899"
nmi_of = lambda a: a.rsplit("_", 1)[-1] if "_" in a else a

# ---------------------------------------------------------------- sources
e = pd.read_excel(EXPORT).fillna("")
e["m"] = pd.to_datetime(e["Occurred_On"], errors="coerce").dt.strftime("%b %y")
for c in ("Actual Data", "Estimated Data", "Accrued Data", "Total Data", "Total CO2e(t)"):
    e[c] = pd.to_numeric(e[c], errors="coerce").fillna(0)

with open(ACC, newline="", encoding="utf-8-sig") as fh:
    acc = pd.DataFrame(list(csv.reader(fh))[1:], columns=list(csv.reader(open(ACC, encoding="utf-8-sig")))[0])
acc["_nmi"] = acc["Account Number"].map(nmi_of)
EXTRACT_DAY = datetime.datetime(2026, 9, 5)
def _still_open(rep):
    rep = rep.strip()
    if rep in ("", ZERO):
        return True
    try:
        return datetime.datetime.strptime(rep, "%d %b %Y") > EXTRACT_DAY
    except ValueError:
        return False
acc["_active"] = (acc["Replaced On"].map(_still_open) & (acc["Location"] != "Unallocated Accounts")).astype(int)
elec_act = acc[(acc["Data Type"] == ELEC) & (acc._active == 1)]

wb = openpyxl.load_workbook(WB, data_only=True)
R = wb["Review - AU Large Market"]
LG = wb["LGCS Accounts to Check"]
SR = wb["Site Register (AU Large)"]
fmt = lambda d: d.strftime("%Y-%m-%d") if isinstance(d, datetime.datetime) else str(d or "")
reg = {}
for r in range(2, SR.max_row + 1):
    n = str(SR.cell(r, 1).value or "").strip()
    if n:
        reg[n] = dict(tender=SR.cell(r, 12).value, contracted=SR.cell(r, 13).value,
                      start=fmt(SR.cell(r, 14).value), end=fmt(SR.cell(r, 15).value),
                      term=SR.cell(r, 16).value)
ENGIE_NMIS = set(elec_act[elec_act["Supplier"] == "EngieAU"]._nmi)


def months_for(account, dtype=ELEC):
    g = e[(e["Item Number"].astype(str) == account) & (e["Data Type"] == dtype)]
    out = []
    for m in MONTHS:
        x = g[g["m"] == m]
        act, est, acr = x["Actual Data"].sum(), x["Estimated Data"].sum(), x["Accrued Data"].sum()
        tot, co2 = x["Total Data"].sum(), x["Total CO2e(t)"].sum()
        if x.empty:
            st = "none"
        elif tot == 0:
            st = "zero"
        elif acr > 0 and act == 0:
            st = "accrued"
        elif est > 0 and act == 0:
            st = "estimated"
        else:
            st = "actual"
        out.append(dict(month=m, kwh=round(float(tot)), status=st, co2=round(float(co2), 2)))
    return out


# ---------------------------------------------------------------- rows
rows, dual = [], []
for r in range(19, 100):
    if not R.cell(r, 3).value:
        continue
    nmi = str(R.cell(r, 3).value).strip()
    src = R.cell(r, 28).value or ""
    decision = R.cell(r, 22).value
    others = [f"{x['Account Number']} ({x['Supplier']}, {x['Account Style']})"
              for _, x in elec_act[elec_act._nmi == nmi].iterrows() if x["Account Number"] != src]
    start = R.cell(r, 10).value
    row = dict(
        nmi=nmi, state=R.cell(r, 4).value, site=R.cell(r, 6).value, address=R.cell(r, 7).value,
        bu=R.cell(r, 8).value, retailer=R.cell(r, 9).value,
        start=start.strftime("%Y-%m-%d") if isinstance(start, datetime.datetime) else str(start or ""),
        matched=R.cell(r, 11).value, location=R.cell(r, 12).value, lref=str(R.cell(r, 13).value or ""),
        matched_style=R.cell(r, 14).value, certs_n=int(R.cell(r, 16).value or 0),
        certs=R.cell(r, 18).value or "", green_kwh=round(float(R.cell(r, 19).value or 0)),
        decision=decision, reason=R.cell(r, 23).value, new_acct=R.cell(r, 24).value or "",
        new_sup=R.cell(r, 25).value or "", src_acct=src, src_history=R.cell(r, 29).value or "",
        opened_on=(R.cell(r, 30).value.strftime("%Y-%m-%d")
                   if isinstance(R.cell(r, 30).value, datetime.datetime) else ""),
        other_on_nmi="; ".join(others),
        src_small=bool(src and str(R.cell(r, 14).value) not in LM),
        months=months_for(src) if src and src != "None" else [],
        green_months=months_for(R.cell(r, 11).value or "", GREEN),
    )
    rows.append(row)

    # a second active account still recording the same renewal months = a double count
    g = reg.get(nmi, {})
    opened = lambda a: (acc[acc["Account Number"] == a]["Opened On"].iloc[0] or "")
    for _, o in elec_act[elec_act._nmi == nmi].iterrows():
        if o["Account Number"] == src:
            continue
        om = months_for(o["Account Number"])
        if not any(x["status"] in ("actual", "accrued", "estimated") and x["month"] != "Jun 26" for x in om):
            continue
        km = months_for(src)
        # the old retailer's account left open through the switch, or a second connector account
        kind = "retailer" if str(o["Supplier"]) != str(acc[acc["Account Number"] == src]["Supplier"].iloc[0]) \
               else "duplicate"
        dual.append(dict(
            nmi=nmi, location=row["location"], site=row["site"], state=row["state"], kind=kind,
            contracted=g.get("contracted", row["retailer"]), tender=g.get("tender", ""),
            contract_start=g.get("start", row["start"]), contract_end=g.get("end", ""),
            term=g.get("term", ""),
            close_date="2026-06-30" if kind == "retailer" else "",
            surplus_kwh=sum(x["kwh"] for x in om if x["month"] != "Jun 26"),
            surplus_co2=round(sum(x["co2"] for x in om if x["month"] != "Jun 26"), 2),
            close=dict(account=o["Account Number"], supplier=o["Supplier"], style=o["Account Style"],
                       opened=opened(o["Account Number"]),
                       months=[dict(month=x["month"], kwh=x["kwh"], kind=x["status"]) for x in om]),
            keep=dict(account=src, supplier=acc[acc["Account Number"] == src]["Supplier"].iloc[0],
                      style=row["matched_style"], opened=opened(src),
                      months=[dict(month=x["month"], kwh=x["kwh"], kind=x["status"]) for x in km]),
        ))

# ---------------------------------------------------------------- LGCS tab
lgcs = []
for r in range(5, LG.max_row + 1):
    if not LG.cell(r, 2).value:
        continue
    lgcs.append(dict(account=LG.cell(r, 2).value, location=LG.cell(r, 3).value,
                     nmis=str(LG.cell(r, 6).value or ""), live=str(LG.cell(r, 7).value or ""),
                     own=LG.cell(r, 8).value))

# rows held because the contracted retailer has no account on the NMI yet. Two flavours: the
# account does not exist at all (wait for the connector), or it exists but is parked at
# Unallocated Accounts (allocate it, then build the meter).
SUPPLIER_MAP = {"Engie": "EngieAU", "Origin": "Origin", "Shell": "ShellEnergyAU",
                "Alinta": "Alinta", "CS Energy": "CSEnergy", "Jacana": "Jacana"}
waiting = []
for r in rows:
    if not str(r["decision"]).startswith("Create - temporary"):
        continue
    g = reg.get(r["nmi"], {})
    contracted = str(g.get("contracted") or "").strip()
    want = SUPPLIER_MAP.get(contracted, contracted)
    parked = acc[(acc._nmi == r["nmi"]) & (acc["Supplier"] == want)
                 & (acc["Data Type"] == ELEC)]["Account Number"].tolist()
    waiting.append(dict(
        nmi=r["nmi"], state=r["state"], location=r["location"], site=r["site"],
        address=r["address"], lref=r["lref"], bu=r["bu"],
        contracted=contracted, expected_supplier=want, tender=g.get("tender", ""),
        contract_start=g.get("start", ""), account=r["src_acct"],
        supplier=(acc[acc["Account Number"] == r["src_acct"]]["Supplier"].iloc[0]
                  if r["src_acct"] and r["src_acct"] != "None" else ""),
        style=r["matched_style"], months=r["months"],
        new_acct=r["new_acct"], new_sup=r["new_sup"], opened_on=r["opened_on"],
        src_history=r["src_history"], certs=r["certs"], certs_n=r["certs_n"],
        parked=parked[0] if parked else "",
        parked_at=(acc[acc["Account Number"] == parked[0]]["Location"].iloc[0] if parked else ""),
    ))

lbl = lambda iso: (datetime.datetime.strptime(iso, "%Y-%m-%d").strftime("%d %b %Y").lstrip("0")
                   if iso else "")
for d in dual:
    d["close_date_label"] = lbl(d["close_date"])
    d["contract_start_label"] = lbl(d["contract_start"])
    d["contract_end_label"] = lbl(d["contract_end"])

old = json.load(open(OLD))
built = acc[acc["Account Number"].str.endswith("_CERTS") & (acc["Supplier"] == "LGC Virtual Account")]
live = [dict(account=a["Account Number"], location=a["Location"], opened=a["Opened On"].strip(),
             supplier=a["Supplier"], source=a["Account Number"][:-len("_CERTS")])
        for _, a in built.drop_duplicates("Account Number").iterrows()]
data = dict(built=datetime.date.today().strftime("%d %b %Y"), extract_date="05 Sep 2026",
            verify_date="4–5 Sep 2026", rows=rows, lgcs=lgcs, live=live, dual=dual,
            waiting=waiting, nz=old["nz"])
json.dump(data, open(DST, "w"), ensure_ascii=False)
import collections
print("rows", len(rows), dict(collections.Counter(r["decision"] for r in rows)))
print("creates whose source is small-market styled:", sum(1 for r in rows if r["decision"] == "Create" and r["src_small"]))
print("lgcs", len(lgcs), "| dual", len(dual), dict(collections.Counter(d["kind"] for d in dual)),
      "| waiting", len(waiting), dict(collections.Counter("parked" if w["parked"] else "missing" for w in waiting)),
      "| live", len(data["live"]))
