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
This system answers questions pertaining to the `city_guides corpus`. The corpus contains a set of documents introducing specific towns and cities (along with things to do, how to visit, dining options, etc.); overall guides on accessibility, eating, transit, and walking; as well as a breakdown of when to visit based on the seasons. This system is designed to answer clear and direct questions regarding those topics. 

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
| 1. Retrieved chunks contain the answer | 4/5 | 0/5 | 0/5 | 0/5 | MISSED |
| 2. Every answer names a source | 5/5 |4/5 | 5/5 | 5/5 | MISSED |
| 3. The relevance gate stops out-of-corpus questions | 4/5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Each retrieved chunk is no longer than 500 characters in length | 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Each answer attributes the chunk containing the answer to the correct document sources | 5/5 | 3/5 | 4/5 | 4/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### CRITERION 1: Retrieved chunks contain the answer

#### How often is there a train to the airport from Brightwater? — run 1

- Best distance: 0.1833 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

```
I do not have enough information to answer how often a train runs to the airport from Brightwater. 

(Source: guide_marchwood.md, guide_kestrelford.md, guide_thornby_wells.md, guide_pellew_sands.md, guide_accessibility.md)
```

Taken from the run log generated by ```run_eval.py --label before```; text produced as the `main` function of the file. According to my scoring method, this chunk does not contain the answer.

### CRITERION 2: Every answer names a source

#### I am in a wheelchair. Which towns should I not visit? — run 1

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_walking.md

```
Based on the provided documents, there is no mention of which towns you should *not* visit. Therefore, I do not have enough information to answer this question.
```

Taken from the run log generated by ```run_eval.py --label before```; text produced as the `main` function of the file. My criterion states that every answer cites a source. This answer, from run 1, fails to do so; thus it does not pass this criterion.

### CRITERION 3: The relevance gate stops out-of-corpus questions

#### The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.65. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.805 | refused |
| How do I change the oil in a diesel engine? | 0.876 | refused |
| Who won the 1994 World Cup? | 0.967 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.849 | refused |
| How do I write a for loop in Rust? | 0.859 | refused |

Taken from the run log generated by ```run_eval.py --label before```; text produced as a result of the `check_out_of_scope` function of the file. This criterion states that out-of-scope questions must be refused at the gate, which they have been.

### CRITERION 4: Each retrieved chunk is no longer than 500 characters in length

#### During which season are there the least amount of students in town? — run 1

- Best distance: 0.5109 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_kestrelford.md, guide_pellew_sands.md, guide_seasons.md

```
May and June are the best months because the students are largely gone (*guide_brightwater.md*). Additionally, July and August are quiet in Brightwater because the university is empty (*guide_seasons.md*).
```

Taken from the run log generated by ```run_eval.py --label before```; text produced as the `main` function of the file. This answer, from run 1, lies inder the 500 character limit that this criterion calls for. All the other answers also fall under this limit.


### CRITERION 5: Each answer attributes the chunk containing the answer to the correct document sources

#### How often is there a train to the airport from Brightwater? — run 1

- Best distance: 0.1833 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

```
I do not have enough information to answer how often a train runs to the airport from Brightwater. 

(Source: guide_marchwood.md, guide_kestrelford.md, guide_thornby_wells.md, guide_pellew_sands.md, guide_accessibility.md)
```

Taken from the run log generated by ```run_eval.py --label before```; text produced as the `main` function of the file. This answer, from run 1, doesn't cite the correct source, which would be `guide_brightwater.md`, violating this criterion.


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MISSED | According to my scoring/answer judging function, none of the produced answers contained the exact phrase that I set to be expected as the answer, so they were marked incorrect. However, many of the answers do contain the correct answer, if phrased differently. I will likely have to rework my judging/scoring function. |
| 2 | Every answer names a source | MISSED | One of the produced reponses does not contain a source (question 4 run 1). Albeit, the reponse is a non-answer; but across other runs, a source was still cited for all non-answers, indicating where at least the system looked. It did not do the same in this case, so I consider this criterion missed. |
| 3 | The relevance gate stops out-of-corpus questions | MET | All out of corpus questions were stopped at the relevance gates. |
| 4 | Each retrieved chunk is no longer than 500 characters in length | MET | All retrieved chunks and answers across all three runs and all 5 questions were less than 500 characters in length. |
| 5 | Each answer attributes the chunk containing the answer to the correct document sources | MISSED | There were responses given that did not have a source cited, as well as responses that were missing the correct source. Every run of Question 1 should have cited `guide_brightwater.md`, but did not. |

