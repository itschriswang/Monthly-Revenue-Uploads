# Large Market Certificates

Renewable-certificate **virtual meters** for the AU electricity sites Downer contracted under the
FY26–28 renewal agreements, and everything behind them.

## Files

| File | What it is |
| --- | --- |
| `Virtual Meter Guide/Large_Market_Virtual_Meters.html` | **Start here.** The brief and the working checklist in one page — every account to create with copyable field values, the two live ones checked against the latest export, the double count to close off, what to leave alone, NZ and reference. Ticks and notes save in the browser. Open it by double-clicking. |
| `Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx` | The review workbook: all 81 register rows with live formulas, the 70 accounts on `Prep` and the load tab (kept as the record of what each account looks like — **not uploaded**, see below), plus the `Manual Setup Checklist` and `LGCS Accounts to Check` tabs. The `Account_Setup_and_Data_Load_-_PM&C_` prefix is what Envizi processes on if a load is ever needed. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28.xlsx` | The renewal agreement site register (scope, retailers, contract dates) and the rate schedules with the LGC lines. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` | The same workbook with the Envizi account mapping added to `Site Register` as columns V–AE, and an `Envizi mapping notes` tab explaining them. Everything left of column V is untouched. |
| `ElectricityEnviziSummaryjunejulyaug26.xlsx` | The Jun–Aug 26 Envizi summary — kWh, actual/accrued split, cost, CO2e and the green component. |

The accounts and locations extracts it reads are in `../FY27/` (`Extract_for_Accounts 03 Sep 26.csv`,
`Extract_for_Locations 26 Aug 26.csv`). The 4 Sep 26 export used to verify the first two accounts is
`../Electricity download after bathurst and mogo virual accounts.xlsx`.

## Scope

The **green rows** in the Site Register are the renewable ones — 78 of the 81 `AU Large Electricity`
rows, the other three being the NT sites on Jacana standing offer. A green row gets a virtual meter
unless it is a named exclusion or already offset another way.

**The meter class does not decide scope.** Category Management, 4 Sep 26, on a Mogo NMI I queried:

> sometimes when you take both to a retailer they will agree to supply both as large market sites —
> that's probably what's occurred here… from a metering perspective it may be considered a small site,
> but from an electricity supply agreement perspective, it's being treated as a large site.

So `Electricity Small Market` in Envizi is the **meter** classification and does not take a site out of
the renewal; the supply agreement does, and the register's green rows record it. 35 of the 70 accounts
sit on a small-market-styled source for exactly this reason (QLD 16, VIC 10, SA 4, TAS 3, NSW 2).

| Outcome | Rows |
| --- | --- |
| **Create — virtual certificate account** | **70** |
| Exclude — already renewable via the account's green component (Alinta WA) | 7 |
| Exclude — named site (NT ×3, QTMP) | 4 |
| Total register rows reviewed | 81 |

By state the 70 are: NSW 36, QLD 16, VIC 10, SA 4, TAS 3, ACT 1. The full list, with the source account
and the field values for each, is on the guide page and on the workbook's `Manual Setup Checklist` tab.

## How the sites were matched

On the connection ID, not the region. The NMI is the text after the last underscore in an Envizi account
number, so each register row is matched to the active accounts on that NMI. Of those, the source is the
one **carrying the electricity from 1 July 2026** — actual data first, large market style as the
tie-break — and the location comes from that account. All 81 rows resolved.

## Is the renewable product LGCs?

For Engie and Origin, yes: `Rates & Source Data` prices both renewal contracts with an explicit LGC line
(FY27 0.395 c/kWh Engie, 0.375 Origin; FY28 0.375) plus a "renewable product $/yr". The Alinta (WA) and
Shell (TAS) contracts are modelled as an all-in delivered rate with no separate LGC line; Category
Management confirms they are renewable, and the Alinta accounts already show 100% green kWh in Envizi.

## Progress — the first two, verified

`50002617964_NAAA00AC25_CERTS` (Asphalt Prod - Bathurst) and `50002769514_4001127731_CERTS`
(Asphalt Prod - Mogo) were created on 4 Sep 26. Against the export taken straight after:

