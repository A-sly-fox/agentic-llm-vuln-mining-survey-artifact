# Intercoder Check Instructions

## Purpose

This template supports an independent second-coder check for the survey corpus layering, A-profile coding, E-level coding, evidence object coding, and external-evidence profile coding. It is a template only. It does not contain second-coder decisions, agreement rates, Cohen's kappa, weighted kappa, or resolved disagreements.

## Independence Requirement

The second coder must complete the check independently. They should not copy or adjust answers after seeing the first coder's detailed decisions. The goal is to measure whether another informed reader can apply the coding guide to the same records, not to confirm the current table mechanically.

Before coding, give the second coder:

- The paper abstract or scope statement.
- `codebook.md`.
- The sampled records or papers to inspect.
- This instruction file.

Do not give them a pre-filled answer key for the sampled rows.

## Suggested Sample

Use a compact but meaningful sample rather than the full corpus unless the author has enough reviewer time.

- Select 10--12 Core studies.
- Select 8--10 Core / Supporting boundary records.
- Select 5--8 Supporting studies.

The sample should include at least:

- One A0/A1 or boundary prompt-based case.
- Several A3 execution-feedback cases.
- Several A4 multi-agent or benchmark cases.
- At least one E4a case.
- At least one E4b case.
- The governance-oriented Core case, if governance risk is part of the manuscript's argument.

## CSV Fields

Fill `data/intercoder_check_template.csv` with one row per sampled record.

- `sample_id`: Local sample identifier, such as `S01`.
- `record_id`: The candidate or Core record identifier from the artifact data.
- `corpus_layer_decision`: Second coder's layer decision, such as `Core`, `Supporting`, `Background`, or `Excluded`.
- `a_level`: Second coder's A-profile decision, such as `A0`, `A1`, `A2`, `A3`, `A4`, `A5`, or a plus-style capability combination if the codebook permits it.
- `e_level`: Second coder's E-level decision, such as `E0`, `E1`, `E2`, `E3`, `E4a`, `E4b`, or `E4c`.
- `evidence_object`: One of the six manuscript categories: model judgment, task completion, system output, task background, external clues, or governance risk.
- `external_evidence_profile`: Use `E4a`, `E4b`, `E4c`, or `NA` when no external-evidence profile applies.
- `coder`: The second coder identifier or initials.
- `decision_reason`: Short justification grounded in the paper or public material.
- `disagreement_note`: Leave blank during independent coding. Fill later only when comparing against the first coding.
- `resolution`: Leave blank during independent coding. Fill later after discussion and adjudication.

## Agreement Calculation

After the second coder completes the sheet, the author may calculate:

- Raw agreement for corpus layer.
- Raw agreement for A-profile.
- Raw agreement for E-level.
- Raw agreement for evidence object.
- Cohen's kappa for categorical fields, if appropriate.
- Weighted kappa for ordinal-like fields, if the author defines and justifies weights.

Codex must not invent agreement rates, Cohen's kappa, weighted kappa, or disagreement resolutions. These values require real second-coder decisions.

## Handling Disagreements

After independent coding is complete:

1. Compare second-coder decisions against the first coding.
2. Mark disagreements in `disagreement_note`.
3. Discuss each disagreement with reference to `codebook.md` and the paper text.
4. Record the final adjudicated decision in `resolution`.
5. Preserve both the original second-coder decision and the resolution for auditability.

## Security Boundary

Do not include undisclosed PoCs, exploit payloads, private target details, or sensitive vulnerability reproduction steps in the intercoder file. If a decision depends on sensitive material, record a non-sensitive reason and mark the sensitive source as restricted.
