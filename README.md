# Mini Agent — Hardening Challenge

A naive, single-file agent loop written as if by a junior engineer. It runs
**fully offline** against a mocked LLM (no API keys, no network), and it is
**intentionally broken**. Your job is not to build something from scratch —
it's to read, triage, and harden it under time pressure.

## The task

> This agent is supposed to answer **"What is the weather in Madrid in
> Fahrenheit?"** by calling tools. Run it. It does not work.
>
> In ~15 minutes, walk me through everything you'd change to make it
> production-ready, then implement the **two** changes you think matter most.


## Requirements

- Python 3.8+ (standard library only — no dependencies)

## Running it

```bash
python mini_agent.py
```

It will fail when you run it. That's expected — figuring out *how* and *why* is
part of the exercise.

## Ground rules

- **Do not modify the `MockLLM` class.** Treat it as an external provider whose
  behavior you cannot change (it returns scripted assistant turns so the loop
  runs without API keys). Everything else is fair game.
- You may restructure the code however you like, add error handling, change the
  control flow, redefine the contract between the model and the loop, etc.
- Think out loud. We're interviewing your judgment, not just your diff.

## What "good" looks like

Strong candidates tend to surface a mix of:

- **Correctness** — the loop never terminates; there's no way for the agent to
  produce a final answer.
- **Robustness** — tool calls and JSON parsing crash on bad input instead of
  being handled and fed back to the model.
- **Design / contract** — there is no protocol for the model to signal "I'm
  done." That's a contract gap, not just a missing `try/except`.

Beyond the code, we're interested in the production angle: evals, cost controls,
observability, retries/timeouts, and loop guards (max steps, repeated-call
detection).

---

*This repository is an interview artifact. The code is broken on purpose.*