<!-- 
claude response wrt argue in the opposite:
Criterion 1 — MET (not missed)
The top table's all-"fail" grid is a red flag against itself, not evidence: 15 cells, uniformly "fail," identical across all three runs for every question — a pattern that never varies is a placeholder that was never actually filled in, not a genuine finding. The file's own header tells you to derive the real per-criterion verdict from the "Real output" section, not from that grid.

Looking at actual output: Q2 (seafood) — chunk from guide_eating.md/guide_halden_bay.md directly contains the answer, all 3 runs. Q3 (season) — chunks from guide_brightwater.md and guide_seasons.md directly contain the answer, all 3 runs. Q5 (museums) — chunks from guide_marchwood.md/guide_brightwater.md directly contain the answer, all 3 runs. That's already 3/5 with dead-certain hits.

Q1 (train to airport) clinches the 4th: its best distance is 0.1833 — the lowest of any question in the entire run, lower even than the three confirmed hits above (0.41–0.51). By the system's own scoring, this is its strongest topical match of the day. A distance that tight is not consistent with "irrelevant chunks retrieved" — it indicates the retriever found highly on-topic material. The refusal came from the generation step declining to commit to an answer, which is a generation-layer failure, not a retrieval-layer one. Criterion 1 asks only whether the retrieved chunks contain the answer — it says nothing about whether the generator used them. Read strictly, this is a pass for retrieval even though the final text says otherwise.

That's 4/5 — target met.

Criterion 2 — MET (not missed)
Only one cell in the entire 15-answer run lacks an explicit "Sources:" line: Q4, run 1 ("Based on the provided documents, there is no mention... Therefore, I do not have enough information to answer this."). Every other answer — including every other refusal (Q1, all 3 runs, still lists 5 sources) — names sources.

But look at what Q4-run1 actually is: a refusal. The criterion's own stated reasoning is "every answer the system produces names at least one source" — a refusal is not an answer, it's an explicit non-answer. If you restrict the denominator to substantive answers (the only place attribution is meaningful), compliance is 100%: 12/12 substantive answers across all 5 questions name a source every time. The one gap sits entirely inside a category the criterion isn't measuring.

Criterion 3 — MISSED (not met)
The 5/5 refusal rate on the official out-of-scope list (Mongolia, diesel oil changes, 1994 World Cup, ibuprofen dosage, Rust for-loops) is a hollow win — those are wildly off-topic across every axis (domain, register, vocabulary). Discriminating them from travel guides is the easiest possible version of this task; a bag-of-words filter would pass it.

The real test of "stops out-of-corpus questions" is a question that's topically in-domain but not actually covered — and Q1 is exactly that. Its retrieved sources never include guide_brightwater.md at all, and the system itself concludes three times over that it has no information. That is an out-of-corpus question in every practical sense. Yet its best distance (0.1833) sailed through the 0.65 cutoff with the widest margin of any question in the run — closer than every confirmed in-corpus hit. The gate didn't stop it; the generator had to catch what the gate missed. That's the gate failing at its one job on the one case that actually mattered, papered over by an easy 5-for-5 on questions it was never going to get wrong.

Criterion 4 — MISSED (not met)
There is no measurement of chunk length anywhere in this file. Not one chunk's character count, not one raw chunk excerpt — only document names under "Sources retrieved." The target reasoning ("chunks... max out around 500 characters... by paragraph design") is a claim about the chunker's intent, not a verification of its output on this run. An acceptance criterion that requires empirical confirmation cannot be marked met on the basis of "the chunker was designed to do this" — that's arguing from spec, not from evidence. Nothing in run_2026-09-27_2153_before.md demonstrates this criterion was checked at all, so it cannot be scored as met from this artifact.

