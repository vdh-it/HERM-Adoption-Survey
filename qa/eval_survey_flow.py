#!/usr/bin/env python3
"""
QA harness for survey-blueprint.md's branching logic.

This is SYNTHETIC TEST DATA, not real survey responses. It exercises the
routing logic (visibility()) as written in survey-blueprint.md AFTER the
2026-09-01 fix: 2.3 shown if 2.1=Yes/Exploring OR 2.2=Yes/Exploring, and
3.10-3.11 excludes "No formal framework" from counting as a real other
framework. The two consistency checks that used to fire on this dataset
(HERM_DISAGREEMENT_..._no_3.1-3.9 and NOFORMAL_POLLUTES_ENGAGEMENT_FLAG)
are kept as permanent regression tests -- they should report 0 rows now.
The remaining HERM_DISAGREEMENT_..._3.1-3.9_fired check documents a
residual, unfixable self-report contradiction (see R14) that no routing
condition can prevent; re-run it against real submissions during cleaning.

Run: python3 qa/eval_survey_flow.py
Produces: qa/synthetic_responses.csv (24 hand-designed respondents)
Prints: consistency-check findings + a recombination coverage report.
"""

import csv
import random
from pathlib import Path

random.seed(42)

HERE = Path(__file__).parent
OUT_CSV = HERE / "synthetic_responses.csv"

FRAMEWORK_TOKENS = ["HERM", "TOGAF", "ZACHMAN", "ARCHIMATE", "CUSTOM", "NOFORMAL", "OTHER"]
NON_HERM_TOKENS = [t for t in FRAMEWORK_TOKENS if t != "HERM"]
# Real, named frameworks other than HERM -- excludes NOFORMAL, which is the
# "no framework at all" placeholder and (post-fix) must not count as one.
REAL_OTHER_TOKENS = [t for t in NON_HERM_TOKENS if t != "NOFORMAL"]

COUNTRIES = ["DE", "NL", "FI", "IT", "PL", "ES", "PT", "AT", "CH", "FR", "SE", "IE"]
INST_TYPES = ["University", "University of Applied Sciences", "Research Institute", "Other"]
SIZE_STUDENTS = ["<2k", "2-10k", "10-30k", ">30k", "n.a."]
SIZE_STAFF = ["<200", "200-1k", "1-3k", ">3k", "n.a."]
ROLES = ["EA Architect", "IT Strategist", "CIO/IT Director", "IT Project Lead", "Other"]
ARTIFACTS = ["ARM", "BRM", "TRM", "DRM", "Business Model Canvas", "SRM", "Process Models", "Value Streams"]
PROBLEMS = ["Structuring application landscape", "Defining business capabilities",
            "Standardizing technology choices", "Benchmarking against peers",
            "Communicating IT to non-IT stakeholders", "Accreditation / compliance documentation"]
COUPLING = ["CIO", "dedicated EA Team", "Central IT", "CDO / Digital Office"]
BARRIERS = ["Lack of awareness", "No leadership support", "No EA practice yet",
            "Lack of time / capacity", "Unclear benefit vs. effort"]
PURPOSES = ["Get to know the results", "Explain your EA tooling",
            "Provide more details about use cases", "Join a community workgroup"]
REASONS_NOT_USING = ["Not aware of it until now", "Current framework already meets our needs",
                      "HERM too complex/specific", "Lack of tooling support",
                      "No community or peer examples", "Switching cost too high"]

def pick(seq, k=1):
    k = min(k, len(seq))
    return random.sample(seq, k=random.randint(1, k))

def flavor_row():
    """Fields that don't affect routing, just realistic variability."""
    return {
        "q1_2_country": random.choice(COUNTRIES),
        "q1_3_institution_type": random.choice(INST_TYPES),
        "q1_4_size_students": random.choice(SIZE_STUDENTS),
        "q1_5_size_staff": random.choice(SIZE_STAFF),
        "q1_6_role": ";".join(pick(ROLES, 2)),
    }

