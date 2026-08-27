# FY27 — Jul 2026 to Jun 2027

Monthly revenue actuals for FY27 and the Envizi account setup / data load built from them.
One month deep so far: **Jul 2026**.

## Files

| File | What it is |
| --- | --- |
| `Account_Setup_and_Data_Load_-_PM&C_REVJUL26toJUL26_Setup.xlsx` | **The working file, and the one to upload.** All 67 Jul-26 rows, built against the 26 Aug extracts. |
| `Account_Setup_and_Data_Load_-_PM&C_JVREVJUL26toJUL26_Setup.xlsx` | **The JV revenue exclusion counterpart — also to upload.** Five Jul-26 rows loading the JV revenue as negatives (-7.2), so reporting nets to revenue excluding JVs. See [JV revenue exclusion](#jv-revenue-exclusion). |
| `Actual Revenue Jul 26 -unlinked.xlsx` | The raw Jul-26 actuals extract, links removed. 162 rows on `FY27 Rev` totalling 731.9, plus five JV lines totalling 7.2 on `FY27 JV Rev`. |
| `Extract_for_Locations 26 Aug 26.csv` | **Current** locations export, 5,622 rows / 4,710 distinct locations. Includes the six new `REV_` locations. Pasted into the workbook tab of the same name. |
| `Extract_for_Accounts 26 Aug 26.csv` | **Current** accounts export, 59,186 rows. Its 146 `REV_` rows are pasted into the workbook's accounts tab. |
| `Extract_for_Locations 25 Aug 26.csv` | The previous locations export, 5,610 rows / 4,704 locations — the state the workbook was originally built against. |
| `Extract_for_Accounts 25 Aug 26.csv` | The previous accounts export, 59,163 rows. |
| `Setup_locations_TEMPLATE.xlsx` | Bulk location setup template — 946 example rows over 20 columns. |
| `Setup_Direct_Location_Group_Memberships.xlsx` | Bulk group setup template — 936 example rows over 7 columns. `Sheet1` lists the valid Classification groups. |
| `Setup_locations_FY27_Jul26_New_Revenue_Locations.xlsx` | Six new locations for the Jul-26 lines that had none. **Loaded 26 Aug 26.** |
| `Setup_Direct_Location_Group_Memberships_FY27_Jul26_New_Revenue_Locations.xlsx` | Group memberships for those six. **Loaded 26 Aug 26.** |
| `Account Setup and Data Loading report fields - IBM Documentation.pdf` | Envizi's own field reference for the setup and data-load format. |

## Setup workbook layout

| Tab | Contents |
| --- | --- |
| `Account_Setup_and_Data_Load` | The load itself — 67 rows, values only. This is what goes to Envizi. |
| `Prep - with formulas` | The same 67 rows with the formulas that build them, so the load can be rederived. |
| `FY27 Revenue` | Jul-26 actuals rolled to Sub-LOB × Level 2, with the target location name in col E. |
| `Extract_for_Locations 26 Aug 26`, `Extract for Accounts 26 Aug 26` | Paste targets the lookups read against, holding the 26 Aug exports. The tabs are named for the export pasted into them, so both they and the formulas that read them move on each refresh. |
| `Jul Check - By Line Item` | Every line item, revenue sheet vs data load, with a Difference and an OK/not flag. |
| `Monthly Totals Check` | Month totals both sides. Extends by one row per month as FY27 fills out. |

Jul-26 loads as `Revenue - AUD Million` (style link 7868) against organization link 37395, over
the record window 2026-07-01 to 2026-07-31, totalling 731.9 across 28 locations and 28 accounts —
one location per Sub-LOB.

## How the mapping works

Each revenue line maps to a location named `REV_` & UD1 Name/Sub-LOB, and an account named
`FY27REV_` & the same Sub-LOB. `Prep - with formulas` col D then looks that location name up in the
locations extract to get its Location Ref:

```
=IFERROR(INDEX('Extract_for_Locations 26 Aug 26'!$E:$E,
               MATCH(C2,'Extract_for_Locations 26 Aug 26'!$B:$B,0)),"")
```

A Sub-LOB with no matching location returns blank, which is the signal that the location has to be
created before the month can load.

Both col C and col D are live formulas on all 67 rows. Where a location is missing, the temptation
is to hardcode col C to an existing location so col D resolves — that is what Jul-26 did for nine
rows, and it silently posts revenue to the wrong place. Create the location instead.

## Monthly process

1. Add the new month's `Actual Revenue <Mon> <YY> -unlinked.xlsx`.
2. Extend the workbook to cover the new month; the filename range moves,
   e.g. `REVJUL26toJUL26` → `REVJUL26toAUG26`.
3. Check for Sub-LOBs with no location (see below) and set them up before loading.
4. Extend the JV exclusion workbook the same way — one column per month on its `FY27 JV Rev`
   source tab, five negative rows per month on its data load (see below).
5. Verify before relying on it: recalculate all formulas (zero errors), and confirm the month's
   check tabs tie out — every line item OK and the monthly total matching both sides.

## JV revenue exclusion

JV and associate revenue is included in the main revenue tab by default (confirmed 27 Aug 26), but
is to be excluded from all revenue figures. `Account_Setup_and_Data_Load_-_PM&C_JVREVJUL26toJUL26_Setup.xlsx`
— the FY27 counterpart of FY26's `JVREVJUL25toJUN26` workbook — loads the five JV lines from the
actuals extract's `FY27 JV Rev` tab as **negatives** against the JV-specific `REV_<name>` locations,
so reporting nets to revenue excluding JVs. Jul 26: BIA -3.8, EDI Rail- Bombardier Transportation
-3.4, and zeros for Allied Asphalt, Emulco and Isaac Asphalt (-7.2 in total against the 731.9).

Points established while building it (see the workbook's `FY27 JV Revenue` tab notes for the full
record):

- All five `REV_<name>` JV locations already exist **open** in Envizi (reopened for the FY26 load),
  each with both Classification and Portfolio `Revenue` memberships — no location setup needed.
  The five `FY27REV_<name>` accounts don't exist yet; the load creates them.
- In the main tab, BIA rides inside `REV_Transport & Infrastructure AU`, and EDI Rail- Bombardier
  appears as the **"WA JV"** line under TLS Fleet inside `REV_Passenger Through Life Support`.
  (The FY26 workbook's note 4 says EDI was not in the FY26 figures — that's wrong: it's the
  "WA JV" line there too, 35.9 vs 35.6 deducted. The FY26 loaded amounts are unaffected.)
- The deduction uses the JV-source figures, which differ from the main tab by rounding — Jul 26
  leaves a 0.1 residual ("WA JV" 3.5 in the main tab vs EDI 3.4 deducted), the same class of
  residual FY26 documented for BIA (69.9 vs 70.1).

## Jul-26 — lines with no location

Six `REV_` names the Jul-26 upload wants did not exist in the 25 Aug 26 locations extract. Nine rows
of `Account_Setup_and_Data_Load` had been pointed at a stand-in location to get a Location Ref;
they now point at their own, and the six locations are set up ready to load:

| Location | Stand-in it replaced | Setup rows | Jul-26 line items |
| --- | --- | --- | --- |
| `REV_E&U Asset Management (ANZ)` | `REV_EU Gap` | 32 | E&U Asset Management (Australia) |
| `REV_Passenger New Supply and Delivery` | `REV_Passenger North` | 51 | RTS QLD |
| `REV_Passenger Refurbishment` | `REV_Passenger North` | 52 | Maryborough Refurbishment |
| `REV_Passenger Through Life Support` | `REV_Passenger North` | 53–54 | TLS Fleet, TLS Projects |
| `REV_Emerging Markets` | `REV_RTS Opportunities` | 55–57 | RTS FREIGHT, Engineering Consulting, RTS Digital |
| `REV_Intercompany Elimination` | `REV_RTS Head Office` | 59 | Intercompany Elimination |

**Load in this order**, or the data load will fail on a Location Ref Envizi does not know yet:
locations → group memberships → `Account_Setup_and_Data_Load`.

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

The group memberships template links to an external workbook — someone's OneDrive copy of an Envizi
location export — which its own formula columns read. The rows built from it hold plain values and
no formulas, so that link is dropped rather than carried over. Keeping it broke the file: the tooling
that wrote it kept only one of the link's two relationships while still pointing at the other, and
Excel offered to repair the file on open. If a future build of either file draws a repair prompt,
that dangling reference is the first thing to check — every `r:id` in a part must resolve in that
part's `.rels`.

### Refreshing the extract tabs

`Account_Setup_and_Data_Load` col D resolves its Location Ref by looking the location name up in the
locations extract tab, so that tab has to contain every location the month posts to. Between the six
being designed and being created in Envizi it did not, and they were held there as placeholder rows
until the 26 Aug export replaced them.

To refresh: export both extracts, paste each over its tab, rename the tab to the export date, and
update the sheet name in the col D formulas to match. The accounts tab is filtered to rows whose
Location starts `REV_` — 146 of the 59,186 in the 26 Aug export — and no formula reads it, so it is
a reference snapshot rather than a lookup source.

The lookups are whole-column (`$E:$E`, `$B:$B`) rather than bounded to a row count. A bounded range
silently ignores rows past its end when a larger extract is pasted in, which fails as wrong answers
rather than as an error.

### Verification

- Every group row references a location and Location Ref the locations file creates.
- All 67 rows of `Account_Setup_and_Data_Load` resolve a Location Ref; none blank.
- 28 distinct locations against 28 distinct accounts — every Sub-LOB now has its own.
- Only the 18 intended cells changed (col C and col D of the nine rows). Every other cached value in
  the workbook is byte-identical to before the repoint.
- Simulating `MATCH`/`INDEX` independently over the extract tab, all 134 col C/D cells agree with
  their stored values, so the workbook recalculates to what it currently shows. None of the six new
  names is shadowed by an earlier row in col B.
- `Jul Check - By Line Item` is OK on all 67 line items with every difference zero; `Monthly Totals
  Check` ties at 731.9 both sides, difference 0. Repointing moves which location a row posts to, not
  any amount, so both check tabs are unchanged by it.

## The 26 Aug 26 cycle

The first Jul-26 upload went in **before** the six locations existed, so it split: the 58 rows on
locations that already existed loaded (639.0), and the nine rows on the new locations were rejected
on a Location Ref Envizi did not have yet (92.9). The locations and group memberships loaded
afterwards and are correct — the 26 Aug export has all six with the refs the setup file assigned,
each carrying both Classification and Portfolio `Revenue`.

Rather than top up the missing nine, **the partial July load is being deleted and the full 67-row
workbook reloaded.** That is the simpler end state: one load, one provenance, and no delta file to
mistake for a top-up later. Record Entry Method is `Insert`, so this only works if the earlier
records are removed first — reloading over them would double-post the 639.0.

Accounts do not need creating separately; the data load file creates them alongside the records. Six
of the 28 `FY27REV_` accounts do not exist yet and will be created by this load.

The workbook now carries the 26 Aug extracts on both extract tabs, renamed to match, so it no longer
depends on the six placeholder rows that stood in before the locations were real.

## Open items

- **The July reload has not been done.** Delete the existing Jul-26 records first, then upload the
  `Account_Setup_and_Data_Load` tab of the setup workbook — all 67 rows, 731.9.
- **Nine rows, not the ten originally expected.** Counted three ways — the workbook's Location Ref
  lookups, the `Jul Check - By Line Item` tab, and exact and whitespace-normalised matching of all
  28 wanted `REV_` names against the extract. Each gives the same nine rows over six locations. The
  five `FY27 JV Rev` names all have locations. Worth a second look in case there is a tenth line
  that this framing misses.
- **The filename range `REVJUL26toJUL26` is an assumption.** No prior FY26 setup workbook covered a
  single month — the earliest committed one already spanned Jul25–Apr26 — so the single-month form
  was inferred by analogy to the `REVJUL25toJUN26` pattern with start month equal to end month.
