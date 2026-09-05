# Claude in Chrome prompts

What I paste into Claude in Chrome with Envizi (`au001.envizi.com`) open in the active tab. Each has been
run at least once against the real screens; the quirks noted inside them are real. Keep Envizi in front
while it works — it only sees the active tab.

Progress as of the 05 Sep 26 extract: **43 of 60** permanent accounts built. Prompt 1 below is the last 17.
Run prompt 0b first — Mogo's two certificate accounts are not where the last export left them. Prompt 3 (the
25-26 factors) is for a later session.

---

## 1 · Create the virtual accounts — the last 17 of section 2

```
You're helping me set up renewable-certificate virtual accounts in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Work through the accounts
listed at the bottom ONE AT A TIME, in order.

THE ONE RULE THAT MATTERS
An account can only be set up as a virtual account while it holds NO records. So
the account is created first and saved empty, and only then linked. Never add
data to it.

THIS BATCH HAS DECOYS
On 12 of these NMIs the OLD retailer's account is still open at the same location,
with data, under the same NMI. It is NOT the source. The source is always the
account I name — the 9000182xx Engie one, or the DEDI01 Shell one — never the
50002xxx Origin one. I've marked every decoy below. Match the full account number
character for character.

MULTIPLE ACCOUNTS AT ONE LOCATION
Largs Bay needs two. Find the location once, then repeat steps 3–6 for each.
Mogo already has 50002617992_4204072845_CERTS — that is the OTHER NMI at that
site; leave it and build the one listed.

=== STEP 1 · Find the location ===
Top-right search, dropdown set to "Locations". Search the location name, open it.
Confirm the Location Ref on the Summary page matches the ref I give you — several
locations share a name, the ref is what disambiguates. If the ref doesn't match, stop.

=== STEP 2 · Open the account list ===
From the location Summary page: Quick links → Accounts. Click "Show All Accounts".
Before creating anything, filter the Account Number column on "CERTS" and confirm
MY EXACT TARGET NUMBER isn't there, then clear the filter. The filter sometimes
renders as a search textbox and sometimes as a multi-select checkbox list. Other
_CERTS rows at the location are expected. If my exact target exists, stop and tell
me — do not edit or reuse it.

=== STEP 3 · Create the account, empty ===
Click the blue "Create New..." button and set:

  Account style      Certificates - Location - kWh
  Account number     as listed below
  Account Ref        the NMI as listed below
  Supplier           LGC Virtual Account
  Reader             leave blank
  Opened On          2026-07-01   (field displays as 7/1/2026)

Leave Reader, Linked Meter, Replaced On and Sub Type blank. Account Style is a jqx
DIV, not a native select — form_input will fail on it. Click it open and type into
its internal Search box, then click the filtered result. The Opened On calendar
opens on the current month, so page back to July 2026 and click 1.
Save. Do NOT add any records, monthly data or capture data.

=== STEP 4 · Open Virtual Account Setup ===
Back in the account list, tick the checkbox on the row for the account you just
created, then click the blue "Actions" button and choose "Virtual Account Setup".

⚠ That same Actions menu also holds "Delete Account(s)", "Close Account(s)" and
"Move Account". Do not click any of those, ever. Screenshot the menu and confirm
before clicking. If you're not certain, stop and show me.

The grid sometimes shows a second row as pre-ticked — a display artifact. Confirm
the breadcrumb on the Virtual Account Relationships page names my new _CERTS
account and the grid reads 0 Row. If it names anything else, stop.

=== STEP 5 · Create the relationship ===
On "Virtual Account Relationships" click the blue "Create New...". A "Virtual
relationship" dialog opens with three tabs. Fill all three BEFORE saving:

- Select rule — Measure: Total Certificates. Data Rule: 100% Renewable Energy
  Certificates (subtitle "Kilowatt hours*Value Variable"). The Measure dropdown
  occasionally renders empty on first click; click it again.

- Source data — Left pane "Available", right pane "Selected". Expand "Kilowatt
  hours", then the location, then click the ⊕ next to the SOURCE ACCOUNT I name.
  Zoom in and match the FULL account number character for character. Add that
  one account and nothing else. The Selected pane should show Kilowatt hours →
  the location → the one account, then "*" and "Value Variable" — leave those
  exactly as the rule sets them.

- Condition (optional) — Effective From: July 2026 (the picker shows "2026 July").
  Effective To: leave blank. This is what stops the virtual account reaching back
  before the renewal. It is not optional for us.

Then SAVE. Confirm the grid reads 1 Row with Formula "Kilowatt hours*Value Va...",
Effective From 7/1/2026, Effective To blank.

=== STEP 6 · Check it ===
Open the new account and confirm Opened On reads 7/1/2026 and there is exactly one
relationship. Read the figures via Review → Monthly Data in the account nav — the
Summary chart tooltips don't render. Confirm Jul and Aug 2026 kWh match the
"Expect" line and there is NO June 2026 row. If June has a value, Effective From
didn't take — stop and tell me.

======================= THE ACCOUNTS · 17 across 16 locations =======================

### Asphalt Prod - Mogo (154) — ref 154   [NSW]
    Leave alone here: LGCS_4001127731, LGCS_4204072845
    50002617992_4204072845_CERTS is ALSO here, opened 7/1/2026, and holds no data. Do
    not create it again. If prompt 0b showed it has no relationship, it is empty and
    ready: skip step 3 for it and run steps 4–6 with src 50002617992_4204072845,
    expecting Jun none · Jul 29,519 · Aug 28,511. If it already has a relationship to
    that account, leave it. If its relationship points at 50002769514_4001127731 or
    its Account Ref reads 4001127731, stop and show me — that is the 4 Sep account
    renamed onto the wrong NMI.
 1. 50002769514_4001127731_CERTS · ref 4001127731 · src 50002769514_4001127731
    Expect Jun none · Jul 3,499 · Aug 3,499
    (This one existed on 4 Sep and has since gone. Step 2's CERTS filter tells you
    whether it is back; if it is there, stop and show me rather than remake it.)

### Asphalt Prod - Somerton (303) — ref L9.J.17032627   [VIC]
    Leave alone here: LGCS_6001311036
 2. 900018217_6001311036_CERTS · ref 6001311036 · src 900018217_6001311036
    Expect Jun none · Jul 95,120 · Aug 95,120
    ⚠ DECOY, do NOT pick: 50002646138_6001311036

### Utilities Derrimut Office — ref 7010   [VIC]
    Leave alone here: LGCS_6203753676
 3. 900018212_6203753676_CERTS · ref 6203753676 · src 900018212_6203753676
    Expect Jun none · Jul 25,947 · Aug 25,947
    ⚠ DECOY, do NOT pick: 50002646140_6203753676

### Asphalt Prod - Shepparton (308) — ref 308   [VIC]
    Leave alone here: LGCS_VCCCSC0020
 4. 900018214_6204134328_CERTS · ref 6204134328 · src 900018214_6204134328
    Expect Jun none · Jul 51,998 · Aug 51,998
    ⚠ DECOY, do NOT pick: 50002946681_6204134328

### Asphalt Prod - Bayswater (302) — ref 302   [VIC]
    Leave alone here: LGCS_6305920528
 5. 900018215_6305920528_CERTS · ref 6305920528 · src 900018215_6305920528
    Expect Jun none · Jul 77,307 · Aug 77,307
    ⚠ DECOY, do NOT pick: 50002646141_6305920528

### Asphalt Prod - Traralgon (300) — ref 300   [VIC]
    Leave alone here: LGCS_6306009124
 6. 900018219_6306009124_CERTS · ref 6306009124 · src 900018219_6306009124
    Expect Jun none · Jul 29,711 · Aug 29,711
    ⚠ DECOY, do NOT pick: 50002929573_6306009124

### Dandenong - PAV — ref 517   [VIC]
    Leave alone here: LGCS_6407100027
 7. 900018211_6407100027_CERTS · ref 6407100027 · src 900018211_6407100027
    Expect Jun none · Jul 9,177 · Aug 9,177
    ⚠ DECOY, do NOT pick: 50002646142_6407100027

### Mulgrave - Wellington Rd, Clayton — ref 9118   [VIC]
    Leave alone here: LGCS_6407695655
 8. 900018210_6407695655_CERTS · ref 6407695655 · src 900018210_6407695655
    Expect Jun none · Jul 2,797 · Aug 2,797
    ⚠ DECOY, do NOT pick: 50002646152_6407695655

### Asphalt Prod - Wodonga (315) — ref 315   [VIC]
    Leave alone here: LGCS_VBBB002698
 9. 900018213_VBBB002698_CERTS · ref VBBB002698 · src 900018213_VBBB002698
    Expect Jun none · Jul 33,474 · Aug 33,474
    ⚠ DECOY, do NOT pick: 50002646143_VBBB002698

### Somerton Emulsion Plant — ref 8001   [VIC]
    Leave alone here: LGCS_VDDD001226
10. 900018216_VDDD001226_CERTS · ref VDDD001226 · src 900018216_VDDD001226
    Expect Jun none · Jul 86,904 · Aug 86,904

### MT-Carrara — ref MT-39510068   [QLD]
    Leave alone here: LGCS_QB06081428, LGCS_QB06082220, 900018198_QB06081428_CERTS
11. 900018193_QB06082220_CERTS · ref QB06082220 · src 900018193_QB06082220
    Expect Jun none · Jul 7,270 · Aug 6,384

### Gillman - PAV — ref L9.J.17050664   [SA]
    Leave alone here: LGCS_2001160742
12. 900018206_2001160742_CERTS · ref 2001160742 · src 900018206_2001160742
    Expect Jun none · Jul 11,104 · Aug 11,104
    ⚠ DECOY, do NOT pick: 50002618025_2001160742

### Asphalt Prod - Wingfield (523) — ref 523   [SA]
    Leave alone here: LGCS_2002254877
13. 900018209_2002254877_CERTS · ref 2002254877 · src 900018209_2002254877
    Expect Jun none · Jul 118,252 · Aug 118,251
    ⚠ DECOY, do NOT pick: 50002618027_2002254877

### Largs Bay — ref 163   [SA]   (2 accounts)
    Leave alone here: LGCS_SAAAAAB023, LGCS_SAAAAAC481
14. 900018208_SAAAAAB023_CERTS · ref SAAAAAB023 · src 900018208_SAAAAAB023
    Expect Jun none · Jul 42,553 · Aug 42,553
    ⚠ DECOY, do NOT pick: 50002656871_SAAAAAB023
15. 900018207_SAAAAAC481_CERTS · ref SAAAAAC481 · src 900018207_SAAAAAC481
    Expect Jun none · Jul 12,365 · Aug 12,365
    ⚠ DECOY, do NOT pick: 50002618029_SAAAAAC481

### Asphalt Prod - Hobart (329) — ref 17030565   [TAS]
16. DEDI01_8000002117_8000002117_CERTS · ref 8000002117 · src DEDI01_8000002117_8000002117
    Expect Jun none · Jul 38,240 · Aug 38,240

### Austins Ferry — ref 12   [TAS]
17. DEDI01_8000002963_CERTS · ref 8000002963 · src DEDI01_8000002963
    Expect Jun none · Jul 7,781 · Aug 7,781

====================================================================================

After each account, report: the account number created, Opened On, the exact
source account you selected, Effective From, and the Jun/Jul/Aug figures against
what I expected. Do number 1, then stop and show me before starting number 2 —
once I've confirmed it I'll tell you to run the rest without stopping.

RULES
- Never delete, close, move or edit the SOURCE account, a decoy, or any LGCS_ account.
- If my exact target account number already exists, stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.
- Never click Save or Delete on a form you're unsure about.

WORKED EXAMPLE
50002617964_NAAA00AC25_CERTS at Asphalt Prod - Bathurst (156) is done and correct —
source 50002617964_NAAA00AC25, measure Total Certificates, rule 100% Renewable
Energy Certificates.
```