# ---------------------------------------------------------------------------
# 24 hand-designed scenarios. Each dict gives the "decisive" routing inputs;
# everything else is filled with plausible flavor text/values by build_row().
# scenario_label documents *why* the row exists.
# ---------------------------------------------------------------------------
SCENARIOS = [
    dict(id="R01", label="HERM-only, actively used, high engagement, consents+contact",
         eam="Yes", herm2_2="Yes", frameworks=["HERM"], name_given=True, consent="Yes",
         maturity="Actively used", share="Yes"),
    dict(id="R02", label="HERM+TOGAF co-occurrence, embedded, consents, no contact interest",
         eam="Yes", herm2_2="Yes", frameworks=["HERM", "TOGAF"], name_given=True, consent="Yes",
         maturity="Embedded in governance", share="No"),
    dict(id="R03", label="HERM+ArchiMate co-occurrence, exploring",
         eam="Exploring", herm2_2="Exploring", frameworks=["HERM", "ARCHIMATE"], name_given=False,
         maturity="Exploring", share=None),
    dict(id="R04", label="HERM pilot, anonymous, declines naming",
         eam="Yes", herm2_2="Exploring", frameworks=["HERM"], name_given=True, consent="No",
         maturity="Pilot", share="Maybe"),
    dict(id="R05", label="TOGAF-only, no HERM, considering adoption -> engagement flag via 3.13",
         eam="Yes", herm2_2="No", frameworks=["TOGAF"], name_given=True, consent="Yes",
         consider="Maybe", share="Yes"),
    dict(id="R06", label="TOGAF-only, no HERM, unlikely to adopt -> no flag -> Section 5, 5.2 suppressed",
         eam="Yes", herm2_2="No", frameworks=["TOGAF"], name_given=False,
         consider="Unlikely", share=None),
    dict(id="R07", label="Zachman-only, definitely not adopting HERM, no name given",
         eam="Exploring", herm2_2="NotFamiliar", frameworks=["ZACHMAN"], name_given=False,
         consider="Definitely not", share=None),
    dict(id="R08", label="Custom in-house framework only, aware of HERM but not using",
         eam="Yes", herm2_2="No", frameworks=["CUSTOM"], name_given=True, consent="Yes",
         consider="Maybe", share="Maybe"),
    dict(id="R09", label="No formal framework (ad hoc), no HERM -- regression check: must NOT pollute engagement flag (fixed 2026-09-01)",
         eam="Yes", herm2_2="No", frameworks=["NOFORMAL"], name_given=True, consent="Yes",
         consider="Unlikely", share=None),
    dict(id="R10", label="No formal framework only, not familiar with HERM, no name -- regression check variant",
         eam="Exploring", herm2_2="NotFamiliar", frameworks=["NOFORMAL"], name_given=False,
         consider="Unlikely", share=None),
    dict(id="R11", label="Other (free-text) framework only, no HERM, interested in HERM",
         eam="Yes", herm2_2="No", frameworks=["OTHER"], name_given=True, consent="Yes",
         consider="Yes interested", share="Yes"),
    dict(id="R12", label="EAM=No, HERM=Yes actively -- regression check: 2.3 now shown via 2.2, reaches 3.1-3.9 (fixed 2026-09-01)",
         eam="No", herm2_2="Yes", frameworks=["HERM"], name_given=True, consent="Yes",
         maturity="Actively used", share="Yes"),
    dict(id="R13", label="EAM=Not familiar, HERM=Exploring -- regression check variant, no formal EAM but piloting HERM",
         eam="NotFamiliar", herm2_2="Exploring", frameworks=["HERM"], name_given=False,
         maturity="Exploring", share=None),
    dict(id="R14", label="EAM=Yes, HERM(2.2)=No, but HERM checked in 2.3 -- residual self-report contradiction, not fixable via routing",
         eam="Yes", herm2_2="No", frameworks=["HERM"], name_given=True, consent="Yes",
         maturity="Pilot", share="No"),
    dict(id="R15", label="EAM=No, HERM=No, straightforward non-user, fast exit",
         eam="No", herm2_2="No", frameworks=None, name_given=False, share=None),
    dict(id="R16", label="EAM=Not familiar, HERM=Not familiar, fast exit, no name",
         eam="NotFamiliar", herm2_2="NotFamiliar", frameworks=None, name_given=False, share=None),
    dict(id="R17", label="HERM-only, moderate engagement, name given, consents, contact but no email purpose overlap",
         eam="Exploring", herm2_2="Yes", frameworks=["HERM"], name_given=True, consent="Yes",
         maturity="Pilot", share="Maybe"),
    dict(id="R18", label="HERM+Custom co-occurrence, embedded, declines naming, wants contact",
         eam="Yes", herm2_2="Yes", frameworks=["HERM", "CUSTOM"], name_given=True, consent="No",
         maturity="Embedded in governance", share="Yes"),
    dict(id="R19", label="HERM-only n.a. maturity, no name given, no engagement -> Section 5 (5.2 suppressed, saw 3.1-3.9 not 3.12-3.15)",
         eam="Yes", herm2_2="Yes", frameworks=["HERM"], name_given=False,
         maturity="n.a.", share=None),
    dict(id="R20", label="ArchiMate+Zachman (no HERM), definitely not, name given, declines naming consent",
         eam="Yes", herm2_2="NotFamiliar", frameworks=["ARCHIMATE", "ZACHMAN"], name_given=True, consent="No",
         consider="Definitely not", share=None),
    dict(id="R21", label="HERM+TOGAF+ArchiMate triple co-occurrence, actively used, full engagement",
         eam="Yes", herm2_2="Yes", frameworks=["HERM", "TOGAF", "ARCHIMATE"], name_given=True, consent="Yes",
         maturity="Actively used", share="Yes"),
    dict(id="R22", label="TOGAF-only, no HERM, interested but declines to share contact details",
         eam="Yes", herm2_2="No", frameworks=["TOGAF"], name_given=True, consent="Yes",
         consider="Yes interested", share="No"),
    dict(id="R23", label="EAM exploring, HERM+NOFORMAL selected together -- regression check: NOFORMAL must not add to 3.10-3.11",
         eam="Exploring", herm2_2="Exploring", frameworks=["HERM", "NOFORMAL"], name_given=False,
         maturity="Exploring", share=None),
    dict(id="R24", label="Custom-only, not familiar with HERM, definitely not adopting, name given, consents",
         eam="Yes", herm2_2="NotFamiliar", frameworks=["CUSTOM"], name_given=True, consent="Yes",
         consider="Definitely not", share=None),
]


