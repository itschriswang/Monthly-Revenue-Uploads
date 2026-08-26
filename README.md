# Monthly-Revenue-Uploads

Monthly revenue actuals and the account setup / data load workbooks built from them, organised by fiscal year (July–June).

## Layout

```
FY26/                   Jul 2025 – Jun 2026
FY27/                   Jul 2026 – Jun 2027
Unallocated Accounts/   Unallocated-account trackers, by MDS cycle
```

Each fiscal year folder contains:

- **`Actual Revenue <Mon> <YY> -unlinked.xlsx`** — the raw monthly actuals extract (one file per month, links removed).
- **`Account_Setup_and_Data_Load_-_PM&C_REV<start>to<end>_Setup.xlsx`** — the setup and data-load workbook covering that month range, built from the monthly actuals. Interim versions from earlier in the year are kept alongside the latest (e.g. FY26 has `...toAPR26`, `...toMAY26`, and the final `...toJUN26`).
- **`Account_Setup_and_Data_Load_-_PM&C_JVREV...`** — the JV revenue exclusion counterpart workbook, where one has been produced.
- **`JV Revenue MDS.xlsx` / `all Revenue MDS.xlsx`** — MDS reference extracts used when building the FY26 workbooks.

## Monthly process

1. Add the new month's `Actual Revenue <Mon> <YY> -unlinked.xlsx` to the fiscal year folder.
2. Extend the year's `Account_Setup_and_Data_Load` workbook to cover the new month (the filename range moves, e.g. `REVJUL26toJUL26` → `REVJUL26toAUG26`).
3. Verify before relying on it: recalculate all formulas (zero errors), and confirm the month's check sheets tie out — every line item OK and the monthly total matching between the revenue sheet and the data load.

## New revenue locations

The setup workbook maps each revenue line to a location named `REV_` & UD1 Name/Sub-LOB. When a
month introduces a Sub-LOB that has no such location, its rows have to ride on a substitute until
the location is created. Two bulk-upload templates in `FY27/` cover that:

- **`Setup_locations_TEMPLATE.xlsx`** — bulk location setup. Australian rows are Region `North Ryde`
  / `North Ryde [New South Wales]` on `Default station` with no weather station; New Zealand rows are
  `Auckland` / `Auckland [New Zealand]` on `Manual over-ride` with `Auckland, Whenuapai Aws`. Copy the
  region and weather-station block from an equivalent location rather than deriving it.
- **`Setup_Direct_Location_Group_Memberships.xlsx`** — bulk group setup, loaded *after* the locations,
  which are unassigned until it is. `Sheet1` lists the valid Classification groups.

Existing `REV_` locations carry two memberships: Classification `Operational Control` > division, and
Portfolio `Revenue`. Both are needed for a new location to report like its peers.

Files produced from the templates for a given month keep the cycle in the name, e.g.
`Setup_locations_FY27_Jul26_New_Revenue_Locations.xlsx` and
`Setup_Direct_Location_Group_Memberships_FY27_Jul26_New_Revenue_Locations.xlsx` — six locations
covering the nine Jul-26 upload rows that had none. Each carries a `Notes` tab recording which upload
rows it serves and which existing location its attributes were copied from.

## Unallocated accounts

Accounts sitting against the `Unallocated Accounts` location in Envizi are worked in a tracker built
on the May-26 template. The workbooks and the full write-up live in **`Unallocated Accounts/`** — see
[`Unallocated Accounts/README.md`](Unallocated%20Accounts/README.md) for the tab layout, the refresh
procedure and the open items on the current cycle.