---

## 2 · Close the 14 double-counting accounts (section 1)

```
You're helping me close off accounts in IBM Envizi (au001.envizi.com). I'm logged
in on the Envizi tab. Work through the accounts listed at the bottom ONE AT A
TIME, in order.

WHAT "CLOSE" MEANS HERE
Set the account's Replaced On date. Nothing else. Do NOT delete, move or merge
any account, and do NOT touch Opened On - it sits directly under Replaced On on
the same form and must stay as it is.

WHY
On each of these NMIs the site switched retailer on 1 Jul 2026 and the new
account is already billing the actuals, but the old account was never closed
so it keeps accruing the same months. Closing it at 30 Jun 2026 stops the
double count from July on. The June actual stays where it is.

THIS BATCH HAS DECOYS
The NEW account sits at the same location under the same NMI. It is the
9000182xx Engie one (or the 1003xxx CS Energy one for the last two). Never
open Edit Account on it. The account to close is always the one I name -
match the full account number character for character.

=== STEP 1 · Find the account ===
Top-right search, dropdown set to "Accounts". Paste the full account number,
open it. You land on the Account Summary page. Confirm three things before
going further: the account number in the header and left panel is exactly
mine, "Relates to" is the location I give you, and "Replaced On : -" (or the
date I say it currently reads). If any of those disagree, stop and show me.

=== STEP 2 · Open the form ===
Click the blue "Actions" button (top right, next to Page Settings). The menu
has Capture Data, Edit Account and Account Settings. Choose "Edit Account".
Do NOT choose Capture Data.

=== STEP 3 · Set Replaced On ===
On the form find "Replaced On:" - a date field with a calendar icon. Click the
calendar icon. It opens on the current month, so page back to the month I
give you and click the day. The field should then read the date in m/d/yyyy
form (30 Jun 2026 shows as 6/30/2026). If typing works better, type it and
tab out, then read it back to check the month and day didn't swap.

Leave "Opened On:" exactly as it was - blank stays blank, a date stays that
date. Change nothing else on the form.

Save.

=== STEP 4 · Check it ===
Back on the Account Summary page, the left panel should now read
"Replaced On : <the date>". Then Review -> Monthly Data: Jun 2026 should
still show its actual; Jul and Aug 2026 should no longer accrue. If the
accruals are still there straight after saving, note it - Envizi can take a
refresh to drop them - and move on.

Report, per account: the account number, the location, what Replaced On read
before, what it reads now, and whether Opened On is unchanged.

Do the first one, stop and show me before continuing. Once I confirm, work
down the list without stopping, and tell me about any account that already
had a Replaced On, that you couldn't find, or where the screen didn't match.

================== THE ACCOUNTS · Replaced On = 30 Jun 2026 ==================

Old Origin account, site now on Engie (9000182xx is the new one - leave it):

 1. 50002646138_6001311036   Asphalt Prod - Somerton (303)       new: 900018217_6001311036
 2. 50002646140_6203753676   Utilities Derrimut Office           new: 900018212_6203753676
 3. 50002946681_6204134328   Asphalt Prod - Shepparton (308)     new: 900018214_6204134328
 4. 50002646141_6305920528   Asphalt Prod - Bayswater (302)      new: 900018215_6305920528
 5. 50002929573_6306009124   Asphalt Prod - Traralgon (300)      new: 900018219_6306009124
      Replaced On currently reads 10/30/2026 - a date in the future, so the
      account is still accruing. Change it to 6/30/2026; do not leave it.
 6. 50002646142_6407100027   Dandenong - PAV                     new: 900018211_6407100027
 7. 50002646152_6407695655   Mulgrave - Wellington Rd, Clayton   new: 900018210_6407695655
 8. 50002646143_VBBB002698   Asphalt Prod - Wodonga (315)        new: 900018213_VBBB002698
 9. 50002618025_2001160742   Gillman - PAV                       new: 900018206_2001160742
10. 50002618027_2002254877   Asphalt Prod - Wingfield (523)      new: 900018209_2002254877
11. 50002656871_SAAAAAB023   Largs Bay                           new: 900018208_SAAAAAB023
12. 50002618029_SAAAAAC481   Largs Bay                           new: 900018207_SAAAAAC481

=============== TWO MORE · date to be confirmed, do these LAST ================

Second CS Energy account on the same NMI, created by the Utilities Connector
with no Opened On. The 1003xxx account is the live one - leave it.

13. 5000021_3120129028       Gympie                              live: 1003085_3120129028
14. 5000021_QB05383854       Asphalt Prod - Archerfield (406)    live: 1003081_QB05383854

For these two, before opening Edit Account: open the LIVE 1003xxx account,
Review -> Monthly Data, and tell me the earliest month it holds data. The
connector closed the other 5000021_ accounts the day before their 1003xxx
replacement opened (31 Mar, 31 May or 30 Jun 2026). Show me what you find
and STOP - I'll give you the date, then do steps 1-4.

RULES
- Replaced On only. Never delete, move, or edit anything else on any account.
- Never open Edit Account on the new 9000182xx / 1003xxx account.
- If the account already has a Replaced On other than the one I've noted, stop
  and show me.
- If a screen doesn't match what I've described, stop and describe what you see.
```

