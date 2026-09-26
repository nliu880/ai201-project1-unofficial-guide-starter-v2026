# The Unofficial Guide

Nicole Liu; city_guides 
<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
     This system answers questions pertaining to the ```city_guides corpus```. The corpus contains a set of documents introducing specific towns and cities (along with things to do, how to visit, dining options, etc.); overall guides on accessibility, eating, transit, and walking; as well as a breakdown of when to visit based on the seasons. This system is designed to answer clear and direct questions regarding those topics. 

## Chunking Strategy

**Chunk size:**
The current default chunking for this corpus splits documents through labeled sections, with an average of 650 characters per chunk. I would like my chunks to by paragraph as each paragraph introduces new information. 

<!--For simpler yes/no/single answer questions, the chunk should be 50-250 characters. Questions that draw from multiple documents, or have multiple answers, should have longer chunks (~500 characters total). -->

**Overlap:**
My chunks will not overlap. All information in my corpus is organized in individual paragraphs by topic, so there is no need to worry that each topic is split unevenly across chunks.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

#### ======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
#### ======================================================================
**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

#### ======================================================================
Chunk 2  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
#### ======================================================================
**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute walk from campus on flat ground, or the
shuttle meets the four busiest arrivals.

#### ======================================================================
Chunk 3  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
#### ======================================================================
**Givens Mill** is one flat street along the river. The mill tour involves
stairs and the machinery floor is not accessible; the tearoom and riverside are.

#### ======================================================================
Chunk 4  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
#### ======================================================================
**Halden Bay** is built on three levels connected by stepped lanes. The harbour
front is level; everything above it is not. This is hard going with luggage or a
pushchair, let alone a wheelchair.

#### ======================================================================
Chunk 5  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
#### ======================================================================
The nearest full hospital is in Marchwood. Brightwater has a hospital;
Kestrelford, Halden Bay, Corry Vale, Givens Mill and Elder Ness have minor
injuries units with limited hours or nothing at all.

<!-- **Chunk 1** — source: `` — produced by: ``

```
```

**Chunk 2** — source: `` — produced by: ``

```
```

**Chunk 3** — source: `` — produced by: ``

```
```

**Chunk 4** — source: `` — produced by: ``

```
```

**Chunk 5** — source: `` — produced by: ``

```
```
-->

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
Where should I go to get fresh seafood?

**Answer:**
```
To get fresh seafood, you should go to Halden Bay's two harbour restaurants, which buy directly from boats that land in the early morning (*guide_eating.md* and *guide_halden_bay.md*).

Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_pellew_sands.md
```

**My relevance cutoff:**

My test questions had best distances between 0.183 and 0.511. The out of scope questions had best distances above 0.805. I will set my relevance cutoff at 0.65, which is halfway between the upper best distance of my in corpus questions and the lower best distance of my out of corpus questions. 

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| How often is there a train to the airport from Brightwater? | Yes | 0.183 |
| Where should I go to get fresh seafood? | Yes | 0.411 |
| During which season are there the least amount of students in town? | Yes | 0.511 |
| I am in a wheelchair. Which towns should I not visit? | Yes | 0.495 |
| Which cities have museums open to visit? | Yes | 0.430 |
| What is the capital of Mongolia? | No | 0.805 |
| How do I change the oil in a diesel engine? | No | 0.876 |
| Who won the 1994 World Cup? | No | 0.967 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.849 |
| How do I write a for loop in Rust? | No | 0.859 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I completed this project on my own as I joined the class late. I used Claude in place of breakout room partners as suggested by the project guidelines. I would give Claude the answer criteria, a sample of chunks, and the distances, along with the question statements. Based on the response given to my chunk samples (asking if a question could be answered by it), I reworked my chunking function to skip past the initial document introduction/description in one of the documents as it was meta information and not related to the actual material in the corpus. 

**2.**
In Milestone 4, I gave the best distances to Claude without the ensuing context. Based on the previous exchange of information, Claude suspected that the lower set of numbers were out of corpus and the higher set in corpus. Giving the context and asking about a cutoff gave a response more along the lines of what I was expecting, along with excess warnings about small sample sizes and lack of more ambiguous or poorly worded questions. I had initially proposed a cutoff point between the upper best distance of my in corpus questions and the lower best distance of my out of corpus questions (0.65), which was also suggested by Claude. I did not change my cutoff point after this. 

I did not use AI otherwise in this project. I wrote my chunking function myself and determined my own criteria, reasoning behind it, and questions pertaining to the corpus material. 

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
