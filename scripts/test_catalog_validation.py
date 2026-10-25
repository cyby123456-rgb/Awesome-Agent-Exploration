"""Regression checks for evidence dates and the legacy editorial backlog."""

import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_catalog


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads(validate_catalog.DATA_PATH.read_text())
        self.backlog = json.loads(validate_catalog.RATIONALE_BACKLOG_PATH.read_text())

    def validate(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / "papers.json"
            backlog = Path(directory) / "rationale_backlog.json"
            data.write_text(json.dumps(self.catalog))
            backlog.write_text(json.dumps(self.backlog))
            output = io.StringIO()
            with patch.object(validate_catalog, "DATA_PATH", data), patch.object(validate_catalog, "RATIONALE_BACKLOG_PATH", backlog), contextlib.redirect_stdout(output):
                result = validate_catalog.main()
            return result, output.getvalue()

    def reviewed_paper(self):
        return next(p for p in self.catalog["papers"] if p.get("evidence"))

    def test_existing_catalog_and_debt_are_explicitly_accepted(self):
        self.assertEqual(self.validate()[0], 0)

    def test_new_template_is_rejected(self):
        self.reviewed_paper()["rationale"] = "A new tag list as the recorded exploration evidence."
        result, output = self.validate()
        self.assertEqual(result, 1)
        self.assertIn("new or changed template rationale", output)

    def test_grandfathered_template_cannot_be_changed(self):
        legacy = next(p for p in self.catalog["papers"] if validate_catalog.legacy_rationale(p["rationale"]))
        legacy["rationale"] += " More generic wording."
        self.assertEqual(self.validate()[0], 1)

    def test_rewrite_must_leave_the_backlog(self):
        row = self.backlog["papers"][0]
        paper = next(p for p in self.catalog["papers"] if p["id"] == row["id"])
        paper["rationale"] = "A source-based contribution description."
        self.assertEqual(self.validate()[0], 1)
        self.backlog["papers"].remove(row)
        self.assertEqual(self.validate()[0], 0)

    def test_impossible_calendar_date_is_rejected(self):
        self.reviewed_paper()["evidence"]["verified_at"] = "2026-02-30"
        self.assertEqual(self.validate()[0], 1)

    def test_review_cannot_follow_registry_update(self):
        self.reviewed_paper()["evidence"]["verified_at"] = "2026-10-26"
        self.assertEqual(self.validate()[0], 1)

    def test_search_cutoff_cannot_follow_registry_update(self):
        self.catalog["literature_search_cutoff"] = "2026-10-26"
        self.assertEqual(self.validate()[0], 1)

    def test_evidence_requires_source_scope_and_limits(self):
        original = copy.deepcopy(self.reviewed_paper()["evidence"])
        for field, value in (("source_url", "http://example.com/paper"), ("scope", "replicated"), ("limitations", "")):
            with self.subTest(field=field):
                paper = self.reviewed_paper()
                paper["evidence"] = copy.deepcopy(original)
                paper["evidence"][field] = value
                self.assertEqual(self.validate()[0], 1)


if __name__ == "__main__":
    unittest.main()
