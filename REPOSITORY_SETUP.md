# Repository Setup Checklist

This file records the steps needed to turn this release candidate into a public artifact repository.

## Suggested Repository

Suggested repository name:

`agentic-llm-vuln-mining-survey-artifact`

Suggested short description:

`Non-sensitive audit artifact for a survey of Agentic LLM systems for vulnerability mining.`

## Before Creating the Repository

- [x] Choose final license: CC BY 4.0 for data/docs and MIT for code.
- [ ] Replace `REPLACE_WITH_PUBLIC_REPOSITORY_URL` in `CITATION.cff`.
- [ ] Replace `[REPOSITORY URL]` in the manuscript.
- [ ] Decide whether author names should remain anonymous before review.
- [x] Decide whether the repository should be private until acceptance or public at submission: private repository for now.
- [x] Decide whether to archive the release on Zenodo: no Zenodo for now.

## Initial Repository Contents

Commit the contents of `artifact_public_release_candidate/`, not the whole working directory.

Do not commit:

- local Zotero export;
- internal phase reports;
- manuscript snapshots or logs;
- proposed/intermediate audit tables;
- `intercoder_sample_key.csv`;
- private notes or backup files.

## Suggested First Commit Message

`Add minimal audit artifact release candidate`

## Suggested Release Tag

`v0.1.0-rc`

Use a final `v1.0.0` release only after repository URL, license, manuscript metadata, and optional Zenodo archive are finalized.
