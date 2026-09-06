# Weeks 12–14 — harden, write up, hand over

The copilot is built and measured. These three weeks make it safe, make it presentable, and turn
the work into each intern's career evidence.

## Week 12 — harden

- **Security pass on your own feature.** Secrets never in code (a scan proves it); prompt-injection
  filtered; PII redacted before any model call; check what's publicly reachable; a dependency scan.
- **Load test.** How does it behave under many concurrent queries? Where does it slow? Fix or
  document the limit.
- **Spec-driven development, named.** By now you've run the lifecycle a dozen times — anti-thesis →
  design → gate → build → review → tests → gate. This week it gets its name, and the recorded case
  where a review caught an overstated benchmark becomes the lesson.
- *Done when:* the security checklist passes; a load-test report exists with an honest limit.

## Week 13 — write it up

- **Documentation.** A README a stranger can run the copilot from; an architecture note; the API.
- **The benchmark report.** The gold-set numbers, before/after, the failure analysis — the artifact
  that becomes a résumé bullet.
- **Résumé (complimentary service).** Turn the evidence into an ATS-compliant, recruiter-ready
  résumé: one column, job-description keywords, bullets as *number · method · scale*, GitHub + live
  URL at the top. See [/project §6](https://vtu-internship-proposal.vercel.app/project/#skills).
- **Certification plan.** One high-value AI certification, prep started (the guide — verify current
  exam codes/prices before relying on it).
- *Done when:* the repo is documented; each intern has a benchmark report and a first-draft résumé.

## Week 14 — hand over

- **The mentor acceptance panel.** A group of mentors reviews the copilot against the real-world
  bar: *would this help a sales exec on the floor?* Judged on shippability, not a rubric. Each
  track owner presents their part and the numbers.
- **Demo.** The whole copilot, live, to the panel.
- **VTU closure.** Diary and report completed (format per the VTU backlog item).
- *Done when:* the panel signs off (or lists what's short); the demo is recorded; VTU paperwork done.

## What each intern walks away with

- A deployed, benchmarked, multimodal (if capstone) RAG agent, on a public GitHub repo.
- A benchmark report with real numbers.
- An ATS-ready résumé built from verifiable work.
- The vocabulary and the scars to talk about RAG, grounding, agents, evals, cost, and safety at an
  interview — because they built each one and watched it break first.

That is the difference between "I did an AI course" and "I shipped a scoped version of a real
system, benchmarked it, and here is the link."
