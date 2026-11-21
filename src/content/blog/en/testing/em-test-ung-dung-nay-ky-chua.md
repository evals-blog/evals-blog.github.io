---
title: 'Have you tested this app thoroughly? Years later, I understand this question is a career in itself'
description: 'My teacher asked if I had tested the app thoroughly. I said yes. Years later I understand: answering that question is not the work of an afternoon — it is the work of a career.'
summary: 'My teacher asked if I had tested the app thoroughly. I said yes. He asked if I had tested every case. I said yes again. Seven years later I understand what was wrong with that answer.'
date: '2026-11-21T09:00:00+07:00'
draft: false
tags:
  - 'testing'
---

During my graduation thesis defence in 2019, a member of the panel asked a question I took for a side note:

"Have you tested this app thoroughly?"

I answered without thinking: "Yes — I ran every feature. Create, edit, delete, search all work."

He did not nod. He asked again: "Have you tested every case?"

I said yes again.

I can still hear how confident that voice was — smooth, quick, and completely unaware of what it was saying.

## Seven years later

On Vietnamese Teachers' Day (20/11), I found myself back in that room. What stays with me is not the wrong answer; it is the confidence in it. I said "yes" to a question that nobody who has done this work for long would answer with "yes": *Have you tested every case?*

"Every case" is not a list. It is an almost infinite set: every string a user can type, every order of actions, every network state, every time zone, every moment when two people click at once. Nobody tests all of it. People who have done the work do not say "I tested everything"; they say: "I tested these. I did not test those. Here is why I still dare to hand it over."

Seven years ago I could not tell those two answers apart. Now I can, and I am grateful he asked. The question was not a trap. It is the question I have to ask myself every time I hand something over.

## Testing is an art

"Art" here is not decoration. It is three hard decisions, repeated every day:

- Choosing what deserves a test, when there is no time for everything.
- Writing the expected result *before* running anything, so I cannot fool myself with "well, it ran".
- Reading a red test and understanding what it is telling me — about the code, about an assumption, or about the requirement itself.

A test is a test only when I know, in advance, what the right result is. "I clicked the button and the screen changed" is observation, not testing. Testing needs three things, written down before you run: a starting condition, an action, and an expected result.

Without an expected result I can say "it still runs", never "it is correct". And "still runs" describes every application whose bugs have not been found yet — including the ones quietly losing user data.

## What a decent test case looks like

A good test case reads clearly and can be re-run by someone else without asking me anything. For a sign-up feature:

- New email, valid password → account is created and can log in immediately.
- Email already exists → a clear error, and **no** second record is created.
- Password under 8 characters → rejected, with a specific reason.
- Network drops mid-request → no half-created account is left behind.
- Submit pressed twice in a row → exactly one account exists.

Note the second one: verifying that a record is **not** created matters as much as verifying that it is. Most serious bugs live on that side, and that is precisely the side an afternoon of happy-path clicking skips.

## Test by risk, not by count

You cannot test everything evenly — there is no time, and no need. Ask instead: if this breaks, what is the damage? A payment off by one unit, lost data, leaked personal information, or a heading that is slightly misaligned? The answer tells you where to spend effort.

Coverage numbers are useful for spotting code nobody has executed, but they say nothing about whether you tested the parts that matter. Eighty percent coverage concentrated on decorative helpers is eighty percent wasted.

## Bugs live at the edges

Bugs rarely sit in the middle of a range. They sit at the edges:

- an empty list, a one-item list, a very long list;
- an empty string, a 10,000-character string, emoji, Vietnamese diacritics, `<` and `&`;
- zero, negative numbers, very large numbers, decimals;
- two people editing the same record at once;
- time zones, daylight saving, and exactly midnight.

If I have not tried these, I do not know what my application does. I only know what it does under the friendliest possible conditions — which are rarely the conditions real users are in.

## Three layers, three questions

Not everything deserves the same kind of test:

- **Unit** — is the plain logic correct? Fast, cheap, thousands of them in seconds. Write most of your tests here.
- **Integration** — do the pieces hold together against the real world? Database, external APIs, queues, permissions, clock. This is where things break most.
- **End-to-end** — can a real user complete a whole flow? Expensive, slow, prone to flaking, so reserve it for a couple of critical journeys.

The common beginner error — mine, seven years ago — is having only one of the two extremes: a few unit tests that make the coverage number look healthy, or manual clicking from start to finish labelled as testing.

## The age of AI agents: code got cheap, verification got expensive

Seven years ago I typed every line myself, so I trusted the code because I had written it. Now part of the code is written by AI in seconds, and I have no reason to trust it merely because it exists.

An agent can generate tests, run them, and fix the code until they pass. But it does not know what "correct" means on my behalf. If I cannot say what right looks like, the agent will write a test that checks the thing it just built — and the two of us will agree that everything is fine.

As the speed of writing code goes up, verification becomes the thing that decides quality. The question has not aged: it has become harder to answer, because the number of cases grows faster than the number of tests I can write. Which is why the age of AI agents is, more than ever, the age of testing.

## The checklist I answer before handing anything over

Before submitting, before a demo, before saying "done":

- Every requirement has at least one test case, with the expected result written down rather than kept in my head.
- I have tried invalid data, empty data, and very large data.
- I have tried two actions at once, and pressing submit twice.
- Error messages tell the user what to do and never leak a stack trace.
- The tests run on someone else's machine, not just mine.
- I know exactly what is untested, and why that is acceptable.

## The answer I owe him

If I meet that teacher again, I will not say "yes" this time.

I will say: "Here is what I tested. Here is what I did not test. Here is the risk that remains — and I dare to hand this over because I know exactly what it is."

That is the answer of someone who does this work, not of a student afraid of a hard question. It took seven years to be able to give it. Still in time — and I still hear the question every time I press the button that ships something.
