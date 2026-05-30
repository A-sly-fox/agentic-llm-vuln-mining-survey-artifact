# Release Manifest

Date prepared: 2026-05-31

## Included

The release candidate includes files that are necessary for non-sensitive survey auditability:

- corpus metadata;
- final Core A/E coding;
- corpus screening summary;
- DOI-enriched reference audit;
- remaining DOI-less status notes;
- coding codebook;
- field dictionary;
- second-coder blind sample and blank templates;
- disagreement-resolution template;
- security boundary and release checklist;
- reproducibility script.
- citation metadata template;
- license options note;
- repository setup checklist;
- `.gitignore` for excluding local/private working files.

## Excluded

The following working files are intentionally excluded from this public release candidate:

- local Zotero BibTeX export;
- proposed/intermediate reference audit variants;
- audit-table backups;
- Zotero DOI merge deltas;
- autofill candidate worksheets;
- verification todo worksheets containing local Zotero keys and working notes;
- `intercoder_sample_key.csv`, because it should not be shared before independent second-coder work is complete;
- compile logs, snapshots, manuscript files, and internal phase reports.

## Rationale

The package should be enough for reviewers to inspect the survey's corpus layers, A/E coding logic, bibliographic traceability, and reproducibility checks. It should not expose local library state, private working history, second-coder answer keys, or sensitive vulnerability materials.

## Before Public Release

Open decisions:

- public repository URL;
- whether to archive on Zenodo;
- final release date;
- whether to include completed second-coder results after real independent coding is available.

License decision:

- data/docs: CC BY 4.0 via `LICENSE-DATA`;
- code scripts: MIT via `LICENSE-CODE`.
