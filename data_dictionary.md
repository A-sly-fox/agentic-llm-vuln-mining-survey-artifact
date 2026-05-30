# Data Dictionary

This dictionary describes the non-sensitive audit artifact used by the survey manuscript. It is intended to help reviewers inspect corpus construction, A/E coding, bibliographic verification, and second-coder preparation.

## Common Identifiers

- `record_id`: stable identifier for one candidate record in the 205-record corpus.
- `core_id`: stable identifier for one final Core study in the 27-record deeply coded subset.
- `sample_id`: stable identifier for one record in the second-coder sample.

## `data/corpus.csv`

- `record_id`: candidate record identifier.
- `title`: record title as used in the local corpus.
- `year`: publication or release year from local metadata.
- `authors`: author string when available; `NA` means not filled in the public-minimal artifact.
- `source_type`: local source type, such as `journalArticle`, `conferencePaper`, `preprint`, or `thesis`.
- `venue_or_source`: local venue/source provenance.
- `doi_or_url`: DOI, URL, ISBN URN, or other local locator.
- `corpus_layer`: analysis-use layer: `Core`, `Supporting`, `Background`, or `Excluded`.
- `task_category`: coarse task family used during screening.
- `exclusion_reason`: reason for exclusion, or `NA`.
- `note`: local audit note.

## `data/core_coding.csv`

- `core_id`: Core-study coding identifier.
- `record_id`: link to `corpus.csv`.
- `system_alias`: short system or benchmark name.
- `task_category`: security task category used in manuscript analysis.
- `a_level`: LLM agency level. See `codebook.md`.
- `a_level_reason`: textual rationale for A-level coding.
- `e_level`: evidence level. See `codebook.md`.
- `e_level_reason`: textual rationale for E-level coding.
- `evidence_object`: object of evidence, such as model judgment, task completion, system output, task background, external clue, or governance risk.
- `external_evidence_profile`: brief external-evidence characterization.
- `artifact_available`: local note on artifact availability.
- `version_reported`: local note on version reporting.
- `environment_reported`: local note on environment reporting.
- `external_confirmation_reported`: local note on independent/external confirmation.
- `note`: boundary, caveat, or manual-check note.

## `data/screening_summary.csv`

- `stage`: corpus construction or screening stage.
- `count`: count if recoverable; `NA` means not recoverable from local records.
- `note`: explanation or boundary condition.

## `data/reference_audit.csv`

- `record_id`: link to `corpus.csv`.
- `canonical_title`: normalized title used for bibliographic audit.
- `system_alias`: system alias when available.
- `publication_status`: current working status after local/Zotero/official-source audit.
- `venue`: venue, repository, proceedings, or source.
- `official_url`: official page, DOI URL, arXiv URL, project page, or best available locator.
- `arxiv_id`: arXiv identifier if applicable; otherwise `NA`.
- `doi`: DOI if available; otherwise `NA`.
- `last_verified_date`: date of the latest local audit update for this row.
- `note`: provenance, risk flags, and manual-check notes.

## Verification Worksheets

`data/verification_todo.csv` is a working sheet for official-source verification. Fields prefixed with `current_` describe the audit state when the worksheet was generated. `zotero_*` fields are local Zotero candidates, not final official-source proof.

`data/zotero_doi_merge_delta.csv` records DOI merge provenance and risk flags. Important risk flags include:

- `needs_publisher_landing_check`
- `arxiv_doi_check_version`
- `differs_from_current_doi`
- `differs_from_url_doi_candidate`
- `published_doi_with_arxiv_url_check_version`

`data/doi_remaining_manual_status.csv` documents records that remain DOI-less after the DOI merge and round-2 pass.

## Intercoder Files

`data/intercoder_sample_blind.csv` is the file to share with an independent second coder. It intentionally withholds current labels.

`data/intercoder_sample_key.csv` is for adjudication only and should not be shared before independent coding is complete.

`data/disagreement_resolution_template.csv` records coder decisions, adjudicated decisions, rationales, and resolution metadata after real second-coder results exist.

## Missing Values

`NA` means one of the following:

- not applicable to the record;
- not recoverable from local records;
- intentionally withheld from the minimal public artifact;
- not yet verified against official sources.

Do not infer a missing value from surrounding rows without recording the source and rationale.
