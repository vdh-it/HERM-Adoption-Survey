#!/usr/bin/env python3
"""
Completion-time statistics per questionnaire path, as Markdown tables.

Answers the field-phase question "how long does the survey really take?"
for the paths defined in Blueprint.md section 3 (Question Flow):

- institutions without EA practice (2.1 = No EA practice / Don't know),
- the long path (EA operational and HERM evaluated/piloted/used, so
  2.2-2.6 and the whole of Section 4 are shown),
- previews, break-offs and people who leave right after the consent page.

Works on the raw LamaPoll export ("Rohdaten ... .csv" with readable
column headers, as delivered in data/). Columns are found by question
text, not by LamaPoll question number, so renumbering does not break it.

Outlier rule (extreme pauses): respondents often leave the survey open
while doing other work. A page shown longer than --extreme-page seconds
(default 1800 = 30 min) is an extreme pause. Responses with at least one
extreme pause are excluded from the time statistics; their answers stay
in the dataset, only their duration is not interpretable. Pages longer
than LONG_PAGE seconds are counted as a warning but kept.
Duration = sum of the per-page durations (LamaPoll "Dauer für Seite").

Only aggregates are printed; no individual responses (AGENTS.md rule 2).
Groups with fewer than MIN_N usable responses show counts only.

    python3 qa/duration_stats.py [export.csv] [--extreme-page 1800]

Default: the newest raw export in data/.
"""

import argparse
import csv
import statistics
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
DATA_DIR = HERE.parent / "data"
MIN_N = 3
LONG_PAGE = 600  # seconds; flagged, not excluded
BOUNCE_RATE = 5.0  # answer rate in % below which a break-off only passed the consent page

COL_PROCEED = "How would you like to proceed?"
COL_EA = "Current status of Enterprise Architecture at your institution"
COL_HERM = "Institutional HERM adoption status"
COL_TOTAL = "Beantwortungsdauer (in s)"
COL_DONE = "abgeschlossen"
COL_RATE = "Antwort-Quote"
PAGE_PREFIX = "Dauer für Seite"

EA_NONE = {"No EA practice", "Don't know / Cannot assess"}
EA_EXPLORING = {"Exploring or planning EA"}
EA_OPERATIONAL = {"Established operational practice",
                  "Early operational practice / currently being established"}
HERM_EVAL_PILOT = {"Being evaluated / considered", "Pilot or experimental use"}
HERM_ACTIVE = {"Active operational use",
               "Embedded in governance or standard EA processes"}
HERM_SECTION4 = HERM_EVAL_PILOT | HERM_ACTIVE


def norm(text):
    """Option labels as compared: LamaPoll drops commas in exported answer texts."""
    return " ".join((text or "").replace(",", "").split()).casefold()


EA_NONE, EA_EXPLORING, EA_OPERATIONAL, HERM_EVAL_PILOT, HERM_ACTIVE, HERM_SECTION4 = (
    {norm(o) for o in s} for s in
    (EA_NONE, EA_EXPLORING, EA_OPERATIONAL, HERM_EVAL_PILOT, HERM_ACTIVE, HERM_SECTION4))