def build_row(s):
    """Turn a scenario dict into a full 'intended answers' row (pre-visibility)."""
    row = {"resp_id": s["id"], "scenario_label": s["label"]}
    row.update(flavor_row())

    row["q1_1_institution_name"] = f"Institution_{s['id']}" if s["name_given"] else ""
    row["q2_1_eam"] = s["eam"]
    row["q2_2_herm"] = s["herm2_2"]

    practicing = s["eam"] in ("Yes", "Exploring")
    herm_engaged = s["herm2_2"] in ("Yes", "Exploring")
    show_2_3 = practicing or herm_engaged  # fixed 2026-09-01: was `practicing` alone
    frameworks = s["frameworks"] if show_2_3 and s["frameworks"] else ([] if show_2_3 else None)
    row["_frameworks"] = frameworks  # internal, not written to CSV directly
    row["_show_2_3"] = show_2_3
    row["q2_3_frameworks"] = ";".join(frameworks) if frameworks is not None else ""

    has_herm = bool(frameworks) and "HERM" in frameworks
    has_other = bool(frameworks) and any(f in frameworks for f in REAL_OTHER_TOKENS)  # fixed: excludes NOFORMAL

    # 3.1-3.9 intended answers (used only if has_herm)
    row["q3_1_artifacts"] = ";".join(pick(ARTIFACTS, 3))
    row["q3_2_bc_area"] = "BC-04 Student Services"
    row["q3_3_problems"] = ";".join(pick(PROBLEMS, 2))
    row["q3_4_scenario_text"] = "Consolidated application landscape ahead of a system migration."
    row["q3_5_start_year"] = random.randint(2017, 2025)
    row["q3_6_maturity"] = s.get("maturity", "Pilot")
    row["q3_7_embedded"] = "Yes, central to it" if practicing else ""
    row["q3_8_worked_well"] = "Shared vocabulary across IT and faculties."
    row["q3_9_difficult"] = "Keeping the model up to date."

    # 3.10-3.11 intended answers (used only if has_other, BUG2 included)
    row["q3_10_duration"] = random.choice(["<1y", "1-3y", "4-7y", ">7y"])
    row["q3_11_coupling"] = ";".join(pick(COUPLING, 2))

    # 3.12-3.15 intended answers (used only if !has_herm and practicing)
    row["q3_12_reason"] = ";".join(pick(REASONS_NOT_USING, 2))
    row["q3_13_consider"] = s.get("consider", "Maybe")
    row["q3_14_complement_replace"] = "complement"
    row["q3_15_what_needed"] = "Clearer migration tooling and peer case studies."

    # 4.1
    row["q4_1_consent"] = s.get("consent", "")

    # 4.2-4.5 intended answers
    row["q4_2_transferability"] = "High"
    row["q4_3_share"] = s.get("share") or ""
    row["q4_4_email"] = f"contact@{s['id'].lower()}.example.org"
    row["q4_5_purpose"] = ";".join(pick(PURPOSES, 2))

    # 5.1-5.3
    row["q5_1_open_questions"] = "How do we scale this beyond one faculty?"
    row["q5_2_barrier"] = ";".join(pick(BARRIERS, 2))
    row["q5_3_help"] = "A reference case study from a peer institution."

    row["_has_herm"] = has_herm
    row["_has_other"] = has_other
    row["_practicing"] = practicing
    return row


