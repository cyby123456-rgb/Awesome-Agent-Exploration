# Candidate registry

`data/candidates.json` is a review ledger, not part of the public catalog.
Records enter it when a legacy source conflicts with a title, a source is
missing, or automated discovery finds a potentially relevant work.

Each candidate has a stable ID, title, reason, next step, and optional legacy
source clue. Its `status` is one of:

- `pending`: still needs source or scope review.
- `promoted`: accepted into `data/papers.json`; `resolved_to` names the catalog
  record ID.
- `rejected`: reviewed and out of scope or unsupported.
- `duplicate`: merged into another candidate or catalog record.

A candidate can be promoted only after a reviewer confirms the exact primary
source, scope, primary area, and required taxonomy tags. Do not treat a
candidate's legacy source as verified evidence.
