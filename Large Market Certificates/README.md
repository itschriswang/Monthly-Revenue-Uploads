# Large Market Certificates

Renewable-certificate **virtual meters** for Downer's AU large market electricity sites under the
FY26–28 renewal agreements, and everything behind them.

## Files

| File | What it is |
| --- | --- |
| `Virtual Meter Guide/Large_Market_Virtual_Meters.html` | **Start here.** The whole brief and the working checklist in one page — background, evidence, the two live accounts checked against the latest export, every account still to create with copyable field values, the historical `LGCS_` accounts to leave alone, exclusions, NZ and reference. Ticks and notes save in the browser. Open it by double-clicking. |
| `Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx` | The review workbook: all 81 register rows with live formulas, the 45 accounts on `Prep` and the load tab (kept as the record of what each account looks like — **not uploaded**, see below), plus the `Manual Setup Checklist` and `LGCS Accounts to Check` tabs. The `Account_Setup_and_Data_Load_-_PM&C_` prefix is what Envizi processes on if a load is ever needed. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28.xlsx` | The renewal agreement site register (scope, retailers, contract dates) and the rate schedules with the LGC lines. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` | The same workbook with the Envizi account mapping added to `Site Register` as columns V–AE. Everything left of column V is untouched. |
| `ElectricityEnviziSummaryjunejulyaug26.xlsx` | The Jun–Aug 26 Envizi summary — kWh, actual/accrued split, cost, CO2e and the green component. |

The accounts and locations extracts it reads are in `../FY27/` (`Extract_for_Accounts 03 Sep 26.csv`,
`Extract_for_Locations 26 Aug 26.csv`). The 4 Sep 26 export used to verify the first two accounts is
`../Electricity download after bathurst and mogo virual accounts.xlsx`.

## Scope: large market only

Only **large market** sites are under the renewal agreement. The Site Register's `AU Large Electricity`
is the *portfolio group* — how the tender was bundled — not the market classification. So a register row
gets a virtual meter only where its NMI has an active Envizi account styled `Electricity Large Market`
(or `Energetics - Large Market`). Confirmed 4 Sep 26: where Envizi styles the account
`Electricity Small Market`, that classification is **correct** and the site is not under the agreement.

| Outcome | Rows |
| --- | --- |
| **Create — large market virtual account** | **45** |
| Exclude — small market, not under the renewal | 25 |
| Exclude — already renewable via the account's green component (Alinta WA) | 7 |
| Exclude — named site (NT ×3, QTMP) | 4 |
| Total register rows reviewed | 81 |

By state, the 45 are: NSW 34, VIC 6, SA 4, ACT 1.
Excluding the small market rows removes every Queensland and Tasmanian row.

## How the sites were matched

On the connection ID, not the region. The NMI is the text after the last underscore in an Envizi account
number, so each register row is matched to the active accounts on that NMI; the virtual meter's source is
the **large market** account among them, and the location comes from that account. All 81 rows resolved.

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
  added or mapped **before the remaining accounts are linked** — 35 of them are NSW or ACT.
- **Mogo's is the small market account** — `50002769514_4001127731` is styled small market, so under the
  rule above it is out of scope. The large market account at that site, `50002617992_4204072845`, is
  still on the list.

## How the new accounts are structured

Modelled on the Ecotricity virtual accounts (`Copy of Eco_ICP_..._CERTS`) and on the two already built:

| Field | Value |
| --- | --- |
| Location | The large market account's location |
| Account style | `Certificates - Location - kWh` |
| Account number | `<source account>_CERTS` — keyed on the source, because `LGCS_<NMI>` is already taken at many sites |
| Account reference | The NMI |
| Supplier | `LGC Virtual Account` |
| Reader | blank |
| Opened On | `2026-07-01` — the contract start, and what bounds the meter to the renewal period |
| Records | **none** — the account must be empty to become a virtual meter |
| Virtual meter source | The large market electricity account, 100% |

44 of the 45 sources have data before 1 Jul 26, which is why Opened On matters: without it the
meter mirrors those years too, generating certificates for periods that were not renewable and doubling
what the old `LGCS_` accounts already record for 2025.

## A virtual meter has to be empty — so they are made by hand

Envizi only lets an account be set up as a virtual meter while it holds no records, and the PM&C template
cannot create an account without a record. So the load tab is **not uploaded**; it stays as the record of
what each account should look like. The `Manual Setup Checklist` tab (and the guide page) is the worklist.

