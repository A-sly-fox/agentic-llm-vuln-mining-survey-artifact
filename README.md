# Minimal Audit Artifact for Agentic LLM Vulnerability Mining Survey

This release candidate contains a non-sensitive audit artifact for a survey on Agentic LLM systems for vulnerability mining. It supports inspection of corpus construction, A/E coding, bibliographic traceability, and second-coder preparation.

## Scope

This package is for survey auditability. It is not an exploit reproduction package.

It excludes undisclosed PoCs, exploit payloads, private targets, credentials, live vulnerability reproduction instructions, sensitive crash inputs, and private vendor or bug-bounty communication.

## Corpus Summary

- Candidate records: 205
- Core studies: 27
- Supporting studies: 65
- Background references: 93
- Excluded records: 20

## Files

- `data/corpus.csv`: corpus metadata and analysis-use layers.
- `data/core_coding.csv`: A/E coding for the 27 final Core studies.
- `data/screening_summary.csv`: recoverable corpus construction and layer counts.
- `data/reference_audit.csv`: DOI-enriched bibliographic audit table.
- `data/doi_remaining_manual_status.csv`: records that remain DOI-less after audit passes.
- `data/intercoder_check_template.csv`: blank template for independent second-coder checking.
- `data/intercoder_sample_blind.csv`: 30-record blind second-coder sample.
- `data/disagreement_resolution_template.csv`: blank disagreement-resolution worksheet.
- `codebook.md`: A/E coding definitions and boundary examples.
- `data_dictionary.md`: field-level data dictionary.
- `intercoder_instructions.md`: second-coder workflow and security instructions.
- `SECURITY_BOUNDARY.md`: explicit security and release boundary.
- `public_release_checklist.md`: release-readiness checklist.
- `reproduce_tables.py`: reproducibility checks for counts and A/E distributions.
- `RELEASE_MANIFEST.md`: file inclusion/exclusion rationale.
- `LICENSE_OPTIONS.md`: license choices awaiting author decision.
- `CITATION.cff`: citation metadata template with placeholder repository URL.
- `REPOSITORY_SETUP.md`: checklist for creating the public artifact repository.
- `.gitignore`: guardrails for keeping local/private working files out of the release repository.

## Reproduce Checks

Run from this directory:

```bash
python reproduce_tables.py
```

Expected result: all corpus counts and A/E distribution checks pass. Remaining missing DOI rows are reported as warnings, not errors.

## License

This release candidate uses a split license:

- data and documentation: CC BY 4.0, see `LICENSE-DATA`;
- code scripts: MIT License, see `LICENSE-CODE`.

The main code file covered by MIT is `reproduce_tables.py`. The CSV files and Markdown documentation are covered by CC BY 4.0 unless a file states otherwise.

## Current Limitations

- Some intermediate screening counts are marked `NA` because they are not recoverable from current local logs.
- The second-coder sample is prepared, but no real second-coder results or agreement statistics are included.
- A small number of records remain DOI-less and are documented in `data/doi_remaining_manual_status.csv`.
- The final public repository URL, release date, license, and archival DOI are not yet assigned.
