# Minimal Audit Artifact for Agentic LLM Vulnerability Mining Survey

This current public audit artifact contains non-sensitive materials for a survey on Agentic LLM systems for vulnerability mining. It supports inspection of corpus construction, A/E coding, bibliographic traceability, boundary-record classification, and second-coder preparation.

## Scope

This package is for survey auditability. It is not an exploit reproduction package.

It excludes undisclosed PoCs, exploit payloads, private targets, credentials, live vulnerability reproduction instructions, sensitive crash inputs, and private vendor or bug-bounty communication.

## Corpus Summary

- Candidate records: 212
- Analytical Core studies: 31
- Supporting studies: 66
- Background references: 95
- Excluded records: 20
- Last incremental manuscript search date: 2026-05-20

## Files

- `data/corpus.csv`: corpus metadata and analysis-use layers.
- `data/core_coding.csv`: A/E coding for the 31 Core studies.
- `data/corpus_layer_audit.csv`: corpus-layer audit with Core / Supporting / Background / Excluded scope fields.
- `data/record_classification_audit.csv`: classification audit for seven boundary/high-relevance records moved out of the manuscript table.
- `data/literature_update_decisions.csv`: source and provenance tracking sheet for the same seven high-relevance records.
- `data/core31_second_coder_full_template_submission.csv`: full 31-Core second-coder template with auxiliary audit fields.
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
- `LICENSE_OPTIONS.md`: license rationale for the current split-license setup.
- `CITATION.cff`: citation metadata for the current public repository.
- `REPOSITORY_SETUP.md`: repository setup decisions and current remote notes.
- `.gitignore`: guardrails for keeping local/private working files out of the release repository.

## Reproduce Checks

Run from this directory:

```bash
python reproduce_tables.py
```

Expected result: all corpus counts and A/E distribution checks pass. Remaining missing DOI rows are reported as warnings, not errors.

## License

This artifact uses a split license:

- data and documentation: CC BY 4.0, see `LICENSE-DATA`;
- code scripts: MIT License, see `LICENSE-CODE`.

The main code file covered by MIT is `reproduce_tables.py`. The CSV files and Markdown documentation are covered by CC BY 4.0 unless a file states otherwise.

## Current Limitations

- Some intermediate source-specific screening counts remain unrecoverable.
- No real second-coder results or agreement statistics are included yet.
- The blind second-coder sample and full 31-Core template are prepared only as review scaffolds.
- A small number of records remain DOI-less and are documented in `data/doi_remaining_manual_status.csv`.
- The current public repository URL is `https://github.com/oldpanthead/agentic-llm-vuln-mining-survey-artifact`; an archival DOI is not yet assigned.
