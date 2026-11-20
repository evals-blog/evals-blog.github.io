---
title: 'What are AI agents? LLM vs AI agents'
description: 'An LLM answers one question; an AI agent pursues a goal across many steps. Learn what an agent is, the loop inside it, and when to use an LLM versus an agent.'
summary: 'An LLM takes a question and answers; an AI agent takes a goal, calls tools, and loops until the work is done. How the two differ — and when to use which.'
date: '2026-09-14T09:00:00+07:00'
draft: true
pinned: true
featuredImage: '/images/posts/en/daily-tips/what-are-ai-agents/cover.svg'
---

You open a chat window, type a question, and get an answer. That is an LLM. Then you hand over a whole task: “find the bug in this translation, fix it, rerun the checks, and open a pull request.” This time it does not just answer — it reads files, edits, runs commands, reads the errors, fixes again, and reports back when done. That is an AI agent.

The two are often lumped together, but they differ in one core way: **an LLM produces text; an agent pursues a goal.** This post separates the two, walks through the loop inside an agent, and explains when you actually need one.

![AI agents cover](/images/posts/en/daily-tips/what-are-ai-agents/cover.svg)

*Cover: an agent is one LLM plus tools and a loop.*

## What an LLM is

A large language model is trained on a huge amount of text to predict the next token. You give it text, it returns text. Every call is a single, independent turn.

Three properties matter:

- **One turn**: it takes a prompt, answers, and stops. To continue, you have to ask again.
- **No action**: it cannot open a file, call an API, or click a button. It only talks.
- **No memory by default**: the API does not store your conversation. The “memory” you see in a chat app is the app resending the history every time.

And because it predicts, an LLM can produce a fluent answer that is simply wrong — that is [hallucination](/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it/). The model is not checking facts; it is picking the most likely continuation.

## What an AI agent is

An AI agent is a system that uses an LLM as its brain and adds three things so it can *act*:

- **Tools**: web search, read and write files, run code, call APIs, query a database.
- **State and memory**: what the agent knows and has done — the plan, the result of each step, the files it changed.
- **A control loop**: the part that decides the next step, runs a tool, reads the result, and repeats until the goal is met or it is stopped.

Put differently: **an agent is the model plus a harness.** The model is still the LLM you already know; what is new is the scaffolding that lets it observe an environment and change it.

## The agent loop

Most agents revolve around one simple loop:

![Agent loop](/images/posts/en/daily-tips/what-are-ai-agents/agent-loop.svg)

*The agent repeats until the goal is met — or until a human stops it.*

Take the task “fix the broken build”:

1. **Goal**: the user says “the build is red, make it green.”
2. **Plan**: read the log, find the relevant file, guess the cause.
3. **Act**: run a command, open a file, change a line.
4. **Observe**: rerun the build, read the new error.
5. **Repeat**: if it is still broken, go back to planning; if it is green, report.

The key point: the path is not written in advance. The model decides the next step from the result it just observed.

## LLM vs AI agent

![LLM vs AI agent](/images/posts/en/daily-tips/what-are-ai-agents/llm-vs-agent.svg)

*Same model underneath, but one side only answers while the other acts and repeats.*

| Dimension | LLM | AI agent |
| --- | --- | --- |
| Input | A question, a prompt | A goal |
| Output | Text | Actions and results |
| Steps | One turn | Many steps, repeated |
| Tools | None | Yes (files, shell, APIs…) |
| State | Forgotten between turns | Kept across many steps |
| Your role | Ask each step | Assign the task, then supervise |
| Main risk | Saying something wrong | Saying *and* doing something wrong |
| How to measure | Score the answer | Score the answer + test the process |

The last row is the one that matters most. When an LLM only talks, a mistake costs a few minutes of reading. When an agent acts, the same mistake can delete the wrong file, send the wrong email, or spend real money.

## The line is blurry — and that is normal

“LLM or agent” is not two separate boxes; it is a spectrum of autonomy:

- A chatbot that only answers is a plain LLM.
- Adding web search or document retrieval (as in [RAG](/en/rag/rag-guide/)) is already a step toward acting.
- Letting it choose which tools to call, in what order, over how many steps — that is a real agent.