Per account: **1.** Create it empty with the fields above, including Opened On. **2.** Open it and set it
up as a virtual meter, source = the large market electricity account, 100% — that one only. **3.** Check
the new account shows kWh equal to the source and the location's market-based CO2e drops to match.

## The existing `LGCS_` accounts — leave them

35 active certificate accounts sit at the in-scope locations. Checked in Envizi on 4 Sep 26: all hold LGC
data from **2025 and earlier**, so none is empty, none can be converted to a virtual meter, and none
covers the renewal period. They stay as the historical record and the new account sits beside them. The
`LGCS Accounts to Check` tab lists them with `Has data?` pre-set to Yes; set one to No and the Action
column switches to reuse.

## Double count to raise separately

On ten NMIs both the large market account and a small market account are recording the same months in
Envizi, so the site's electricity is counted twice before any certificate is applied: Somerton (303),
Utilities Derrimut, Bayswater (302), Dandenong - PAV, Mulgrave, Wodonga (315), Gillman - PAV,
Wingfield (523) and Largs Bay ×2. Only the large market account is linked to the virtual meter, so this
does not affect the set-up, but it needs fixing on the electricity side. The pairs and monthly kWh are on
the guide page.

## The 45 accounts

| New account | Location | Ref | State | Virtual meter source | Source has pre-Jul-26 data |
| --- | --- | --- | --- | --- | --- |
| `50002618040_7001184714_CERTS` | Asphalt Prod - Hume (101) | 101 | ACT | `50002618040_7001184714` | yes |
| `50002617964_NAAA00AC25_CERTS` | Asphalt Prod - Bathurst (156) | 170156 | NSW | `50002617964_NAAA00AC25` | yes |
| `50002617992_4204072845_CERTS` | Asphalt Prod - Mogo (154) | 154 | NSW | `50002617992_4204072845` | yes |
| `50002756108_4311396021_CERTS` | Asphalt Prod - Rosehill (163) | 163 | NSW | `50002756108_4311396021` | yes |
| `50002756109_4311396022_CERTS` | Asphalt Prod - Rosehill (163) | 163 | NSW | `50002756109_4311396022` | yes |
| `50002617996_4104030101_CERTS` | Asphalt Prod - Teralba (152) | 152 | NSW | `50002617996_4104030101` | yes |
| `50002617965_4103711576_CERTS` | Auburn | 3002 | NSW | `50002617965_4103711576` | yes |
| `50002617957_4103713125_CERTS` | Auburn | 3002 | NSW | `50002617957_4103713125` | yes |
| `50002755315_4311006315_CERTS` | Eastern Creek | L9.J.170160 | NSW | `50002755315_4311006315` | yes |
| `50002617953_4103803680_CERTS` | Hexham Office | COR-10920006 | NSW | `50002617953_4103803680` | yes |
| `50002617973_4103737079_CERTS` | North Ryde T1 - Level 1 | 1006 | NSW | `50002617973_4103737079` | yes |
| `50002617971_4103737729_CERTS` | North Ryde T1 - Level 1 | 1006 | NSW | `50002617971_4103737729` | yes |
| `50002617975_4103742938_CERTS` | North Ryde T1 - Level 3 | 1007 | NSW | `50002617975_4103742938` | yes |
| `50002617966_4103742939_CERTS` | North Ryde T1 - Level 3 | 1007 | NSW | `50002617966_4103742939` | yes |
| `50002617985_4103742940_CERTS` | North Ryde T1 - Level 4 | 1008 | NSW | `50002617985_4103742940` | yes |
| `50002617958_4103759848_CERTS` | North Ryde T3 - Level 2 | 1013 | NSW | `50002617958_4103759848` | yes |
| `50002617952_4103759849_CERTS` | North Ryde T3 - Level 3 | 1009 | NSW | `50002617952_4103759849` | yes |
| `50002617969_4001200751_CERTS` | PPP - HQJOC (ACT) | 9092 | NSW | `50002617969_4001200751` | yes |
| `50002716068_4103689689_CERTS` | PPP - NSW Schools 2 (Ashtonfield PS) | 9008 | NSW | `50002716068_4103689689` | yes |
| `50002617988_4311006154_CERTS` | PPP - NSW Schools 2 (Elderslie PS) | 9009 | NSW | `50002617988_4311006154` | yes |
| `50002617986_4310934278_CERTS` | PPP - NSW Schools 2 (Halinda SSP) | 9010 | NSW | `50002617986_4310934278` | yes |
| `50002617955_4310957406_CERTS` | PPP - NSW Schools 2 (John Palmer PS) | 9011 | NSW | `50002617955_4310957406` | yes |
| `50002617993_4103766552_CERTS` | PPP - NSW Schools 2 (Kariong) | 9001 | NSW | `50002617993_4103766552` | yes |
| `50002617982_4001198085_CERTS` | PPP - NSW Schools 2 (Kelso HS) | 9002 | NSW | `50002617982_4001198085` | yes |
| `50002617951_4311006155_CERTS` | PPP - NSW Schools 2 (Middleton Grange PS) | 9003 | NSW | `50002617951_4311006155` | yes |
| `50002617970_4310938258_CERTS` | PPP - NSW Schools 2 (Ropes Crossing PS) | 9004 | NSW | `50002617970_4310938258` | yes |
| `50002617959_4310984436_CERTS` | PPP - NSW Schools 2 (Rouse Hill HS) | 9005 | NSW | `50002617959_4310984436` | yes |
| `50002716071_4310955386_CERTS` | PPP - NSW Schools 2 (Tulimbar PS) | 9006 | NSW | `50002716071_4310955386` | yes |
| `50002617995_4103705443_CERTS` | PPP - NSW Schools 2 (Warnervale PS) | 9007 | NSW | `50002617995_4103705443` | yes |
| `50002617960_4103927804_CERTS` | PPP - SICEEP | 9077 | NSW | `50002617960_4103927804` | yes |
| `50002617968_4103927806_CERTS` | PPP - SICEEP | 9077 | NSW | `50002617968_4103927806` | yes |
| `50002617956_4103927808_CERTS` | PPP - SICEEP | 9077 | NSW | `50002617956_4103927808` | yes |
| `50002617980_4103927809_CERTS` | PPP - SICEEP | 9077 | NSW | `50002617980_4103927809` | yes |
| `50002617997_4001287259_CERTS` | RPQ NSW Moree | L9.J.171220 | NSW | `50002617997_4001287259` | yes |
| `50002617983_4001158058_CERTS` | Tamworth | 170937 | NSW | `50002617983_4001158058` | no |
| `50002646141_6305920528_CERTS` | Asphalt Prod - Bayswater (302) | 302 | VIC | `50002646141_6305920528` | yes |
| `50002646138_6001311036_CERTS` | Asphalt Prod - Somerton (303) | L9.J.17032627 | VIC | `50002646138_6001311036` | yes |
| `50002646143_VBBB002698_CERTS` | Asphalt Prod - Wodonga (315) | 315 | VIC | `50002646143_VBBB002698` | yes |
| `50002646142_6407100027_CERTS` | Dandenong - PAV | 517 | VIC | `50002646142_6407100027` | yes |
| `50002646152_6407695655_CERTS` | Mulgrave - Wellington Rd, Clayton | 9118 | VIC | `50002646152_6407695655` | yes |
| `50002646140_6203753676_CERTS` | Utilities Derrimut Office | 7010 | VIC | `50002646140_6203753676` | yes |
| `50002618027_2002254877_CERTS` | Asphalt Prod - Wingfield (523) | 523 | SA | `50002618027_2002254877` | yes |
| `50002618025_2001160742_CERTS` | Gillman - PAV | L9.J.17050664 | SA | `50002618025_2001160742` | yes |
| `50002656871_SAAAAAB023_CERTS` | Largs Bay | 163 | SA | `50002656871_SAAAAAB023` | yes |
| `50002618029_SAAAAAC481_CERTS` | Largs Bay | 163 | SA | `50002618029_SAAAAAC481` | yes |

