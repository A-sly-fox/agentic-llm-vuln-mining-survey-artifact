# Release Manifest

Date prepared: 2026-06-02

## Included

The release candidate includes files that are necessary for non-sensitive survey auditability:

- corpus metadata;
- Core A/E coding;
- corpus-layer audit;
- literature-update decision audit;
- full 31-Core second-coder submission template with auxiliary audit fields;
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
- verification status worksheets containing local Zotero keys and working notes;
- `intercoder_sample_key.csv`, because it should not be shared before independent second-coder work is complete;
- compile logs, snapshots, manuscript files, and internal phase reports.

## Rationale

The package should be enough for reviewers to inspect the survey's corpus layers, A/E coding logic, literature-update decisions, bibliographic traceability, and reproducibility checks. It should not expose local library state, private working history, second-coder answer keys, or sensitive vulnerability materials.

## Before Public Release

Open decisions:

- whether to archive on Zenodo;
- final release date;
- whether to include completed second-coder results after real independent coding is available.

Current public repository URL: `https://github.com/oldpanthead/agentic-llm-vuln-mining-survey-artifact`.

License decision:

- data/docs: CC BY 4.0 via `LICENSE-DATA`;
- code scripts: MIT via `LICENSE-CODE`.