- **Mirroring is exact** — certificate kWh equals source kWh in every month, and it follows the source
  when a bill replaces an accrual (Bathurst's August moved from an accrued 49,402 to an actual 41,470).
- **The date bound works** — both opened 2026-07-01 and carry no June record, though both sources have
  June data.
- **The factor vintage is out** — certificates use `LGCs NSW 24-25` (−0.66 kg/kWh) against electricity on
  `25-26 New South Wales` (0.64), so a 100% meter over-offsets by about 3% and Bathurst nets −1.08 t in
  July instead of zero. Victoria has an `LGCs Victoria 25-26` factor; NSW needs its 25-26 equivalent
  added or mapped **before the remaining accounts are linked**.
- **Mogo settled the scope rule** — that one was built on `50002769514_4001127731`, which Envizi styles
  small market. Querying it produced the answer quoted above, so the account is right where it is and
  34 more like it joined the list.

## How the new accounts are structured

Modelled on the Ecotricity virtual accounts (`Copy of Eco_ICP_..._CERTS`) and on the two already built:

| Field | Value |
| --- | --- |
| Location | The source account's location |
| Account style | `Certificates - Location - kWh` |
| Account number | `<source account>_CERTS` — keyed on the source, because `LGCS_<NMI>` is already taken at many sites |
| Account reference | The NMI |
| Supplier | `LGC Virtual Account` |
| Reader | blank |
| Opened On | `2026-07-01` — the contract start, and what bounds the meter to the renewal period |
| Records | **none** — the account must be empty to become a virtual meter |
| Virtual meter source | The account on the card, 100% |

50 of the 70 sources have data before 1 Jul 26, which is why Opened On matters: without it the meter
mirrors those years too, generating certificates for periods that were not renewable and doubling what
the old `LGCS_` accounts already record for 2025.

## A virtual meter has to be empty — so they are made by hand

Envizi only lets an account be set up as a virtual meter while it holds no records, and the PM&C template
cannot create an account without a record. So the load tab is **not uploaded**; it stays as the record of
what each account should look like. The `Manual Setup Checklist` tab (and the guide page) is the worklist.

Per account: **1.** Create it empty with the fields above, including Opened On. **2.** Open it and set it
up as a virtual meter, source = the account on the card, 100% — that one only. **3.** Check the new
account shows kWh equal to the source and the location's market-based CO2e drops to match.

## The existing `LGCS_` accounts — leave them

54 active certificate accounts sit at 40 of the in-scope locations. Checked in Envizi on 4 Sep 26: all
hold LGC data from **2025 and earlier**, so none is empty, none can be converted to a virtual meter, and
none covers the renewal period. They stay as the historical record and the new account sits beside them.
The `LGCS Accounts to Check` tab lists them with `Has data?` pre-set to Yes; set one to No and the Action
column switches to reuse.

## Double count — 13 accounts to close off

On 13 NMIs a second active account is still recording the months the source account already covers, so
the site's electricity is counted twice before any certificate is applied. Together they carry
**1,159,261 kWh / 684 tCO₂e** of July and August on top of what the source accounts report. Two causes:

**Retailer switched, old account left open (11).** These moved to Engie on 1 Jul 26 and the previous
retailer's account was never closed, so it keeps accruing while the Engie account bills the actuals:
Somerton (303), Utilities Derrimut, Shepparton (308), Bayswater (302), Dandenong - PAV, Mulgrave,
Wodonga (315), Gillman - PAV, Wingfield (523) and Largs Bay ×2. I checked **column M (Contracted
Retailer)** first and Engie is correct on every one — tendered to Origin, contracted to Engie,
1 Jul 26 to 30 Jun 28, 24 months. The old account gets `Replaced On` = **30 June 2026**.
Worth 958,192 kWh / 549 tCO₂e.

**Second connector account on the same NMI (2).** Gympie and Archerfield (406) each carry a second
CS Energy account created by the Utilities Connector, accruing with no Opened On and no actuals. Nine of
its `5000021_` siblings have already been closed off at 31 Mar, 31 May and 30 Jun 26 — these two were
missed. Worth 201,069 kWh / 135 tCO₂e. I confirm the date against how the siblings were done rather than
assuming 30 Jun.

**Still on the tender retailer's account (13).** Every Queensland site contracted to Engie from 1 Jul 26
has no EngieAU account in Envizi yet — the connector hasn't switched them. Their virtual meters follow
the CS Energy account for now, so when the Engie account appears the source needs repointing and the
CS Energy one closing, exactly like the 11 above. Worth watching rather than acting on today.

The guide page has a card per NMI with both accounts side by side, the month-by-month actual/accrued
split, and four tick boxes: contracted retailer checked, old account closed, duplicated months cleared,
re-checked in a fresh export.

## The site register, mapped to Envizi

`Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` adds ten columns to
`Site Register` — the same 341 rows, all commodities and both countries, with the Envizi account each
Connection ID resolves to:

| Col | Contents |
| --- | --- |
| V | **Envizi Account Number** — the account the virtual meter follows where there is one, else the active account for that commodity, or `Not found` |
| W–Y | Account Style, Data Type, Supplier |
| Z–AA | Location, Location Ref |
| AB | Account Status — Active or Replaced *date* |
| AC | Match Basis |
| AD | Other Envizi accounts on the same ID |
| AE | Certificate / virtual meter account — the new one (live, or still to create) and any historical `LGCS_` at the location |

Shading: red in V–AE where no Envizi account ends in that Connection ID, amber in AB for a closed
account, peach in AD for an ID that is being double counted, green in AE where the certificate account is
already live. The `Envizi mapping notes` tab carries the same explanation and the double-count list.

**283 of 341 rows matched.** The 58 that did not are 48 NZ electricity ICPs and 10 NZ gas rows — NZ
per-ICP accounts were replaced in 2023 by one account per location.

Two notes on the file. Saving through the spreadsheet library rewrites a few Annual Consumption values in
column K with a shorter decimal representation (worst difference 4.5e-16 relative, about a nano-kWh); the
stored numbers are identical at Excel's own precision and no other cell left of column V changes. And
`Budget FY26-28` uses `XLOOKUP`, which LibreOffice does not evaluate — it recalculates identically in the
original file, so it is a LibreOffice limitation, not something the mapping introduced.

## New Zealand

All NZ electricity is renewable under the new arrangements (TOU on Ecotricity since 1 Jul 26; NTOU moving
to Ecotricity 1 Jan 27). 114 of the 158 NZ green ICPs resolve to 80 open Envizi locations; 29 of those
already have a CERTS account; 44 cannot be placed from the extracts. Nothing NZ is set up yet — the NTOU
contract has not started, and for a site whose consumption sits on a per-location account rather than an
`Eco_ICP_` account, what the virtual meter should copy needs deciding first.

## Still open

- The NSW 25-26 LGC emission factor — settle before linking the rest.
- The 13 double-counting NMIs — close the old accounts, and confirm the date for the two CS Energy ones.
- The 13 Queensland sites whose Engie account has not appeared in Envizi yet.
- NZ, once the Ecotricity switch is confirmed.
- The Envizi Account Style Link for the certificates style, only if the load tab is ever uploaded.