## Excluded — small market (25)

| Location | Site (register) | State | NMI |
| --- | --- | --- | --- |
| Asphalt Prod - Mogo (154) | Roads - Jerramadra (Mogo) | NSW | `4001127731` |
| RPQ NSW Chinderah | RPQ Chinderra | NSW | `4407159054` |
| Asphalt Prod - Shepparton (308) | Roads Shepparton | VIC | `6204134328` |
| Asphalt Prod - Traralgon (300) | Fowlers Asphalting - Traralgon | VIC | `6306009124` |
| Gippsland Asphalt - Bairnsdale | — | VIC | `6305885252` |
| Somerton Emulsion Plant | Roads - Somerton | VIC | `VDDD001226` |
| Asphalt Prod - Hobart (329) | Roads - Lindisfarne | TAS | `8000002117` |
| Asphalt Prod - Mowbray (360) | New Roads Mowbray | TAS | `8000326927` |
| Austins Ferry | Roads - Granton | TAS | `8000002963` |
| Asphalt Prod - Archerfield (406) | Roads - Archerfield | QLD | `QB05383854` |
| Asphalt Prod - Bli Bli (408) | Roads - Bli Bli | QLD | `3120103988` |
| Asphalt Prod - Brendale (423) | New Brendale Asphalt plant | QLD | `3120725958` |
| Corporate - Offices (Cairns QLD) | Office - Spotless Cairns | QLD | `3030075637` |
| Gympie | Roads - Gympie | QLD | `3120129028` |
| MT-Carrara | Mineral Tech - Carrara | QLD | `QB06081428` |
| MT-Carrara | Mineral Tech - Carrara | QLD | `QB06082220` |
| Maryborough | Rail - Maryborough | QLD | `QGGG000010` |
| Maryborough | Rail - Maryborough | QLD | `QGGG000320` |
| PPP - Southbank TAFE (QLD) | Southbank Tafe PPP | QLD | `3116382269` |
| PPP - Sunshine Coast University Hospital | Spotless -Sunsh Coast Hosp Car Park | QLD | `3120143385` |
| RPQ Spray Seal | RPQ SPRAY SEAL | QLD | `3051770385` |
| RPQ Spray Seal | RPQ SPRAYSEAL | QLD | `3120014382` |
| RPQ Swanbank | RPQ SPRAYSEAL | QLD | `3120070486` |
| Richlands | Engineering - Archerfield | QLD | `3116600011` |
| Teneriffe - Brisbane (QLD) | Corporate Office - Brisbane | QLD | `3117134943` |

