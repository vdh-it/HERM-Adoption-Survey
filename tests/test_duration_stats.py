import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "qa"))
import duration_stats as ds

HEADER = [
    "ID", "Frage 1 - How would you like to proceed?",
    "Frage 11 - Current status of Enterprise Architecture at your institution",
    "Frage 21 - Institutional HERM adoption status",
    "abgeschlossen", "Beantwortungsdauer (in s)", "Antwort-Quote", "Attribut 2",
    "Dauer für Seite 1 (in s)", "Dauer für Seite 2 (in s)", "Dauer für Seite 3 (in s)",
]
PART = "Participate in the survey. I have read the information above ..."
PREVIEW = "Preview the questionnaire only. My responses will not be included in the study."


def row(i, ea, herm, done, pages, proceed=PART, rate="50%", channel="Distribution_X"):
    return [i, proceed, ea, herm, done, sum(pages), rate, channel, *pages]


class DurationStatsTest(unittest.TestCase):
    def write(self, rows, delimiter=","):
        tmp = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                          newline="", encoding="utf-8-sig")
        writer = csv.writer(tmp, delimiter=delimiter)
        writer.writerow(HEADER)
        writer.writerows(rows)
        tmp.close()
        self.addCleanup(Path(tmp.name).unlink)
        return Path(tmp.name)

    def test_extreme_pause_excluded_long_page_kept(self):
        rows = [
            row(1, "No EA practice", "Not considered", "1", [60, 120, 60]),
            row(2, "No EA practice", "Not considered", "1", [60, 120, 120]),
            row(3, "No EA practice", "Not considered", "1", [60, 700, 140]),     # long page, kept
            row(4, "No EA practice", "Not considered", "1", [60, 120, 90000]),   # extreme pause
            row(5, "Established operational practice", "Active operational use", "1", [600, 600, 600]),
        ]
        report = ds.build_report(self.write(rows), extreme=1800)
        # used durations 4, 5 and 15 min
        self.assertIn("| **Short path:** no EA practice and HERM not in use | 4 | 1 | 3 | 5.0 | 4.5–10.0 | 1 |",
                      report)
        self.assertIn("| **Heavy users:** EA operational and HERM Section 4 | 1 | 0 | 1 | – | – | 0 |", report)

    def test_previews_breakoffs_and_channels(self):
        rows = [
            row(1, "Exploring or planning EA", "Not considered", "0", [30, 0, 0], rate="1%"),
            row(2, "", "", "1", [5, 10, 5], proceed=PREVIEW, channel="Distribution_Y"),
            row(3, "", "", "0", [5, 0, 0], proceed=PREVIEW, channel="Distribution_Y"),
        ]
        report = ds.build_report(self.write(rows, delimiter=";"), extreme=1800)
        self.assertIn("| **Preview** (0.1), all | 2 | 0 | 2 |", report)
        self.assertIn("|   Preview clicked through to the end | 1 |", report)
        self.assertIn("|   of which left after consent (answer rate < 5 %) | 1 |", report)
        self.assertIn("| Y | 0 | 0 | 2 |", report)
        self.assertIn("| X | 0 | 1 | 0 |", report)
        self.assertNotIn("probably filtered", report)

    def test_filtered_export_note(self):
        rows = [row(i, "No EA practice", "Not considered", "1", [60, 60, 60]) for i in range(3)]
        report = ds.build_report(self.write(rows), extreme=1800)
        self.assertIn("| All completed | 3 | 0 | 3 | 3.0 |", report)
        self.assertIn("probably filtered", report)


if __name__ == "__main__":
    unittest.main()
