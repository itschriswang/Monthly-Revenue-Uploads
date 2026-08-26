# Unallocated Accounts

Accounts sitting against the `Unallocated Accounts` location in Envizi, and the tracker used to
work them back onto real locations.

## Files

| File | What it is |
| --- | --- |
| `Unallocated_Accounts_FY27_Aug26.xlsx` | **The working file.** Current cycle, built from the 25 Aug 2026 extracts in `../FY27/`. |
| `Unallocated_Accounts_FY26_May26.xlsx` | The May 2026 cycle. This is the template the current file follows. |
| `Unallocated Accounts - Proposed Location Links.csv` / `.xlsx` | The flat review that fed the Aug-26 tracker — 136 accounts with match basis and confidence each. Superseded as a working document; kept as the evidence trail behind the tracker's Notes columns. |

## Tracker layout

| Tab | Rows (Aug-26) | Contents |
| --- | --- | --- |
| `1 - Electricity Gas NMI` | 32 | Electricity / natural gas accounts, matched by NMI to an account already allocated to a location. |
| `2 - Fuel Cards FTC` | 91 | Fuel card accounts, matched by job / cost-centre number to a location reference. |
| `3 - BOC Viva` | 13 | BOC and Viva stationary fuel and gas, matched by invoice delivery address. |
| `How to Refresh` | — | The six-step refresh procedure, plus what changed from the May-26 file. |
| `MDS Extract`, `Location Extract`, `Accounts Extract` | — | Paste targets the working tabs look up against. |
| `BOC_*`, `VIVA_*` | — | Ten supplier invoice files, carried over from the May-26 tracker. |

Formula columns are live and read from the three extract tabs. Yellow columns are manual.
Row shading: green / blue alternate for rows that resolve, amber marks rows needing a manual
Envizi search. On `3 - BOC Viva` the row shades itself from the Match Result in col T
(BU Approved / Management Approved / Higher Confidence / Low Confidence / TBA).

## Refreshing for a new cycle

Follow the `How to Refresh` tab. In short: export the MDS, Accounts Extract and Location Extract
from Envizi; paste each into its tab starting at row 3; fill the helper columns down
(Accounts Extract AJ–AL, Location Extract AC–AD); then review the working tabs for accounts that
have been allocated since (delete) or newly appeared (classify into a section).

## Aug-26 rebuild — notes

The Aug-26 cycle was first delivered as a flat two-sheet report. It was rebuilt on the May-26
template so the manual investigation columns carry across cycles.

Five of the thirteen BOC/Viva accounts were still open in May and carry their prior manual columns
forward (Match Result, Status, Notes, Group Sustainability and BU E&S comments).

### Template defects fixed so the formula columns resolve

1. **Restored the `MDS Extract` tab.** It had been deleted from the May file, so every MDS-driven
   formula was left as `#REF!` and read "Not found". The formulas now point at `'MDS Extract'`
   (col P Item Number, V Occurred_On, Z Accrued Data, AA Total Data, AU Total CO2e) and go live as
   soon as the export is pasted in.
2. **NMI is taken from the text after the last underscore, not the first.** Item numbers like
   `DEDI01_8000002117_8000002117` (Shell Energy) failed under the old rule. Accounts Extract helper
   col AJ uses the same rule, so the two always agree.
3. **Accounts Extract helper col AK now treats an account as active only if it is neither replaced
   nor itself unallocated.** Without this, Section 1 cols H and J matched an unallocated account
   against itself and reported "Unallocated Accounts" as its existing location — 6 of the 32 NMIs.

Also added: Location Extract helper cols AC–AD, so the Section 2 job-number lookup works whether
the pasted refs land as text or as numbers.

### Verification

- All 136 source accounts are present across the three tabs (32 + 91 + 13); none dropped or duplicated.
- Every lookup was simulated against the real 25 Aug 26 extracts: 32/32 NMI rows and 91/91 FTC rows
  resolve to the same location as the flat review. The one exception is Synergy NMI `8001014340`,
  where the existing Envizi record carries an 11-digit typo of the NMI — correctly left amber for a
  manual Envizi search, which is the template's designed handling.
- Ship-to numbers for 10 of the 13 BOC/Viva rows are present in the carried-over invoice tabs, so
  cols J–M populate.

### Open items

- **`1006152_Acetylene` has a conflict.** May matched it to Linton Operations on the delivery
  address; the Aug review matched it to Palmerston North Depot on an existing Envizi allocation of
  the same BOC account. May's value is left in cols R/S and the conflict is flagged in Notes —
  needs a decision before loading.
- **Three rows have no invoice file.** `100017373`, `100480339` and Viva `2489625` are not in any
  carried-over invoice tab, so their `Source Invoice File` cell is blank and cols J–M read
  "Not in file". They need a newer invoice file per `How to Refresh` STEP 6.
- **MDS columns read "Not found" / 0 until an MDS export is pasted in.** Section 1 cols E/I,
  Section 2 cols E/L and Section 3 cols O/P/Q/V. No MDS extract for this cycle is in the repo. This
  is a step in the documented refresh, not a fault — they read "Not found" in the May file too, but
  from broken references rather than an empty source.