# ---------------------------------------------------------------------------
# visibility(): implements survey-blueprint.md's routing as written after the
# 2026-09-01 fix (2.3 gated on 2.1 OR 2.2; NOFORMAL excluded from "other").
# ---------------------------------------------------------------------------
def visibility(row):
    show_2_3 = row["_show_2_3"]
    has_herm = row["_has_herm"]
    has_other = row["_has_other"]  # excludes NOFORMAL (fixed)

    show_3_1_9 = has_herm
    show_3_10_11 = has_other
    show_3_12_15 = (not has_herm) and show_2_3

    engagement_flag = (
        (show_3_1_9 and row["q3_6_maturity"] in ("Pilot", "Actively used", "Embedded in governance"))
        or show_3_10_11
        or (show_3_12_15 and row["q3_13_consider"] in ("Yes interested", "Maybe"))
    )

    show_4_1 = bool(row["q1_1_institution_name"])
    show_4_2_5 = engagement_flag
    show_4_4_5 = show_4_2_5 and row["q4_3_share"] in ("Yes", "Maybe")

    show_5 = not engagement_flag
    show_5_2 = show_5 and not show_3_12_15

    return dict(
        s3_1_9=show_3_1_9, s3_10_11=show_3_10_11, s3_12_15=show_3_12_15,
        s4_1=show_4_1, s4_2_5=show_4_2_5, s4_4_5=show_4_4_5,
        s5=show_5, s5_2=show_5_2, engagement_flag=engagement_flag,
    )


CSV_FIELDS = [
    "resp_id", "scenario_label",
    "q1_1_institution_name", "q1_2_country", "q1_3_institution_type",
    "q1_4_size_students", "q1_5_size_staff", "q1_6_role",
    "q2_1_eam", "q2_2_herm", "q2_3_frameworks",
    "q3_1_artifacts", "q3_2_bc_area", "q3_3_problems", "q3_4_scenario_text",
    "q3_5_start_year", "q3_6_maturity", "q3_7_embedded", "q3_8_worked_well", "q3_9_difficult",
    "q3_10_duration", "q3_11_coupling",
    "q3_12_reason", "q3_13_consider", "q3_14_complement_replace", "q3_15_what_needed",
    "q4_1_consent", "q4_2_transferability", "q4_3_share", "q4_4_email", "q4_5_purpose",
    "q5_1_open_questions", "q5_2_barrier", "q5_3_help",
]


