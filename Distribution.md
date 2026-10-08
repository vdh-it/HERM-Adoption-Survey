# Distribution Plan

**Last updated:** 2026-10-08
**Texts:** all invitation and reminder texts are in `Survey_Invitation.md`. This file holds links, process, rules and tracking only.

## 1. Current status

- [+] **Channel attributes** require the LamaPoll Gold licence; the licence is acquired.
- [+] Distribution links are built (syntax: `?Country_<ISO>=1&Distribution_<NAME>=1&main=1`, reminders with `reminder=1` instead of `main=1`).
- [+] First test with data representation was done.
- [+] Survey is open since 2026-10-08.
- [ ] Board endorsement message sent to the national organisations (requested in `Letter to the board.md`).
- [ ] First field-day check of the export (see rule 6).

---

## 2. Commitments made to distribution partners

As promised in `Survey_Invitation.md`; any change here must also be made there.

- Each partner has its own link; it identifies the channel, never the respondent.
- Partners are asked to send the invitation **within two weeks** of our mail (`[SEND-BY DATE]`); members are asked to respond **within three weeks**.
- Reminder text and reminder link are **not** part of the first mail; we send them when a reminder is due.
- The closing date is announced **at least two weeks in advance**; the final reminder goes through all channels and the EUNIS mailing lists.
- Channel-specific results are reported only if **at least 5 institutions** responded through the channel (Analysis Matrix E1).
- Partners can analyse their channel in the published de-identified dataset; no raw data are shared before publication.

**Internal only:** the field phase is planned for about two months. This is not communicated (see `Survey_Invitation.md`, internal note).

---

## 3. Process

| Step | When | What | Owner |
|---|---|---|---|
| 1 | Now | Board endorsement message to national organisations | EUNIS Board |
| 2 | Shortly after step 1 | Invitation (Part 1 and 2 of `Survey_Invitation.md`) with main link and `[SEND-BY DATE]` to each partner | [OWNER] |
| 3 | First field day after each partner mailing | Check export: attribute columns present, channel values match the sent link | [OWNER] |
| 4 | Weekly | Count responses and institutions per channel; update tracking table and contact status (5.1) | [OWNER] |
| 5 | `[SEND-BY DATE]` passed without confirmation | Friendly follow-up to the partner | [OWNER] |
| 6 | About 2–3 weeks after a partner's mailing | Reminder text (Part 3) and reminder link to the partner; priority for channels below 5 institutions | [OWNER] |
| 7 | When participation levels off, at the latest after about 6 weeks | Decide the closing date | EA SIG |
| 8 | At least 2 weeks before closing | Final reminder with closing date via all partners and via EUNIS (`Distribution_EUNIS`, `reminder=1`) | [OWNER], EUNIS |
| 9 | Closing date | Close survey; export; apply Blueprint data rules 12 and 13 | [OWNER] |

## 4. Rules

1. Send each partner only its own link. Never send the reminder link in the first mail.
2. Country parameters `EU` and `XX` are neutral; question 1.2 is authoritative for country analyses.
3. Do not change link syntax once a link has been sent.
4. New channels: copy the template, add the channel to the tracking table, test the link before sending.
5. SIG channels are expected to show selection bias; plan a sensitivity analysis without them.
6. Check the export after the first real responses of each new channel; correct broken links immediately.

---

## 5. Tracking table

"Membership" is taken from `National_Higher_Education_IT_Networks_Europe.md` and is only a rough denominator; replace it with the number the partner reports. "Contact": names and e-mail addresses of contact persons are kept only in `EUNIS_contacts.csv`, which is excluded from Git (`.gitignore`). "in CSV" means a representative is listed there; "not on EUNIS map" means the contact must come from elsewhere.

