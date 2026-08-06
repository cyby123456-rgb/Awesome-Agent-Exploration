# Candidate registry

`data/candidates.json` is a review ledger, not part of the public catalog.
Records enter it when a legacy source conflicts with a title, a source is
missing, or automated discovery finds a potentially relevant work.

Each candidate has a stable ID, title, reason, next step, and optional legacy
source clue. Its `status` is one of:

- `pending`: still needs source or scope review and must state `next_step`.
- `promoted`: accepted into `data/papers.json`; `resolved_to` names the catalog
  record ID and `resolved_at` records the decision date.
- `rejected`: reviewed and out of scope or unsupported; record `decision_reason`
  and `resolved_at`.
- `duplicate`: merged into another candidate or catalog record; `duplicate_of`
  records the target.

A candidate can be promoted only after a reviewer confirms the exact primary
source, scope, primary area, and required taxonomy tags. Do not treat a
candidate's legacy source as verified evidence.