## The site register, mapped to Envizi

`Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` adds ten columns to
`Site Register` — the same 341 rows, all commodities and both countries, with the Envizi account each
Connection ID resolves to:

| Col | Contents |
| --- | --- |
| V | **Envizi Account Number** — the best match, or `Not found` |
| W–Y | Account Style, Data Type, Supplier |
| Z–AA | Location, Location Ref |
| AB | Account Status — Active, Replaced *date*, or At Unallocated Accounts |
| AC | Match Basis |
| AD | Other Envizi accounts on the same ID |
| AE | Certificate / virtual meter account — existing, and the planned one where this review creates it |

Matching is on the Connection ID: first as the segment after the last underscore in the Envizi account
number (283 rows), then anywhere in the account number, reference, reader, serial or location account ref
(1 row). Where an ID carries several accounts, the active one of the right data type is shown and the
rest are listed in col AD. Rows with no match are shaded, and a non-active status is shaded amber.

**285 of 341 rows matched.** The 57 that did not are 45 NZ electricity ICPs and 10 NZ gas rows — NZ
per-ICP accounts were replaced in 2023 by one account per location — plus 2 AU small energy sites.

Note: saving through the spreadsheet library rewrites a few Annual Consumption values in column K with a
shorter decimal representation (worst difference 4.5e-16 relative, about a nano-kWh). The stored numbers
are identical at Excel's own precision; no other cell left of column V changes.

## New Zealand

All NZ electricity is renewable under the new arrangements (TOU on Ecotricity since 1 Jul 26; NTOU moving
to Ecotricity 1 Jan 27). 114 of the 158 NZ green ICPs resolve to 80 open Envizi locations; 29 of those
already have a CERTS account; 44 cannot be placed from the extracts. Nothing NZ is set up yet — the NTOU
contract has not started, and for a site whose consumption sits on a per-location account rather than an
`Eco_ICP_` account, what the virtual meter should copy needs deciding first.

## Still open

- The NSW 25-26 LGC emission factor (above) — settle before linking the rest.
- The ten double-counting NMIs, on the electricity side.
- NZ, once the Ecotricity switch is confirmed.
- The Envizi Account Style Link for the certificates style, only if the load tab is ever uploaded.
