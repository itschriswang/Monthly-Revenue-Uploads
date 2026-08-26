# FY27 — Jul 2026 to Jun 2027

Monthly revenue actuals for FY27 and the Envizi account setup / data load built from them.
One month deep so far: **Jul 2026**.

## Files

| File | What it is |
| --- | --- |
| `Account_Setup_and_Data_Load_-_PM&C_REVJUL26toJUL26_Setup.xlsx` | **The working file.** The setup and data-load workbook for Jul-26. |
| `Actual Revenue Jul 26 -unlinked.xlsx` | The raw Jul-26 actuals extract, links removed. 162 rows on `FY27 Rev` totalling 731.9, plus five JV lines totalling 7.2 on `FY27 JV Rev`. |
| `Extract_for_Locations 25 Aug 26.csv` | Envizi locations export, 5,610 rows / 4,704 distinct locations. The lookup source for location refs. |
| `Extract_for_Accounts 25 Aug 26.csv` | Envizi accounts export, 59,163 rows. |
| `Setup_locations_TEMPLATE.xlsx` | Bulk location setup template — 946 example rows over 20 columns. |
| `Setup_Direct_Location_Group_Memberships.xlsx` | Bulk group setup template — 936 example rows over 7 columns. `Sheet1` lists the valid Classification groups. |
| `Setup_locations_FY27_Jul26_New_Revenue_Locations.xlsx` | Six new locations for the Jul-26 lines that had none. Not yet loaded. |
| `Setup_Direct_Location_Group_Memberships_FY27_Jul26_New_Revenue_Locations.xlsx` | Group memberships for those six. Load **after** the locations. Not yet loaded. |
| `Account Setup and Data Loading report fields - IBM Documentation.pdf` | Envizi's own field reference for the setup and data-load format. |

## Setup workbook layout

| Tab | Contents |
| --- | --- |
| `Account_Setup_and_Data_Load` | The load itself — 67 rows, values only. This is what goes to Envizi. |
| `Prep - with formulas` | The same 67 rows with the formulas that build them, so the load can be rederived. |
| `FY27 Revenue` | Jul-26 actuals rolled to Sub-LOB × Level 2, with the target location name in col E. |
| `Extract_for_Locations 25 Aug 26`, `Extract for Accounts 25 Aug 26` | Paste targets the lookups read against. |
| `Jul Check - By Line Item` | Every line item, revenue sheet vs data load, with a Difference and an OK/not flag. |
| `Monthly Totals Check` | Month totals both sides. Extends by one row per month as FY27 fills out. |

Jul-26 loads as `Revenue - AUD Million` (style link 7868) against organization link 37395, over
the record window 2026-07-01 to 2026-07-31, totalling 731.9 across 24 locations and 28 accounts.

## How the mapping works

Each revenue line maps to a location named `REV_` & UD1 Name/Sub-LOB, and an account named
`FY27REV_` & the same Sub-LOB. `Prep - with formulas` col D then looks that location name up in the
locations extract to get its Location Ref:

```
=IFERROR(INDEX('Extract_for_Locations 25 Aug 26'!$E$2:$E$5611,
               MATCH(C2,'Extract_for_Locations 25 Aug 26'!$B$2:$B$5611,0)),"")
```

A Sub-LOB with no matching location returns blank, and the row has to be pointed at a stand-in
location by hand until one is created.

## Monthly process

1. Add the new month's `Actual Revenue <Mon> <YY> -unlinked.xlsx`.
2. Extend the workbook to cover the new month; the filename range moves,
   e.g. `REVJUL26toJUL26` → `REVJUL26toAUG26`.
3. Check for Sub-LOBs with no location (see below) and set them up before loading.
4. Verify before relying on it: recalculate all formulas (zero errors), and confirm the month's
   check tabs tie out — every line item OK and the monthly total matching both sides.

## Jul-26 — lines with no location

Six `REV_` names the Jul-26 upload wants do not exist in the 25 Aug 26 locations extract, so nine
rows of `Account_Setup_and_Data_Load` are pointed at a stand-in location:

| Wanted location | Stand-in now in the load | Setup rows | Jul-26 line items |
| --- | --- | --- | --- |
| `REV_E&U Asset Management (ANZ)` | `REV_EU Gap` | 32 | E&U Asset Management (Australia) |
| `REV_Passenger New Supply and Delivery` | `REV_Passenger North` | 51 | RTS QLD |
| `REV_Passenger Refurbishment` | `REV_Passenger North` | 52 | Maryborough Refurbishment |
| `REV_Passenger Through Life Support` | `REV_Passenger North` | 53–54 | TLS Fleet, TLS Projects |
| `REV_Emerging Markets` | `REV_RTS Opportunities` | 55–57 | RTS FREIGHT, Engineering Consulting, RTS Digital |
| `REV_Intercompany Elimination` | `REV_RTS Head Office` | 59 | Intercompany Elimination |

