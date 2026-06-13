# Legacy Code Crosswalk

## Purpose

This file explains how the legacy A/E coding fields correspond to the natural-language terminology used in the v13 manuscript. It is a compatibility note for audit and reproduction. It is not a new coding system and does not overwrite the existing artifact fields.

## Legacy A0--A5 and natural-language capability terms

| Legacy field | Manuscript term | Recommended use in manuscript-oriented summaries |
|---|---|---|
| A0 | Candidate / textual judgment | Ordinary prompt-based detection or background reference |
| A1 | Textual discussion / role-based reasoning | Text-only multi-role discussion or boundary reference |
| A2 | Tool-enhanced analysis | Context aggregation, rule extraction, tool access, and candidate convergence |
| A3 | Execution-feedback loop | Feedback interpretation and closed-loop adjustment |
| A4 | Multi-Agent / multi-module orchestration | Long-horizon orchestration, state management, or verification-duty organization |
| A5 | Cross-round strategy update | Failure summarization and strategy update |

A4 and A5 may coexist with A0--A3 in the artifact. The manuscript should not present A0--A5 as a strictly linear maturity ladder.

## Legacy E0--E3 and evidence-output terms

| Legacy field | Manuscript term | Recommended use in manuscript-oriented summaries |
|---|---|---|
| E0 | Candidate judgment | Classification metrics, risk labels, explanations, or rankings |
| E1 | Controlled task completion | CTF, benchmark, cyber range, or task success |
| E2 | Runtime security signal | Crash, assertion, sanitizer, oracle, or coverage combined with explicit security conditions |
| E3 | Reproducible validation | Replay, PoC, PoV, patch validation, or reproducible trigger path |

## Legacy E4a--E4c and external audit materials

| Legacy field | Manuscript term | Recommended use in manuscript-oriented summaries |
|---|---|---|
| E4a | Author-reported external signal | Author-reported vulnerability discovery, deployment, confirmation, or competition background |
| E4b | Public material | Benchmark ground truth, project page, public repository, announcement, or task background |
| E4c | Claim-level audit material | Artifact, version, environment, external link, and confirmation workflow traceable to a specific vulnerability claim |

## Legacy fields retained in the artifact

- `legacy_a_profile`
- `legacy_evidence_stage`
- `legacy_external_evidence_profile`
- `evidence_object`
- `original_a_level` / `a_level`
- `original_e_level` / `e_level`

## Legacy fields no longer used as the manuscript backbone

- A0--A5 as a section-by-section taxonomy.
- Combination-style expressions such as `A3 + A4 + A5 / E3`.
- E4a--E4c as long-form chapter-level definitions.

## Natural-language fields used by the v13 manuscript

- `workflow_coverage`
- `agent_capabilities`
- `strongest_evidence_output`
- `external_audit_materials`
- `agent_contribution`
- `claim_boundary`
- `manual_review_required`