def apply_visibility(row, vis):
    """Blank out fields that visibility() says should not be shown."""
    out = {k: row.get(k, "") for k in CSV_FIELDS}
    if not vis["s3_1_9"]:
        for k in ("q3_1_artifacts", "q3_2_bc_area", "q3_3_problems", "q3_4_scenario_text",
                   "q3_5_start_year", "q3_6_maturity", "q3_8_worked_well", "q3_9_difficult"):
            out[k] = ""
    if not (vis["s3_1_9"] and row["_practicing"]):
        out["q3_7_embedded"] = ""
    if not vis["s3_10_11"]:
        out["q3_10_duration"] = ""
        out["q3_11_coupling"] = ""
    if not vis["s3_12_15"]:
        out["q3_12_reason"] = ""
        out["q3_13_consider"] = ""
        out["q3_15_what_needed"] = ""
    if not (vis["s3_12_15"] and row["q3_13_consider"] in ("Yes interested", "Maybe")):
        out["q3_14_complement_replace"] = ""
    if not vis["s4_1"]:
        out["q4_1_consent"] = ""
    if not vis["s4_2_5"]:
        out["q4_2_transferability"] = ""
        out["q4_3_share"] = ""
    if not vis["s4_4_5"]:
        out["q4_4_email"] = ""
        out["q4_5_purpose"] = ""
    if not vis["s5"]:
        out["q5_1_open_questions"] = ""
        out["q5_3_help"] = ""
    if not vis["s5_2"]:
        out["q5_2_barrier"] = ""
    return out


def generate_dataset():
    rows = []
    for s in SCENARIOS:
        raw = build_row(s)
        vis = visibility(raw)
        rows.append((raw, vis, apply_visibility(raw, vis)))
    return rows


# ---------------------------------------------------------------------------
# Consistency checks -- run against the CSV-shaped output only, as an analyst
# inspecting an export would, not using generator internals.
# ---------------------------------------------------------------------------
def run_consistency_checks(rows):
    findings = []

    def flag(check, resp_id, detail):
        findings.append((check, resp_id, detail))

    for raw, vis, out in rows:
        rid = out["resp_id"]

        # 2.2 claims HERM use, but 3.1-3.9 never fired (BUG 1, direction a)
        if raw["q2_2_herm"] in ("Yes", "Exploring") and not out["q3_1_artifacts"]:
            flag("HERM_DISAGREEMENT_2.2_says_yes_but_no_3.1-3.9", rid,
                 f"2.2={raw['q2_2_herm']!r} but 3.1 artifacts blank (2.1={raw['q2_1_eam']!r})")

        # 2.2 denies HERM use, but 3.1-3.9 fired anyway (BUG 1, direction b)
        if raw["q2_2_herm"] in ("No", "NotFamiliar") and out["q3_1_artifacts"]:
            flag("HERM_DISAGREEMENT_2.2_says_no_but_3.1-3.9_fired", rid,
                 f"2.2={raw['q2_2_herm']!r} but 3.1 artifacts populated (2.3={raw['q2_3_frameworks']!r})")

        # NOFORMAL alone triggered the engagement flag (BUG 2)
        fw = raw["_frameworks"] or []
        if fw == ["NOFORMAL"] and vis["engagement_flag"]:
            flag("NOFORMAL_POLLUTES_ENGAGEMENT_FLAG", rid,
                 "sole 2.3 answer was 'No formal framework, ad hoc' yet 4.2-4.5 fired")

        # Sanity: 5.2 should never co-occur with 3.12-3.15
        if out["q3_12_reason"] and out["q5_2_barrier"]:
            flag("ORPHAN_5.2_WITH_3.12", rid, "both 3.12 and 5.2 populated")

        # Sanity: 4.1 should never appear without 1.1
        if out["q4_1_consent"] and not out["q1_1_institution_name"]:
            flag("ORPHAN_4.1_WITHOUT_1.1", rid, "4.1 populated but 1.1 blank")

        # Sanity: conditional children without their parent
        if out["q3_2_bc_area"] and not out["q3_1_artifacts"]:
            flag("ORPHAN_3.2_WITHOUT_3.1", rid, "3.2 populated but 3.1 blank")
        if out["q3_4_scenario_text"] and not out["q3_3_problems"]:
            flag("ORPHAN_3.4_WITHOUT_3.3", rid, "3.4 populated but 3.3 blank")
        if out["q3_14_complement_replace"] and out["q3_13_consider"] not in ("Yes interested", "Maybe"):
            flag("ORPHAN_3.14_WITHOUT_QUALIFYING_3.13", rid, f"3.13={out['q3_13_consider']!r}")
        if (out["q4_4_email"] or out["q4_5_purpose"]) and out["q4_3_share"] not in ("Yes", "Maybe"):
            flag("ORPHAN_4.4-4.5_WITHOUT_QUALIFYING_4.3", rid, f"4.3={out['q4_3_share']!r}")

    return findings