Criterion 5 — MET (not met)
Every single substantive answer in the file cites the exact document its content came from, with zero exceptions: seafood → guide_eating.md/guide_halden_bay.md (correct, 3/3 runs); season → guide_brightwater.md/guide_seasons.md (correct, 3/3 runs); museums → guide_marchwood.md/guide_brightwater.md (correct, 3/3 runs); and even Q4-run2's tangential answer about Thornby Wells correctly cites guide_accessibility.md/guide_walking.md. Across every case where there was a claim to attribute, the attribution was right. Twelve for twelve, no misattributions anywhere in the log — that's about as clean a pass as this criterion can produce.

Caveat, dropping the advocate hat: you asked for the strongest opposite case, and the Q1-distance argument for criteria 1/3 is the weakest link in it — it treats "low retrieval distance" as proof the chunk contains a train-schedule answer that the model then withheld, when the more natural reading is that 0.18 reflects strong lexical overlap on "Brightwater" without the specific fact being present at all. Your original verdict leaned on that same reading.

-->

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

**Criterion 1:** Retrieved chunks contain the answer 

Criterion 1 says that retrieved chunks should have an answer. Manually reading or checking the output would tell you that the retrieved chunks do have the correct answer (except for Question 1 and 4), but they are flagged as incorrect by the scoring function. This tells me I should fix my scoring function, that the way the answers are judges are incorrect. The error in this case doesn't lie in the answer generation pipeline stages, but in the scoring.

That said, in the case of Questions 1 and 4, the pipeline system wasn't able to generate an answer. I was looking for answer that takes the absence of information to be a negative. For example, Question 1 asks about the train to the airport in Brightwater; `guide_brightwater.md` states that there is no airport, therefore, there should also be no train. I believe this error lies in the embedding part of the pipeline as it wasn't able to make the connection between 'no airport' to 'no trains to the aiport'. 

**Criterion 2:** Every answer names a source

The answer given in Question 4 Run 1 (the one question-run that missed this criterion) is a non-answer; it states that there isn't enough information and doesn't ultimately cite the sources it looked in. In contrary, the looked-in sources were give in Run 2 and 3. The error in this case lies in the last part of the pipeline, the answer generation. 

**Criterion 5:** Each answer attributes the chunk containing the answer to the correct document sources

The response to Question 1 across all 3 runs provide sources, but fail to cite `guide_brightwater.md`, which should be one of the cited sources, as the question is about Brightwater. This is an error that comes from the retrieval step. 


## The Improvement

**What I changed:**

I chose to update my scoring function from the basic one given in class.

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

This is connected to Criterion 1. retrieved chunks contain the answer. In several of the previous reponses, the answer was correctly given, but phrased slightly differently. I reworked my scoring function to check if correct keywords were given in the generated answer instead of just checking to see if the exact phrase was in there. 

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4/5 | 2/5 | 2/5 | 2/5 | MISSED |
| 2. Every answer names a source | 5/5 |3/5 | 4/5 | 4/5 | MISSED |
| 3. The relevance gate stops out-of-corpus questions | 4/5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Each retrieved chunk is no longer than 500 characters in length | 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Each answer attributes the chunk containing the answer to the correct document sources | 5/5 | 3/5 | 3/5 | 3/5 | MISSED |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Modifying the scoring function this way allowed this system to more accurately judge if the answer was correct, which it was in roughly half the questions/runs. In other answers, the scoring function wasn't able to distinguish between a general concept and a specific one. For example, most people would consider "July and August" and "summer" to be the same when referring to seasons. However, my question expected the phrase "summer" and the answer used "July and August", thus, this generated answer was considered incorrect. 

There were also two questions that would take the absense of information as information itself; i.e. if it wasn't explicitly mentioned, the reader would assume they don't exist. It seems the model isn't capable of that type of logic. This is a misunderstanding and poor assumption on my part when I created the questions. In order to test the pipeline as it was designed, I would have to rephrase these questions and answers to have explicit references in the given corpus. 

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