Expected after the run: the 12 Origin accounts read Replaced On 6/30/2026 on their Summary pages, Traralgon
included, and the next accounts extract shows them with `Replaced On` = 30 Jun 2026. Section 1 on the guide
page reads from the extract, so it catches up on the next rebuild.

---

## 3 · The 25-26 LGC emission factors

```
You're helping me add custom emission factors in IBM Envizi (au001.envizi.com).

We already have LGC certificate factors for 23-24 and 24-25, and one for 25-26
(Victoria only). I need the rest of the 25-26 set. Each is the NEGATIVE of that
state's Scope 2 factor from National Greenhouse Accounts Factors 2025.

Admin → Custom Factors. Wait out the loading spinner. In the Name filter search
"lgc" and open LGCs NSW 24-25 (Region "Australia - New South Wales", -0.66) as
the template — note every field and screenshot it. Do NOT use LGCs Victoria
25-26 as the template: its Region reads plain "Australia", which is wrong.

Existing rows read: Data Type Certificates - Location - kWh, Factor Set Custom -
Downer, Sub Type Default.

Create New for each, identical to the template except:

  Name              Region                                     Total CO2e
  LGCs NSW 25-26    Australia - New South Wales                 -0.64
  LGCs ACT 25-26    Australia - Australian Capital Territory    -0.64
  LGCs QLD 25-26    Australia - Queensland                      -0.67
  LGCs SA 25-26     Australia - South Australia                 -0.22
  LGCs TAS 25-26    Australia - Tasmania                        -0.20
  LGCs NT 25-26     Australia - Northern Territory              -0.56
  LGCs WA 25-26     Australia - Western Australia               -0.50

Match each name's abbreviation to that state's own existing rows. Every value is
NEGATIVE — if a field won't take a minus, stop. Check for an existing 25-26 row
for the region first; skip and tell me if one exists. Never edit or delete an
existing factor. Do NSW first, stop and show me, then the rest.
```