def find_latest_export(data_dir):
    """Newest raw export (by mtime) with readable headers."""
    candidates = sorted(data_dir.glob("*Rohdaten*.csv"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    for path in candidates:
        if COL_TOTAL in read_header(path):
            return path
    sys.exit(f"No raw export with column '{COL_TOTAL}' in {data_dir}")


def sniff(sample):
    return csv.Sniffer().sniff(sample, delimiters=",;\t")


def read_header(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(20000)
    return next(csv.reader([sample.splitlines()[0]], sniff(sample)))


def load_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        dialect = sniff(f.read(20000))
        f.seek(0)
        return list(csv.DictReader(f, dialect=dialect))


def column(rows, text):
    """Name of the column whose header contains the question text."""
    for name in rows[0]:
        if name.endswith(" - " + text) or name == text:
            return name
    sys.exit(f"Column not found: {text}")


def number(value):
    value = (value or "").strip().replace("%", "").replace(",", ".")
    return float(value) if value else 0.0


def minutes(seconds):
    return f"{seconds / 60:.1f}"


class Timing:
    def __init__(self, pages, extreme):
        self.pages = pages
        self.extreme = extreme

    def durations(self, row):
        return [number(row[p]) for p in self.pages]

    def is_extreme(self, row):
        return any(d > self.extreme for d in self.durations(row))

    def has_long_page(self, row):
        return any(d > LONG_PAGE for d in self.durations(row))

    def stats_row(self, label, rows):
        usable = [r for r in rows if not self.is_extreme(r)]
        excluded = len(rows) - len(usable)
        long_pages = sum(self.has_long_page(r) for r in usable)
        head = f"| {label} | {len(rows)} | {excluded} | {len(usable)} |"
        if len(usable) < MIN_N:
            return f"{head} – | – | {long_pages} |"
        q1, med, q3 = statistics.quantiles(sorted(sum(self.durations(r)) for r in usable),
                                           n=4, method="inclusive")
        return f"{head} {minutes(med)} | {minutes(q1)}–{minutes(q3)} | {long_pages} |"

    def last_page(self, row):
        visited = [i + 1 for i, d in enumerate(self.durations(row)) if d > 0]
        return visited[-1] if visited else 0


def channel_of(row):
    return next((v.removeprefix("Distribution_") for k, v in row.items()
                 if k.startswith("Attribut") and (v or "").startswith("Distribution_")), "(none)")


def build_report(path, extreme):
    rows = load_rows(path)
    timing = Timing([c for c in rows[0] if c.startswith(PAGE_PREFIX)], extreme)
    proceed, ea_col, herm_col = (column(rows, t) for t in (COL_PROCEED, COL_EA, COL_HERM))
    for r in rows:
        r["_ea"], r["_herm"] = norm(r[ea_col]), norm(r[herm_col])
    ea, herm = "_ea", "_herm"

    participants = [r for r in rows if r[proceed].startswith("Participate")]
    previews = [r for r in rows if r[proceed].startswith("Preview")]
    leavers = [r for r in rows if r[proceed].startswith("Leave")]
    done = [r for r in participants if r[COL_DONE] == "1"]
    broken = [r for r in participants if r[COL_DONE] != "1"]

    groups = [
        ("All completed", done),
        ("No EA practice / don't know (2.1)", [r for r in done if r[ea] in EA_NONE]),
        ("Exploring or planning EA (2.1)", [r for r in done if r[ea] in EA_EXPLORING]),
        ("EA operational: early or established (2.1)", [r for r in done if r[ea] in EA_OPERATIONAL]),
        ("HERM not in use, Section 5 path (3.2)", [r for r in done if r[herm] not in HERM_SECTION4]),
        ("HERM evaluated or piloted, Section 4 + 5.1/5.2 (3.2)", [r for r in done if r[herm] in HERM_EVAL_PILOT]),
        ("HERM active or embedded, Section 4 (3.2)", [r for r in done if r[herm] in HERM_ACTIVE]),
        ("**Heavy users:** EA operational and HERM Section 4",
         [r for r in done if r[ea] in EA_OPERATIONAL and r[herm] in HERM_SECTION4]),
        ("**Short path:** no EA practice and HERM not in use",
         [r for r in done if r[ea] in EA_NONE and r[herm] not in HERM_SECTION4]),
        ("Break-off (participants, not completed)", broken),
        (f"  of which left after consent (answer rate < {BOUNCE_RATE:g} %)",
         [r for r in broken if number(r[COL_RATE]) < BOUNCE_RATE]),
        ("**Preview** (0.1), all", previews),
        ("  Preview clicked through to the end", [r for r in previews if r[COL_DONE] == "1"]),
        ("  Preview stopped early", [r for r in previews if r[COL_DONE] != "1"]),
        ("Leave (0.1)", leavers),
    ]

    out = [
        "## Completion time by questionnaire path",
        "",
        f"Source: `{path.name}` · {len(rows)} rows · {len(participants)} participants "
        f"({len(done)} completed), {len(previews)} previews, {len(leavers)} leave.",
        "",
        f"Duration = sum of page durations. **Excluded** = at least one page longer than "
        f"{extreme / 60:g} min (extreme pause, survey left open). **Long page** = a page longer than "
        f"{LONG_PAGE / 60:g} min among the used responses (kept). "
        f"Groups with fewer than {MIN_N} used responses show counts only.",
        "",
        "| Group | n | Excluded | Used | Median (min) | IQR (min) | Long page |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    out += [timing.stats_row(label, group) for label, group in groups]

    if not previews and not leavers:
        out += ["", "Note: the export contains no Preview or Leave responses; "
                    "it is probably filtered to participants. Export all respondents to measure them."]

    stops = Counter(timing.last_page(r) for r in broken)
    if stops:
        out += ["", "### Break-offs by last page visited (participants)", "",
                "| Last page | n |", "| ---: | ---: |"]
        out += [f"| {page} | {n} |" for page, n in sorted(stops.items())]

    kinds = {"Completed": done, "Not completed": broken, "Preview": previews}
    counts = {kind: Counter(channel_of(r) for r in group) for kind, group in kinds.items()}
    names = sorted(set().union(*counts.values()),
                   key=lambda c: (-sum(counts[k][c] for k in kinds), c))
    if names:
        out += ["", "### Responses by distribution channel", "",
                "| Channel | " + " | ".join(kinds) + " |",
                "| --- |" + " ---: |" * len(kinds)]
        out += [f"| {c} | " + " | ".join(str(counts[k][c]) for k in kinds) + " |" for c in names]

    return "\n".join(out) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("export", nargs="?", type=Path, help="raw LamaPoll export (CSV)")
    parser.add_argument("--extreme-page", type=float, default=1800,
                        help="seconds on one page above which a response is excluded (default 1800)")
    args = parser.parse_args(argv)
    path = args.export or find_latest_export(DATA_DIR)
    sys.stdout.write(build_report(path, args.extreme_page))


if __name__ == "__main__":
    main()
