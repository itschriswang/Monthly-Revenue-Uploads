# Large Market Certificates

Virtual certificate accounts for the AU large market electricity sites under the FY26–28 renewal
agreements, and the Envizi upload that creates them.

## Files

| File | What it is |
| --- | --- |
| `Virtual Meter Guide/Large_Market_Virtual_Meters.html` | **Start here.** The whole brief and the working checklist in one page — background, evidence, every account to create with the values to key in and the source to link, the historical `LGCS_` accounts to leave alone, exclusions, NZ, reference. Ticks and notes save in the browser. Open it locally (double-click). |
| `Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx` | The review workbook: 81 register rows with live formulas, the 70 accounts on `Prep` and the load tab (kept as the record of what each account looks like — **not uploaded**, see below), the `Manual Setup Checklist` and `LGCS Accounts to Check` tabs. The `Account_Setup_and_Data_Load_-_PM&C_` prefix is what Envizi processes on if a load is ever needed. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28.xlsx` | The renewal agreement site register. `Site Register` has 81 AU Large Electricity rows; the green rows (78) are the large market accounts in scope, the 3 Northern Territory rows are not green. |
| `ElectricityEnviziSummaryjunejulyaug26.xlsx` | The Jun–Aug 26 monthly summary from Envizi — kWh, cost and CO2e for every electricity account and its green component. Used to confirm each match and to see where an offset is already being recorded. |

The accounts and locations extracts it reads are the ones in `../FY27/` (`Extract_for_Accounts 03 Sep 26.csv`,
`Extract_for_Locations 26 Aug 26.csv`).

## Workbook layout

| Tab | Contents |
| --- | --- |
| `Account_Setup_and_Data_Load` | The 70 accounts in the template's 21 columns, kept as the record — see *A virtual meter has to be empty*. Cols E, H, J, K read the Review/Prep tabs. |
| `Prep - with formulas` | The same 70 rows built by formula from the Review tab, keyed on the Connection ID in col V. |
| `Review - AU Large Market` | One row per AU Large Electricity register row (81). Inputs at the top; the match, the offset checks, a suggested decision by formula, the Decision itself as a dropdown, and the proposed account fields. |
| `Check` | Tie-outs: decisions add up, load rows equal the Create count, no duplicate or pre-existing account numbers, no blank location refs, Prep and load agree, style link filled. |
| `Manual Setup Checklist` | The worklist for creating and linking the 70 by hand — every field to key in, the virtual meter's source account, whether that source has pre-Jul-26 data (date-bound the meter), the historical `LGCS_` account(s) at the site, the incoming retailer's account to add when live, and a Status dropdown. |
| `LGCS Accounts to Check` | The 54 existing certificate accounts at the 40 in-scope sites. All hold 2025-and-earlier data (checked 4 Sep 26), so Has data? is pre-set to Yes and the Action reads keep-as-history; set one to No and it switches to reuse. |
| `Notes` | How it was built and what was assumed. |
| `Site Register (AU Large)`, `Extract for Accounts 03 Sep 26`, `Extract_for_Locations 26 Aug 26`, `Envizi Summary Jun-Aug 26` | The source rows the formulas read. The accounts tab is filtered to the register NMIs plus every certificate account, with the same helper columns the unallocated tracker uses. |

## How the sites were matched

On the connection ID, not the region. The NMI is the text after the last underscore in the Envizi
account number, so each register row was matched to the active electricity account carrying that NMI
(Large Market style preferred where a site has more than one) and the location taken from that account.
All 81 resolved. Five of the NMIs also have a new unallocated account (the Sep-26 unallocated tracker) —
the allocated one is used.

## Scope

In scope: the green AU Large Electricity rows. Named exclusions: the three Northern Territory sites
(Jacana; not green in the register either), QTMP (Torbanlea, `3053253239`), and Pakenham — which is not
in the register's large market rows at all, and in Envizi already carries `LGCS_HCMT` and the SEC VIC
100% Renewable Deduction at HCMT - East Pakenham Depot.

## Is the renewable product LGCs?

For Engie and Origin, yes — `Rates & Source Data` in the budget workbook prices both renewal contracts
with an explicit LGC line, FY27 0.395 c/kWh (Engie) and 0.375 (Origin), FY28 0.375, plus a
"renewable product $/yr". That is 68 of the 78 green sites. The Alinta (WA) and Shell (TAS) contracts
are modelled as an all-in delivered rate with no separate LGC line; Category Management confirms they
are renewable (3 Sep 26: all AU large market sites except the NT are renewable, no small market site
is), and the Alinta accounts already show 100% green kWh in Envizi. The existing `LGCS_<NMI>`
accounts are the same mechanism recorded the Envizi way — 55 of the 69 were created in one batch on
12 Mar 2024 and 11 on 27 Jun 2025. Whether any of them hold data is not visible in the accounts
extract or the electricity summary; a `Certificates - Location` data export would show it. An empty
one is the virtual meter for that site, which is why a location that has one is excluded here rather
than given a second account.

Because of that, the Review tab carries an **Account pattern** input (C14): `Ecotricity - account_CERTS`
(as built) or `AU LGC - LGCS_NMI`, which names the 18 `LGCS_<NMI>` with supplier and reader `LGCs`, the
same as the existing 69. Cols E, H, J and K of the load tab read the Review and Prep tabs, so the
switch and the style link flow straight through; every other load column is a value.

## New Zealand

All NZ electricity is renewable under the new arrangements — the 26 TOU sites on Ecotricity since
1 Jul 26, and the 132 NTOU sites moving to Ecotricity on 1 Jan 27. Against Envizi, 114 of the 158 NZ
green ICPs resolve to 80 open locations: 26 on active accounts, 82 through the closed `<ref>_ICP_<icp>`
accounts that were replaced by the per-location `<ref>_Electricity - Purchased from grid` accounts in
2023, and 6 by a unique street-address match. 29 of those locations already have a CERTS account (the
Ecotricity TOU copies). 44 cannot be placed from the extracts — 40 are not in Envizi under any field,
4 sit only at `_CLOSED_` locations. None are in this load: the NTOU contract has not started, and for a
site whose consumption sits on a per-location account rather than an `Eco_ICP_` account the pattern
to copy needs deciding first.

## What the review found

Of the 78 green rows:

- **70 get a new virtual account** — 18 at sites with no certificate account today, and 52 at sites that already have an `LGCS_<NMI>` account. Those 54 `LGCS_` accounts (40 locations) were checked in Envizi on 4 Sep 26 and **all hold LGC data from 2025 and earlier**, so none is empty, none can be converted to a virtual meter, and none covers the renewal period. They stay as the historical record and the new account sits beside them. (The review workbook's input C15 switches back to excluding those sites if any turn out to be empty after all.)
- **7 are the WA Alinta accounts**, whose own green component has recorded 100% green kWh since the 1 Jul 26 Alinta contract (Jul–Aug 26 in the summary, with negative CO2e) — an offset is already in place without a separate certificate account, so they are excluded. The Alinta contract is an all-in rate with no separate LGC line in the rate model. Flip the Decision to `Create` on the Review tab if a certificate account is wanted as well. (SICEEP's Origin accounts show green kWh only in *June* 26, under the old contract, so they are in the create list.)
- **1 is QTMP** — named exclusion.

### The 70 new virtual accounts

Named off the virtual meter's source account — `<source account>_CERTS` — because `LGCS_<NMI>` is already taken at 40 of the sites. The source is the contracted retailer's account on the NMI where one exists (the Engie and Shell accounts started at the renewal, so they carry no earlier history), otherwise the continuing account. The full list with locations, refs, suppliers and sources is on the `Manual Setup Checklist` tab and in the HTML guide; the 18 sites with no certificate account today are:

| New account | Location | Ref | Supplier |
| --- | --- | --- | --- |
| `900018218_6305885252_CERTS` | Gippsland Asphalt - Bairnsdale | 103.1 | EngieAU |
| `50002617982_4001198085_CERTS` | PPP - NSW Schools 2 (Kelso HS) | 9002 | Origin |
| `50002617969_4001200751_CERTS` | PPP - HQJOC (ACT) | 9092 | Origin |
| `50002716068_4103689689_CERTS` | PPP - NSW Schools 2 (Ashtonfield PS) | 9008 | Origin |
| `50002617995_4103705443_CERTS` | PPP - NSW Schools 2 (Warnervale PS) | 9007 | Origin |
| `50002617993_4103766552_CERTS` | PPP - NSW Schools 2 (Kariong) | 9001 | Origin |
| `50002617986_4310934278_CERTS` | PPP - NSW Schools 2 (Halinda SSP) | 9010 | Origin |
| `50002617970_4310938258_CERTS` | PPP - NSW Schools 2 (Ropes Crossing PS) | 9004 | Origin |
| `50002716071_4310955386_CERTS` | PPP - NSW Schools 2 (Tulimbar PS) | 9006 | Origin |
| `50002617955_4310957406_CERTS` | PPP - NSW Schools 2 (John Palmer PS) | 9011 | Origin |
| `50002617959_4310984436_CERTS` | PPP - NSW Schools 2 (Rouse Hill HS) | 9005 | Origin |
| `50002617988_4311006154_CERTS` | PPP - NSW Schools 2 (Elderslie PS) | 9009 | Origin |
| `50002617951_4311006155_CERTS` | PPP - NSW Schools 2 (Middleton Grange PS) | 9003 | Origin |
| `1003074_3116382269_CERTS` | PPP - Southbank TAFE (QLD) | 9108 | EngieAU |
| `1003075_3120143385_CERTS` | PPP - Sunshine Coast University Hospital | 9078 | EngieAU |
| `DEDI01_8000002117_8000002117_CERTS` | Asphalt Prod - Hobart (329) | 17030565 | ShellEnergyAU |
| `DEDI01_8000002963_CERTS` | Austins Ferry | 12 | ShellEnergyAU |
| `1032371065_8000326927_CERTS` | Asphalt Prod - Mowbray (360) | 360 | ShellEnergyAU |

Three of these are set up against a contracted retailer that differs from the retailer on the live
Envizi account: Southbank TAFE and Sunshine Coast University Hospital (CS Energy → Engie; the Engie
accounts are not yet in Envizi) and Mowbray (Aurora → Shell; Shell's `DEDI01_088_8000326927` is still
at Unallocated Accounts, Sep-26 tracker row 5).

The other 52 — beside a historical `LGCS_` account — are at: Asphalt Prod - Hume (101), Mogo (154) ×2,
Tamworth, RPQ NSW Moree, Auburn ×2, North Ryde T1 L1 ×2 / L3 ×2 / L4, North Ryde T3 L2 / L3, Hexham
Office, PPP - SICEEP ×4, Teralba (152), Eastern Creek, Rosehill (163) ×2, RPQ NSW Chinderah, Bathurst
(156), Somerton (303), Utilities Derrimut Office, Shepparton (308), Bayswater (302), Traralgon (300),
Dandenong - PAV, Mulgrave - Wellington Rd, Wodonga (315), Somerton Emulsion Plant, Corporate - Offices
(Cairns QLD), RPQ Spray Seal ×2, Richlands, Teneriffe - Brisbane, RPQ Swanbank, Bli Bli (408), Gympie,
Brendale (423), Archerfield (406), MT-Carrara ×2, Maryborough ×2, Gillman - PAV, Wingfield (523),
Largs Bay ×2.

### History — date-bound the virtual meter

A virtual meter mirrors every period its source account has data for. 50 of the 70 sources have data
before 1 Jul 26 (the continuing Origin and CS Energy accounts); 20 start at the renewal (Engie, Shell).
Where the source has history, set the meter's effective-from to 2026-07-01 if Envizi offers it, or link
to the new-contract account once it exists — otherwise the meter generates certificates for years that
were not renewable and, for 2025, doubles what the old `LGCS_` accounts already record. The flag is on
every card in the guide and in col Q of the checklist tab.

### Excluded — already renewable (7, all Alinta WA)

Green component already recording the offset: LSE - Perth Convention & Exhibition Centre ×2,
Cannington Emulsion Plant, Maddington - BIT, Albany (601), Geraldton (602), Hope Valley (628).

## How the new accounts are structured

Modelled on the Ecotricity virtual accounts (`Copy of Eco_ICP_..._CERTS`): same location as the large
market account, account style `Certificates - Location - kWh`, account number = the virtual meter's
source account + `_CERTS` (prefix and suffix are inputs on the Review tab; the `Copy of ` Envizi's copy
function adds is left off), Account Reference = the NMI, Supplier = the contracted retailer under the
renewal in Envizi's naming (EngieAU / Origin / ShellEnergyAU), Reader blank. The Account pattern input
can switch the set to the `LGCS_<NMI>` convention, but that now collides at the 40 sites that already
have one — the Check tab counts the collisions.

Envizi will not create an account from this template without a record, so each row carries one
placeholder record — the contract's first month, 2026-07-01 to 2026-07-31, Quantity 0, Entry Method
`Overwrite` — which the real certificate quantity for that month replaces when it is loaded.

## A virtual meter has to be empty — setting them up by hand

Envizi only lets an account be set up as a virtual meter (its records calculated from a source
account) while it holds no records, and the PM&C template cannot create an account without a record.
So the load tab is **not uploaded** for this purpose — its placeholder row would leave every new account
non-empty. It stays as the record of what each account should look like; the `Manual Setup Checklist`
tab is the worklist.

Per account:

1. **Create it empty.** Open the location and Add Account: style `Certificates - Location - kWh`;
   account number, reference and supplier from the checklist (`<source account>_CERTS` / NMI /
   contracted retailer). Save without a record. The Ecotricity ones were made by copying
   the electricity account instead — hence their `Copy of ` prefix; a copy carries no data, so either
   route works.
2. **Link it.** Open the new account and set it up as a virtual meter: source = the large market
   electricity account in the checklist, 100%, add. Where the checklist lists the incoming retailer's
   account (Mowbray's Shell account, still unallocated; Southbank TAFE and Sunshine Coast Hospital's
   Engie accounts once they exist), add it as a second 100% source — the two don't overlap in time, so
   the virtual meter follows the site across the retailer change.
3. **Date-bound it** where the checklist says the source has pre-Jul-26 data (col Q): effective from
   2026-07-01, or wait for the new-contract account and link to that.
4. **Check it.** The new account should show kWh equal to the source for the latest months and the
   location's market-based CO2e should drop to match. Mark Status and Date on the checklist.

The existing `LGCS_` accounts carry Usage Type `Consolidation`, Use `CO2e and Base Measure`,
Apportionment 0 — match those if the screen offers them, otherwise leave the defaults.

**The existing `LGCS_` accounts.** The 54 certificate accounts at the 40 in-scope sites are on
`LGCS Accounts to Check`. Checked in Envizi on 4 Sep 26: all hold LGC data from 2025 and earlier, so
none is empty and none can be converted — they stay as the historical record and the new account is
created beside each. Col I is pre-set to Yes; if one turns out to be empty, set it to No and the Action
column switches to reuse (link it as the virtual meter of the live electricity account(s) listed). Three
of the 54 sit on a different NMI to the register's (Shepparton's `LGCS_VCCCSC0020`, Hexham Office's
`LGCS_4103893142`, RPQ Spray Seal's `LGCS_3120136120`) and are flagged amber.

## Before uploading

1. **Fill the Account Style Link** for `Certificates - Location - kWh` in the yellow cell on the Review
   tab (Envizi > Admin > Account Styles). It is mandatory, it is the one value not in any extract, and
   the Check tab reads `NOT FILLED` until it is there. It flows to col E of the load and prep tabs.
2. Confirm the Decision column — anything changed from Suggested shows red on the Review tab and counts
   on the Check tab.
3. Check tab all OK, recalculate, save, upload the first tab.