There is a very useful middle ground: a **workflow**. You write the steps in advance (extract → summarize → translate → validate), and each step is one model call. Workflows are cheaper, more stable, and easier to debug than a free-roaming agent. If the path is known ahead of time, use a workflow; reach for an agent only when the model must decide the next step itself.

## When to use which

- **Single-turn LLM**: writing, summarizing, classifying, answering, suggesting. Fast, cheap, predictable.
- **Workflow**: multi-step but fixed; you know the order.
- **Agent**: open-ended work with tools, where the path depends on each result — debugging, research, data investigation, operations.

A quick test: if you can write the procedure as fixed steps, you do not need an agent yet. If you find yourself describing *how to react to every possible situation*, that is a sign to let the agent decide.

## Some AI agents in use today

The list below is a set of anchors, not a ranking — this market changes monthly.

**Coding agents**

- **Claude Code** (Anthropic) — a terminal agent that reads the repo, edits files, runs tests, and checks its own work.
- **OpenAI Codex** — a coding agent that runs in the cloud or locally, built for long-horizon tasks.
- **Cursor (Agent Mode)** — an agent inside the IDE that makes multi-file changes.
- **GitHub Copilot (coding agent)** — an agent wired into pull requests and GitHub workflows.
- **Devin** (Cognition) — a bet on full autonomy: hand it a task and review the result.
- **Cline** and **Aider** — open source, bring your own model key.

**General-purpose and computer-use agents**

- **ChatGPT Agent / Operator** (OpenAI) — browses the web, fills forms, and works through multi-step tasks.
- **Claude with computer use** (Anthropic) — a model that drives a mouse, keyboard, and browser.
- **Gemini agents** (Google) — agents inside the Google ecosystem.
- **Microsoft Copilot agents** — agents inside Teams, Outlook, and SharePoint.

**Research and browsing agents**

- **OpenAI Deep Research** and **Gemini Deep Research** — search, read many sources, and write up a report.
- **Perplexity** — agent-style search with citations.
- **Browser Use** — an open-source library for building your own browser agent.

**Enterprise agents**

- **Salesforce Agentforce** and **ServiceNow AI Agents** — agents tied to internal workflows.
- **Sierra** and **Intercom Fin** — customer-support agents.
- **Microsoft Copilot Studio** and **Amazon Bedrock Agents** — platforms for building your own.

**Frameworks for building agents** — not off-the-shelf products, but worth knowing: **LangGraph** (LangChain), **CrewAI**, **Microsoft AutoGen**, **OpenAI Agents SDK**.

One thing to notice: almost every large vendor now calls its product an “agent.” So when you evaluate one, do not ask “is this really an agent?” Ask what the agent **is allowed to do, how many steps it decides on its own, and who stops it** — the same three questions from above.

## Agents fail too — and it costs more

An agent inherits every weakness of an LLM and multiplies it, because it has permission to act:

- Hallucination turns into **wrong action**: deleting the wrong file, editing the wrong place, calling the wrong API.
- Small errors can **compound** across steps.
- An agent can **loop forever** or drift away from the original goal.

So a few practical rules:

- **Least privilege**: grant only the tools and permissions the task truly needs.
- **Isolate the run**: sandboxes, a dedicated git branch, staging environments.
- **Gate the dangerous actions**: deleting data, sending externally, spending money — require human approval.
- **Log every step**: you need to know what it called and what it got back.
- **Measure with evals**: score not just the final answer but the process — see [LLM evals](/en/evals/llm-evals/).

And if you notice you keep handing the same repeatable procedure to an agent, package it as an [agent skill](/en/daily-tips/agent-skills/) so it runs consistently and versions like code.

## Key takeaways

- **An LLM produces text; an agent pursues a goal.** Same model, different answer to “can it act, and does it loop?”
- An agent is **model + tools + state + a control loop**.
- The basic loop: goal → plan → act → observe → repeat.
- If the path is fixed, use a **workflow** instead of a free-roaming agent — cheaper and easier to debug.
- Autonomy brings risk: least privilege, sandboxing, human gates on dangerous actions, and evals to measure it.
- Plenty of products carry the “agent” label: judge them by permissions and autonomy, not by the name.

**Read next:** [give your agent skills](/en/daily-tips/agent-skills/), [measure quality with LLM evals](/en/evals/llm-evals/), and [RAG in practice](/en/rag/rag-guide/).
