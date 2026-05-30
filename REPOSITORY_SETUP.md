# Repository Setup Checklist

This file records the steps needed to turn this release candidate into a public artifact repository.

## Suggested Repository

Suggested repository name:

`agentic-llm-vuln-mining-survey-artifact`

Suggested short description:

`Non-sensitive audit artifact for a survey of Agentic LLM systems for vulnerability mining.`

## Before Creating the Repository

- [x] Choose final license: CC BY 4.0 for data/docs and MIT for code.
- [x] Replace `REPLACE_WITH_PUBLIC_REPOSITORY_URL` in `CITATION.cff`.
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

## Current Local Git State

This release candidate has already been initialized as a local Git repository on branch `main`.

The first local commit has been created with anonymous review-safe metadata:

- author name: `Anonymous Authors`
- author email: `anonymous@example.com`
- commit message: `Add minimal audit artifact release candidate`

## Push After Creating a Private GitHub Repository

After creating a private repository named `agentic-llm-vuln-mining-survey-artifact` under the target GitHub account, run these commands from `artifact_public_release_candidate/`:

```bash
git remote add origin https://github.com/OWNER/agentic-llm-vuln-mining-survey-artifact.git
git push -u origin main
```

Replace `OWNER` with the actual GitHub owner or organization.

If using HTTPS and GitHub asks for credentials, use a personal access token or GitHub Desktop. Do not paste tokens into manuscript files or artifact data files.

Current remote:

```bash
origin https://github.com/oldpanthead/agentic-llm-vuln-mining-survey-artifact.git
```