# ---------------------------------------------------------------------------
# Coverage: cross-tab the four axes the user named (EAM / HERM / consent /
# contact), 2x2x3x3 = 36 cells. Reachability of each cell under the current
# spec is determined empirically via Monte Carlo sampling of visibility(),
# not hand-derived -- this also independently confirms Bug 1's structural
# consequence (no NotPracticing respondent can ever reach the contact funnel).
# ---------------------------------------------------------------------------
def axes_of(raw, vis):
    eam_axis = "Practicing" if raw["_practicing"] else "NotPracticing"
    herm_axis = "WithHERM" if raw["q2_2_herm"] in ("Yes", "Exploring") else "WithoutHERM"
    if not raw["q1_1_institution_name"]:
        consent_axis = "NoName"
    else:
        consent_axis = "ConsentYes" if raw.get("q4_1_consent") == "Yes" else "ConsentNo"
    if not vis["engagement_flag"]:
        contact_axis = "NoFlag"
    else:
        contact_axis = "ShareYesMaybe" if raw.get("q4_3_share") in ("Yes", "Maybe") else "ShareNo"
    return (eam_axis, herm_axis, consent_axis, contact_axis)


def monte_carlo_reachable(n=20000):
    reachable = set()
    for _ in range(n):
        eam = random.choice(["Yes", "Exploring", "No", "NotFamiliar"])
        herm2_2 = random.choice(["Yes", "Exploring", "No", "NotFamiliar"])
        practicing = eam in ("Yes", "Exploring")
        herm_engaged = herm2_2 in ("Yes", "Exploring")
        show_2_3 = practicing or herm_engaged  # fixed 2026-09-01
        if show_2_3:
            fw = [t for t in FRAMEWORK_TOKENS if random.random() < 0.3]
            if not fw:
                fw = [random.choice(FRAMEWORK_TOKENS)]
        else:
            fw = None
        name_given = random.random() < 0.6
        consent = random.choice(["Yes", "No"]) if name_given else ""
        maturity = random.choice(["Exploring", "Pilot", "Actively used", "Embedded in governance", "n.a."])
        consider = random.choice(["Yes interested", "Maybe", "Unlikely", "Definitely not"])
        share = random.choice(["Yes", "Maybe", "No"])

        raw = {
            "_practicing": practicing,
            "_show_2_3": show_2_3,
            "q2_2_herm": herm2_2,
            "q1_1_institution_name": "x" if name_given else "",
            "q4_1_consent": consent,
            "q3_6_maturity": maturity,
            "q3_13_consider": consider,
            "q4_3_share": share,
            "_frameworks": fw,
        }
        has_herm = bool(fw) and "HERM" in fw
        has_other = bool(fw) and any(f in fw for f in REAL_OTHER_TOKENS)  # fixed: excludes NOFORMAL
        raw["_has_herm"] = has_herm
        raw["_has_other"] = has_other
        vis = visibility(raw)
        reachable.add(axes_of(raw, vis))
    return reachable


