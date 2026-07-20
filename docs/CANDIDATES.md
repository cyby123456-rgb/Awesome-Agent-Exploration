# Candidate registry

`data/candidates.json` is a review queue, not part of the public catalog.
Records enter it when a legacy source conflicts with a title, a source is
missing, or automated discovery finds a potentially relevant work.

Each candidate has a stable ID, a `pending` status, a title, the reason it
requires review, and any legacy source clue. A candidate can move to
`data/papers.json` only after a reviewer confirms the exact primary source,
scope, primary area, and required taxonomy tags.

Do not treat a candidate's legacy source as verified evidence.