Only the *location* is a stand-in. Col H already carries the true account name on these rows —
`FY27REV_Emerging Markets`, not `FY27REV_RTS Opportunities` — so the accounts need no rework.

### The two setup files

`Setup_locations_FY27_Jul26_New_Revenue_Locations.xlsx` creates the six. All are Australian, so
they take the template's Australian block: Country `Australia`, Region `North Ryde`, Region Label
`North Ryde [New South Wales]`, Station Assignment Method `Default station`, no weather-station
over-ride. (Only the template's 134 New Zealand rows carry `Auckland, Whenuapai Aws` on
`Manual over-ride`; its 812 Australian rows are blank there.) Location Type `Other` matches the
template — all 946 rows — and three of the four stand-ins.

`Ref No` is inherited from the stand-in. `REV_` locations already share a Ref No where they share a
source job: `REV_Utilities Gap` / `REV_Utilites Gap`, `REV_T&I Head Office` / `REV_VEC Contracting`,
`REV_AU National Operations` / `REV_BIA`. `Location Ref` is a new mnemonic in the established `REV_`
style (`RTSOPPS`, `RTSQLD`, `SICSHE`, `CORIE`):

| Location | Location Ref | Ref No |
| --- | --- | --- |
| `REV_E&U Asset Management (ANZ)` | `EUAMANZ` | `L9.J.392150` |
| `REV_Passenger New Supply and Delivery` | `RTSPNSD` | `L9.J.709250` |
| `REV_Passenger Refurbishment` | `RTSPREF` | `L9.J.709250` |
| `REV_Passenger Through Life Support` | `RTSPTLS` | `L9.J.709250` |
| `REV_Emerging Markets` | `RTSEMKT` | `L9.J.709010` |
| `REV_Intercompany Elimination` | `RTSICE` | `L9.J.799999` |

Each was checked against the 25 Aug 26 extract; none collides with an existing Location Ref.

`Setup_Direct_Location_Group_Memberships_FY27_Jul26_New_Revenue_Locations.xlsx` gives each two
memberships, which is what 70 of the 72 existing `REV_` locations carry:

1. **Classification** — `Operational Control` > division, copied from the stand-in.
   `Energy and Utilities (EU)` for the first, `Rail & Transit Systems (RTS)` for the other five.
   Both appear verbatim on the template's `Sheet1`.
2. **Portfolio** — `Revenue`, a flat single-level group, so Group Level 2 and 3 stay blank. The
   template ships only Classification rows, so this comes from the extract, where it reads
   `Portfolio / Revenue / Revenue / Revenue` — the extract right-aligns the leaf into Level 3 and
   pads the levels above it. Without this the new locations sit outside the Revenue portfolio that
   every other `REV_` location reports through.

`REV_Energy & Industrial` and `REV_Telecommunications & Networks` are the two existing `REV_`
locations missing the Portfolio membership. They look like gaps rather than a pattern to follow.

Both files keep the templates' headers, column widths and `Sheet1` reference tab unchanged, and add
a `Notes` tab recording which upload rows each location serves and where its attributes came from.

### Verification

- Every group row references a location and Location Ref the locations file creates.
- Simulating the load against the extract, all 67 rows of the setup workbook resolve to their own
  location, none left unmatched.

## Open items

- **The two setup files have not been loaded into Envizi.** Locations first, then group memberships
  — new locations are unassigned until the second file goes in.
- **The setup workbook still points at the stand-ins.** Loading the six locations does not move the
  revenue on its own. Rows 32 and 51–59 of `Account_Setup_and_Data_Load` (and `Prep - with formulas`)
  need repointing at the new locations and refs afterwards. `Prep` col D picks the ref up
  automatically once a refreshed locations extract is pasted in; col C is the manual part.
- **Nine rows, not the ten originally expected.** Counted three ways — the workbook's Location Ref
  lookups, the `Jul Check - By Line Item` tab, and exact and whitespace-normalised matching of all
  28 wanted `REV_` names against the extract. Each gives the same nine rows over six locations. The
  five `FY27 JV Rev` names all have locations. Worth a second look in case there is a tenth line
  that this framing misses.
- **The filename range `REVJUL26toJUL26` is an assumption.** No prior FY26 setup workbook covered a
  single month — the earliest committed one already spanned Jul25–Apr26 — so the single-month form
  was inferred by analogy to the `REVJUL25toJUN26` pattern with start month equal to end month.