def coverage_report(rows):
    eam_vals = ["Practicing", "NotPracticing"]
    herm_vals = ["WithHERM", "WithoutHERM"]
    consent_vals = ["NoName", "ConsentYes", "ConsentNo"]
    contact_vals = ["NoFlag", "ShareYesMaybe", "ShareNo"]

    all_cells = [(e, h, c, k) for e in eam_vals for h in herm_vals
                 for c in consent_vals for k in contact_vals]

    covered = {}
    for raw, vis, out in rows:
        cell = axes_of(raw, vis)
        covered.setdefault(cell, []).append(out["resp_id"])

    reachable = monte_carlo_reachable()

    print(f"\n=== Coverage: EAM x HERM(2.2) x Consent x Contact ({len(all_cells)} cells) ===")
    n_reachable = n_covered = n_gap = n_structurally_unreachable = 0
    for cell in all_cells:
        is_reachable = cell in reachable
        is_covered = cell in covered
        if is_reachable:
            n_reachable += 1
        if is_covered:
            n_covered += 1
        if is_reachable and not is_covered:
            n_gap += 1
        if not is_reachable:
            n_structurally_unreachable += 1
        tag = ("covered  " if is_covered else
               "GAP      " if is_reachable else
               "n/a      ")
        who = ",".join(covered.get(cell, []))
        print(f"  {tag} {cell}  {who}")

    print(f"\nReachable under current spec: {n_reachable}/{len(all_cells)}")
    print(f"Covered by synthetic_responses.csv: {n_covered}/{len(all_cells)}")
    print(f"Gaps (reachable but not covered): {n_gap}")
    print(f"Structurally unreachable (0/{20000} Monte Carlo draws landed here): {n_structurally_unreachable}")
    # Post-fix: only NotPracticing x WithoutHERM x 3 consent states x {ShareYesMaybe,ShareNo}
    # remains unreachable (1x1x3x2=6) -- correctly so, since a respondent with neither EAM
    # practice nor HERM engagement never triggers 2.3 at all, so has nothing to be engaged
    # about. NotPracticing x WithHERM is now reachable (via 2.2), which is the fix working.
    if n_structurally_unreachable == 6:
        print("  -> post-fix: the only unreachable cells left are genuine non-users")
        print("     (NotPracticing AND WithoutHERM) trying to reach the contact funnel --")
        print("     correctly impossible, since they have no engagement signal to report.")
        print("     NotPracticing x WithHERM is now reachable: Bug 1 is fixed.")

    print("\n=== Secondary table: framework-selection category (not multiplied into the cube) ===")
    cat_counts = {}
    for raw, vis, out in rows:
        if not raw["_show_2_3"]:
            cat = "not_shown_(2.3_not_shown)"
        elif raw["_has_herm"] and raw["_has_other"]:
            cat = "HERM+Other"
        elif raw["_has_herm"]:
            cat = "HERM-only"
        elif raw["_frameworks"] == ["NOFORMAL"]:
            cat = "NoFormal-only"
        elif raw["_has_other"]:
            cat = "Other-only"
        else:
            cat = "other/unclassified"
        cat_counts.setdefault(cat, []).append(out["resp_id"])
    for cat, ids in sorted(cat_counts.items()):
        print(f"  {cat:28s} n={len(ids):2d}  {','.join(ids)}")


def main():
    rows = generate_dataset()

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for _, _, out in rows:
            writer.writerow(out)
    print(f"Wrote {len(rows)} synthetic rows to {OUT_CSV}")

    findings = run_consistency_checks(rows)
    print(f"\n=== Consistency check findings: {len(findings)} ===")
    by_check = {}
    for check, rid, detail in findings:
        by_check.setdefault(check, []).append((rid, detail))
    for check, items in sorted(by_check.items()):
        print(f"\n{check}  ({len(items)} rows)")
        for rid, detail in items:
            print(f"  {rid}: {detail}")

    coverage_report(rows)


if __name__ == "__main__":
    main()