---

## 0b · Mogo — what is actually there (read-only)

```
On the Envizi tab. Read-only — create, edit, save or delete nothing.
Find location "Asphalt Prod - Mogo (154)" (Location Ref 154), Quick links →
Accounts, Show All Accounts, filter Account Number on "CERTS". List every row you
see with its full account number, Account Ref, Supplier and Opened On.

Then for each _CERTS row whose supplier is LGC Virtual Account: tick it, Actions →
Virtual Account Setup, and tell me what the Virtual Account Relationships grid
shows — 0 Row, or the source account, Effective From and Effective To. Screenshot
the grid. Do not click Create New, Delete, Close or Move. Then open the account and
read Review → Monthly Data for Jun, Jul and Aug 2026.

I expect to see 50002617992_4204072845_CERTS (Account Ref 4204072845). Tell me
whether 50002769514_4001127731_CERTS is there at all, and whether either account's
Account Ref disagrees with the NMI in its own name.
```

Expected, if the 05 Sep extract is right: one row, `50002617992_4204072845_CERTS`, ref 4204072845, opened
7/1/2026, **0 Row** on the relationships grid and no monthly data. That is the "created, not linked" state
and prompt 1's Mogo card picks it up from there. The account I made on 4 Sep, `50002769514_4001127731_CERTS`,
should be absent — it is in neither the 05 Sep extract nor the export taken after the first batches.

---

## 0 · Read-only test

```
On the Envizi tab. Read-only — create, edit, save or delete nothing.
Find 50002617964_NAAA00AC25_CERTS and tell me: its location, account style,
supplier and whether Reader is blank, Opened On, whether it's a virtual account
and the source and percentage, its kWh for Jun/Jul/Aug 2026, and the emission
factor name and value. Then tell me how you found it.
```

Expected: Asphalt Prod - Bathurst (156) · Certificates - Location - kWh · LGC Virtual Account / blank ·
2026-07-01 · source `50002617964_NAAA00AC25` at 100% · **no June**, 53,778, 41,470 · LGCs NSW 24-25 −0.66
(or 25-26 −0.64 once that factor is in and picked up).
