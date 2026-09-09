+++
title = 'LLM evals'
description = 'How to measure AI quality: build a small eval set, score answers the same way on every change, and catch regressions before your users do.'
[menu.main]
  name = 'LLM evals'
  weight = 40
  url = '/en/evals/'
+++

# LLM evals

Demos feel great and measure nothing: in production, users ask questions you did not pick, and models drift between versions. Evals fix that — a small set of representative cases, scored the same way every run, rerun whenever you change a prompt or a model. Feelings become numbers you can compare.

Posts in this topic cover what to measure, how to start small, simple scoring methods, and running evals as a regression loop.

## Where this fits

Evals are the last step of the practical loop this blog follows: understand why models [hallucinate](/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it/), [ground](/en/rag/) and [prompt](/en/prompting/) them well — then check that quality actually holds.