| Channel | Country | Contact | Membership (inventory) | Invitation sent | Send-by | Partner sent | Reached (reported) | Reminder sent | Institutions |
|---|---|---|---|---|---|---|---|---|---|
| AMUE | FR | in CSV | 178 institutions | | | | | | |
| CINECA | IT | not on EUNIS map | 71 HE institutions | | | | | | |
| CSIESR | FR | in CSV | 145 institutions | | | | | | |
| CSC | FI | in CSV | undefined | | | | | | |
| EUNIS_CZ | CZ | in CSV | undefined | | | | | | |
| EUNIS_SK | SK | in CSV | 20 full + 1 associate | | | | | | |
| GUnet | GR | in CSV | 25 universities | | | | | | |
| Jisc | GB | in CSV | undefined | | | | | | |
| MUCI | PL | in CSV | > 100 institutions | | | | | | |
| LADOK | SE | in CSV | 43 institutions | | | | | | |
| OPI | PL | in CSV | undefined | | | | | | |
| SIGMA | ES | in CSV | 17 universities | | | | | | |
| SURF | NL | in CSV | > 120 institutions | | | | | | |
| UCISA | GB | not on EUNIS map | undefined | | | | | | |
| ZKI | DE | in CSV | > 250 members | | | | | | |
| CIO | DE | in CSV (not on EUNIS map) | 56 individuals | | | | | | |
| HIS | DE | in CSV | 223 members | | | | | | |
| RASH | AL | in CSV | undefined | | | | | | |
| Asiera | IE | in CSV | 9 institutions | | | | | | |
| SRCE | HR | in CSV | undefined | | | | | | |
| VPC | LV | in CSV | 4 founders | | | | | | |
| Sikt | NO | in CSV | undefined | | | | | | |
| Funidata | FI | in CSV | 8 owner organisations | | | | | | |
| HKdir | NO | in CSV | undefined | | | | | | |
| SIG (DE, FI, EU) | — | in CSV | n/a | | | | | | |
| EUNIS | EU | EUNIS secretariat | n/a | | | | | | |

**Added 2026-10-08 from the EUNIS member map:** Funidata (FI) and the Norwegian Directorate for Higher Education and Skills (HKdir, NO). Both are also marked in the network inventory. Test their links before the first mailing (rule 4).

### 5.1 Contact status in `EUNIS_contacts.csv`

The column **"Distribution status"** in `EUNIS_contacts.csv` holds the current lifecycle state of each contact. Any value other than `not relevant` marks a contact as relevant for the study. The tracking table above keeps dates and numbers; the CSV keeps the current state. Update both when a step of section 3 is done.

| Status | Meaning | Set when | Next status |
|---|---|---|---|
| `not relevant` | Default. No direct contact planned: institutions (reached through the EUNIS channel), solution providers, test entries | — | — |
| `contact missing` | Relevant, but no usable address yet | Initial state | `to invite` once an address is known, e.g. from the EUNIS secretariat |
| `to invite` | Relevant, address available, first mail not yet sent | Initial state, or address found | `invited` |
| `invited` | First mail (Part 1 and 2 of `Survey_Invitation.md`) sent | Step 2 | `confirmed`, `declined` or, after `[SEND-BY DATE]`, `follow-up sent` |
| `follow-up sent` | `[SEND-BY DATE]` passed without reaction; friendly follow-up sent | Step 5 | `confirmed`, `declined` or `no response` |
| `confirmed` | Partner agreed to distribute or announced its mailing date | Partner reply | `distributed` |
| `distributed` | Partner has sent the invitation to its members | Partner confirms mailing | `reminder sent` |
| `reminder sent` | Reminder text (Part 3) and reminder link sent to the partner | Step 6 | `final reminder sent` |
| `final reminder sent` | Final reminder with closing date sent through the partner | Step 8 | `closed` |
| `declined` | Partner will not distribute | Partner reply | End state; channel only reached through EUNIS |
| `no response` | No reaction after the follow-up | About one week after `follow-up sent` | End state; channel only reached through EUNIS |
| `closed` | Field phase closed; thank-you mail with pointer to the results sent | Step 9 | — |

Initial state on 2026-10-08: 30 contacts `to invite` (all national channels except CINECA, EUNIS, and the two leads of each SIG channel), 1 contact `contact missing` (CINECA), all other entries `not relevant`. Contacts provided by the project team are marked "provided by project team" in the CSV.

**One status carrier per channel:** if a channel has several contacts, the contact we actually write to carries the status; the others are `not relevant` with a note naming the carrier (CSIESR, SRCE). Exception: the SIG channels, where both co-leads are contacted.

