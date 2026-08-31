<div align="center">

# Ritesh Ekbote

**Bug bounty hunter · Security researcher · Automation engineer**

I build automated systems that perform continuous, authorized security research —
multi-model AI pipelines, target inventory, recon, lead discovery, triage, and verification —
orchestrated with GitHub Actions.

<a href="https://www.linkedin.com/in/ritesh-ekbote/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:ritesh@ekbote.dev"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>

</div>

---

## What I Build

Software that turns bug-bounty hunting into a repeatable, measurable engineering discipline instead of a series of manual clicks:

- **Autonomous hunting pipelines** — scheduled, multi-model agents that move through recon → surface → hypothesis → triage → verification, one phase per cycle, with state and a shared knowledge base.
- **Multi-model analysis** — prompt-driven analyst, triager, and verifier roles; outputs are ranked by confidence and gated through a 7-Question validation gate before anything is reported.
- **Passive-first, scope-bound testing** — every pipeline is bound to an explicit authorized scope, uses GET/HEAD/OPTIONS-only probes where rules require it, and enforces rate limits, politeness budgets, and 403/429 grace-stops.
- **Target inventory & verification** — per-target asset lists, live-host checks, and an honest distinction between *leads* (candidate findings) and *validated bugs*.

The `*-hunt` repositories are concrete deployments of this model against specific authorized bug-bounty programs.

## Featured Projects

| Project | Description |
|---|---|
| [DedupeAI](https://github.com/riteshekbote/DedupeAI) | Burp Suite (Montoya) extension: deduplicates HTTP history into an AI-ready unique-request feed, color-codes attacker/victim traffic by listener port, and ships the set to Claude Code — built for multi-account IDOR/BOLA testing. |
| [oniontui](https://github.com/riteshekbote/oniontui) | Terminal AI assistant that browses and searches the web — including `.onion` hidden services — through Tor, with plan-first agents, working memory, and circuit rotation. |
| [Js-Scanner](https://github.com/riteshekbote/Js-Scanner) | AI-powered JS security audit tool: crawls a site's scripts, extracts endpoints/secrets/JWTs, and produces an interactive report. |
| [gladia-hunt](https://github.com/riteshekbote/gladia-hunt) | 24/7 multi-model bug-hunting automation bound to the Gladia authorized scope. |
| [threema-hunt](https://github.com/riteshekbote/threema-hunt) | 24/7 passive, read-only multi-model hunting pipeline for the Threema program. |

## Research Areas

**Web2** · IDOR · broken access control · auth/ATO chains · business logic · SSRF · injection

**Mobile** · Android/iOS app assessment (jadx, Frida, objection, MobSF)

**AI/LLM** · prompt injection · RAG/vector-store poisoning · agentic AI security (ASI01–ASI10)

**Web3** · smart-contract auditing (Foundry, Slither, Echidna)

**Cloud / infra** · AWS/GCP/K8s misconfiguration · post-credential privilege analysis

## Automation & Tooling

`GitHub Actions` · `opencode` multi-model agents · `Python` · recon (subfinder, dnsx, httpx) · `Burp Suite` / Montoya · `Frida` · `jadx` · `Foundry` · `Slither` · orchestrating scheduled, stateful, verifiable research.

## How I Work

1. **Scope first** — every pipeline is bound to an explicit authorized target with exclusions and safe defaults.
2. **Passive before active** — read-only probes where program rules require it.
3. **Leads ≠ findings** — candidate hypotheses are triaged by a second model and validated before reporting.
4. **Humans decide** — models propose; I verify and submit.

---

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=riteshekbote&theme=redical&hide_border=true&bg_color=0d1117&color=FF6B6B&line=FF6B6B&point=ffffff)](https://github.com/riteshekbote)

*Hack legally. Report responsibly.* 🔒

<!-- STATS:START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Followers | **4** |
| Public repos | **119** |
| Total stars | **9** |

**Recently updated:**

- [aurasell-hunt](https://github.com/riteshekbote/aurasell-hunt) — 24/7 multi-model bug-hunting automation for the Aurasell Bug Bounty program (aurasell.ai)
- [cfoptimizer-hunt](https://github.com/riteshekbote/cfoptimizer-hunt) — 24/7 multi-model bug-hunting automation for Cash Flow Optimizer vulnerability reporting (cfoptimizer.com)
- [hunt-100](https://github.com/riteshekbote/hunt-100) — 100+ bounty automation — Muse Spark 1.2 Free OpenCode Zen xhigh
- [qwen-hunt](https://github.com/riteshekbote/qwen-hunt) — 24/7 Qwen3 abliterated (Ollama) bug-hunting automation
- [hunt-lab](https://github.com/riteshekbote/hunt-lab) — Restored Google/Microsoft VRP hunt — Muse Spark 1.2 Free Zen xhigh

> _Last refreshed: 2026-08-31 10:46 UTC — auto-updated daily by GitHub Actions (`.github/workflows/profile-stats.yml`)_
<!-- STATS:END -->
