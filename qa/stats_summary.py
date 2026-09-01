#!/usr/bin/env python3
"""
Lightweight descriptive-stats pass over a survey export shaped like
qa/synthetic_responses.csv (resp_id + q1_1..q6_3 columns, multi-select
fields ';'-joined, blank = not shown/not answered).

This is NOT a validity check -- that's qa/eval_survey_flow.py's job
(routing consistency, reachability). This script answers a different
question: "if we ran this on real data, does the shape of the output
look like something we could report from?" It exercises Goal 1 ("map
who is using HERM and which artifacts, and for what problems") end to
end as frequency tables, and gives skip/completion rates per question
so a short instrument's actual burden is visible, not just assumed.

Deliberately stdlib-only (csv + collections.Counter) so it runs
against a real anonymised export with zero new dependencies -- point
it at any CSV with the same column names:

    python3 qa/stats_summary.py [path/to/export.csv]

Default: qa/synthetic_responses.csv (synthetic test data).
"""

import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_CSV = HERE / "synthetic_responses.csv"

MULTI_SELECT_FIELDS = [
    "q2_3_frameworks", "q2_5_coupling", "q3_1_artifacts", "q3_3_problems",
    "q4_1_reason", "q5_5_purpose", "q6_2_barrier",
]
FREETEXT_FIELDS = [
    "q1_1_institution_name", "q3_2_bc_area", "q3_4_scenario_text",
    "q3_8_worked_well", "q3_9_difficult", "q4_4_what_needed",
    "q5_4_email", "q6_1_open_questions", "q6_3_help",
]


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct(n, total):
    return f"{100 * n / total:5.1f}%" if total else "  n/a"


def section_reach(rows):
    n = len(rows)
    reach = {
        "Section 3 (HERM Usage Details)": sum(1 for r in rows if r["q3_1_artifacts"]),
        "Section 4 (Why not (yet) HERM?)": sum(1 for r in rows if r["q4_1_reason"]),
        "Section 5.2-5.5 (follow-up contact funnel)": sum(1 for r in rows if r["q5_2_transferability"]),
        "  of which: agreed to share (5.3 Yes/Maybe)": sum(1 for r in rows if r["q5_3_share"] in ("Yes", "Maybe")),
        "  of which: gave an email (5.4)": sum(1 for r in rows if r["q5_4_email"]),
        "Section 6 (Open Questions & Barriers)": sum(1 for r in rows if r["q6_1_open_questions"]),
        "5.1 naming consent asked (had 1.1)": sum(1 for r in rows if r["q5_1_consent"]),
        "  of which: consented to naming": sum(1 for r in rows if r["q5_1_consent"] == "Yes"),
    }
    print(f"\n=== Section reach (N={n}) ===")
    for label, count in reach.items():
        print(f"  {count:3d} ({pct(count, n)})  {label}")


def value_counts(rows, field, title=None):
    counts = Counter(r[field] for r in rows if r[field])
    n_answered = sum(counts.values())
    print(f"\n--- {title or field} (answered: {n_answered}/{len(rows)}) ---")
    for value, count in counts.most_common():
        print(f"  {count:3d} ({pct(count, n_answered)})  {value}")


def multi_select_counts(rows, field, title=None):
    """Frequency of individual tokens across a ';'-joined multi-select field."""
    counter = Counter()
    n_respondents = 0
    for r in rows:
        if not r[field]:
            continue
        n_respondents += 1
        for token in r[field].split(";"):
            counter[token] += 1
    print(f"\n--- {title or field} (respondents: {n_respondents}, multi-select so % can exceed 100) ---")
    for value, count in counter.most_common():
        print(f"  {count:3d} ({pct(count, n_respondents)})  {value}")


def completion_rates(rows):
    print(f"\n=== Free-text field completion (share of respondents who SAW the field and filled it) ===")
    # denominator per field: rows where the field's group was shown at all --
    # approximate via a sibling required field in the same group being non-empty.
    denom = {
        "q1_1_institution_name": len(rows),  # always shown (optional)
        "q3_2_bc_area": sum(1 for r in rows if r["q3_1_artifacts"]),
        "q3_4_scenario_text": sum(1 for r in rows if r["q3_3_problems"]),
        "q3_8_worked_well": sum(1 for r in rows if r["q3_1_artifacts"]),
        "q3_9_difficult": sum(1 for r in rows if r["q3_1_artifacts"]),
        "q4_4_what_needed": sum(1 for r in rows if r["q4_1_reason"]),
        "q5_4_email": sum(1 for r in rows if r["q5_3_share"] in ("Yes", "Maybe")),
        "q6_1_open_questions": sum(1 for r in rows if not r["q5_2_transferability"]),
        "q6_3_help": sum(1 for r in rows if not r["q5_2_transferability"]),
    }
    for field in FREETEXT_FIELDS:
        d = denom.get(field, len(rows))
        n = sum(1 for r in rows if r[field])
        print(f"  {n:3d}/{d:<3d} ({pct(n, d)})  {field}")


def numeric_summary(rows, field, title=None):
    values = [int(r[field]) for r in rows if r[field]]
    if not values:
        print(f"\n--- {title or field}: no answers ---")
        return
    print(f"\n--- {title or field} (n={len(values)}) ---")
    print(f"  min={min(values)}  max={max(values)}  mean={sum(values)/len(values):.1f}")


def main():
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CSV
    rows = load_rows(csv_path)
    print(f"Loaded {len(rows)} rows from {csv_path}")

    section_reach(rows)

    print("\n=== Screener (Section 2) ===")
    value_counts(rows, "q2_1_eam", "2.1 Practice EAM?")
    value_counts(rows, "q2_2_herm", "2.2 Use HERM?")
    multi_select_counts(rows, "q2_3_frameworks", "2.3 Frameworks in use")
    value_counts(rows, "q2_4_duration", "2.4 Duration")
    multi_select_counts(rows, "q2_5_coupling", "2.5 EAM coupling")

    print("\n=== Goal 1: HERM usage (Section 3, HERM users only) ===")
    multi_select_counts(rows, "q3_1_artifacts", "3.1 HERM artifacts used")
    multi_select_counts(rows, "q3_3_problems", "3.3 Problems solved with HERM")
    value_counts(rows, "q3_6_maturity", "3.6 HERM adoption maturity")
    numeric_summary(rows, "q3_5_start_year", "3.5 HERM start year")

    print("\n=== Section 4: why not (yet) HERM ===")
    multi_select_counts(rows, "q4_1_reason", "4.1 Reasons for not using HERM")
    value_counts(rows, "q4_2_consider", "4.2 Would consider adopting HERM")

    print("\n=== Section 6: barriers (non-engaged respondents only) ===")
    multi_select_counts(rows, "q6_2_barrier", "6.2 Main barrier to adopting HERM")

    completion_rates(rows)


if __name__ == "__main__":
    main()
