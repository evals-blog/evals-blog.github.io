+++
title = 'RAG'
description = 'A model only knows its training data. RAG lets it read your documents before answering — grounding answers, shrinking hallucination, and making AI useful for private or recent information.'
[menu.main]
  name = 'RAG'
  weight = 20
  url = '/en/rag/'
+++

# RAG

A model's knowledge is a frozen snapshot of public text. Your policies, product docs, and support tickets never got in — so a model asked about them answers from patterns, not facts. Retrieval-Augmented Generation (RAG) closes that gap: search your documents first, put the relevant passages in the prompt, then let the model write from what it read.

Posts in this topic cover the pipeline (ingest, retrieve, generate), a minimal code sketch, and the tuning levers that matter.

## Where this fits

RAG is the main answer to the [hallucination problem](/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it/) raised in this blog's first post. Combine it with [clear prompting](/en/prompting/) so the model follows your instructions, and keep an [eval](/en/evals/) loop so quality does not silently slip.
