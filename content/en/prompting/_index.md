+++
title = 'Prompting'
description = 'The same model answers very differently depending on how you ask. Learn the building blocks of a clear prompt, techniques that work, and when prompting is not enough.'
[menu.main]
  name = 'Prompting'
  weight = 30
  url = '/en/prompting/'
+++

# Prompting

Wording is steering: a language model answers from the shape of your request, so a vague prompt invites a vague answer and a precise one lands closer to what you meant. Prompting is the cheapest way to get more from a model you already have — no retraining, no new tools, just clearer instructions.

Posts in this topic cover the anatomy of a good prompt (role, context, task, format, examples), the techniques that move answers most, and how to debug prompts like code.

## Where this fits

Prompting cannot add knowledge the model never had — that is what [RAG](/en/rag/) is for — and it cannot tell you whether answers are actually good, which is what [evals](/en/evals/) measure. Underneath both sits the [hallucination](/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it/) failure mode they are designed around.
