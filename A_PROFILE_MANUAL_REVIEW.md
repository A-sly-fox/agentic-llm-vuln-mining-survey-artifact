# A Profile Manual Review

This checklist records Core records whose A-profile notation should be reviewed by the author before any further semantic consolidation. It is intentionally conservative: no record is upgraded to A2 or A3 unless the underlying paper text makes the interaction-depth base explicit.

| Core ID | system alias | old A notation | new A notation | whether interaction-depth base is explicit | manual review required | notes |
|---|---|---|---|---|---|---|
| C03 | Multi-Agent Collaborative Smart Contract Fuzzing | `A4` | `A4` | no | yes | Keep as overlay orchestration unless explicit tool/execution depth is documented. |
| C04 | FuzzingBrain | `A3--A5` | `A3 + A4 + A5` | partial | yes | Treat as combined interaction-depth plus orchestration/update profile only if the paper supports all components. |
| C11 | MALF | `A4` | `A4` | no | yes | Do not infer A2/A3 from orchestration alone. |
| C12 | NeTestLLM | `A4` | `A4` | no | yes | Orchestration is explicit; lower interaction depth is not assumed. |
| C13 | PBFuzz | `A3--A5` | `A3 + A4 + A5` | partial | yes | Preserve as a mixed profile until the manuscript explicitly supports all three tags. |
| C14 | Co-RedTeam | `A4` | `A4` | no | yes | Benchmark-style orchestration should remain an overlay tag. |
| C15 | Real-world Pentest Agent Study | `A4` | `A4` | no | yes | Keep the interaction-depth base unexpanded. |
| C17 | Multi-Agent Harnesses | `A4--A5` | `A4 + A5` | partial | yes | Review whether the workflow actually demonstrates persistent adaptation beyond orchestration. |
| C18 | PentestAgent | `A4` | `A4` | no | yes | Do not infer A2/A3. |
| C23 | Cybench | `A4` | `A4` | no | yes | Controlled benchmark completion remains an overlay-capability case. |
| C24 | BountyBench | `A4` | `A4` | no | yes | Governance / benchmark framing should stay separate from interaction depth. |
| C26 | CyberGym | `A3--A5` | `A3 + A4 + A5` | partial | yes | Keep explicit distinction between interaction depth and overlay capabilities. |
| C27 | AgentFuzz | `A4` | `A4` | no | yes | Governance-oriented boundary case; do not reclassify into target-vulnerability discovery. |
| C28 | FuzzingBrain V2 | `A4` | `A4` | no | yes | Overlay orchestration is explicit; maintain conservative reading. |
| C30 | OSS-CRS | `A4` | `A4` | no | yes | Keep as orchestration-heavy Core without auto-inferring deeper interaction depth. |
| C31 | GONDAR | `A4` | `A4` | no | yes | Review only if the source text makes tool/execution depth explicit. |