---

## 6. Links

### Main links (first mail)

Known organisations from eunis.org:
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FR=1&Distribution_AMUE=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_IT=1&Distribution_CINECA=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FR=1&Distribution_CSIESR=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_CSC=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_CZ=1&Distribution_EUNIS_CZ=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_SK=1&Distribution_EUNIS_SK=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GR=1&Distribution_GUnet=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GB=1&Distribution_Jisc=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_PL=1&Distribution_MUCI=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_SE=1&Distribution_LADOK=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_PL=1&Distribution_OPI=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_ES=1&Distribution_SIGMA=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NL=1&Distribution_SURF=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GB=1&Distribution_UCISA=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_ZKI=1&main=1

Additional organisations which also are EUNIS members (Funidata and HKdir added 2026-10-08 from the EUNIS member map):
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_CIO=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_HIS=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_AL=1&Distribution_RASH=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_IE=1&Distribution_Asiera=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_HR=1&Distribution_SRCE=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_LV=1&Distribution_VPC=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NO=1&Distribution_Sikt=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_Funidata=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NO=1&Distribution_HKdir=1&main=1

Special Interest Groups (expected selection bias, see rule 5):
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_SIG=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_SIG=1&main=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_EU=1&Distribution_SIG=1&main=1

All EUNIS members:
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_EU=1&Distribution_EUNIS=1&main=1

Template:
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_XX=1&Distribution_XX=1&main=1

### Reminder links (only with Part 3, never in the first mail)

https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FR=1&Distribution_AMUE=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_IT=1&Distribution_CINECA=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FR=1&Distribution_CSIESR=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_CSC=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_CZ=1&Distribution_EUNIS_CZ=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_SK=1&Distribution_EUNIS_SK=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GR=1&Distribution_GUnet=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GB=1&Distribution_Jisc=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_PL=1&Distribution_MUCI=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_SE=1&Distribution_LADOK=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_PL=1&Distribution_OPI=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_ES=1&Distribution_SIGMA=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NL=1&Distribution_SURF=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_GB=1&Distribution_UCISA=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_ZKI=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_CIO=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_HIS=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_AL=1&Distribution_RASH=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_IE=1&Distribution_Asiera=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_HR=1&Distribution_SRCE=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_LV=1&Distribution_VPC=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NO=1&Distribution_Sikt=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_Funidata=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_NO=1&Distribution_HKdir=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_DE=1&Distribution_SIG=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_FI=1&Distribution_SIG=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_EU=1&Distribution_SIG=1&reminder=1
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_EU=1&Distribution_EUNIS=1&reminder=1

Template:
https://survey.lamapoll.de/EA-and-HERM-Adoption?Country_XX=1&Distribution_XX=1&reminder=1

---

## 7. EUNIS member map: summary

**Source:** public member map embedded on https://eunis.org/eunis-members/ (iframe `community.eunis.org/company-map/eunis`), retrieved 2026-10-08 via the map's public endpoints. **118 entries.**

**Contact details are not kept in this file.** The full list with representatives, roles, websites and e-mail addresses is in `EUNIS_contacts.csv` (excluded from Git). Use it only to contact organisations about this survey.

| Type on the map | Entries | Survey channel |
|---|---|---|
| National / sectoral organisations | 21 | their own channel |
| Institutions | 93 | EUNIS |
| Solution providers (SAP, SemaLogic) | 2 | none |
| Other (EUNIS itself, platform test entry) | 2 | none |

**Findings**

- **All 21 national / sectoral organisations on the map** are covered by a channel. Funidata (FI) and the Norwegian Directorate for Higher Education and Skills (NO) were added on 2026-10-08 as a result of this comparison.
- **CINECA, UCISA and Hochschul-CIO are not on the map**, although they have channels. Contacts must come from elsewhere, e.g. the EUNIS Board introduction.
- **SURF's representative on the map is the Board member** to whom `Letter to the board.md` is addressed.
- **Institutions in countries without a national channel** can only be reached through the EUNIS channel: AT 3, BE 5, CH 7, DK 5, EE 1, LU 1, PT 3, RO 1, SI 1. For these countries the EUNIS mailing and its reminders are the only distribution route.
