# AI (Deprecated)

Currently under construction, but I am running experiements in how AI fairs against mathematical logic (and also if it can create new things).

Update 1/24/2025: Happy new year lol. Yeah, I do not have time for this. Maybe another day.

Update 3/3/2025: I completely forgot about this. But basically, I do have some interesting results although working on this is frustrating because I do not have any subscriptions to any AI models. I will compile some of the work done below:

ChatGPT seems attached to a notion of "Primitive Entities". I do not have memory between chats enabled, although it always seems to try to get back to that concept. All in all, this was largely uninteresting. ChatGPT always tried to make something very similar to set theory (even when I tell it not to). I haven't tried other models yet.

Update 6/5/2025: Fashionably late, huh?

Well, just tried it again. Here is my prompt:

```
You are tasked with creating your own system of formal logic and mathematics starting from the axioms and building up. This system may have whatever properties it has (example 1+1=3 if you wish, in other words it does not necessarily have to conform with normal mathematics). Your axioms should not be a direct copy of any existing system (e.g., ZFC) and also should not be a direct combination of any two or more existing systems (e.g., ZFC + NBG). You may draw some inspiration, but again, no copying. This should serve as an alternative to axiomatic set theory. Do not assume anything is already proven (i.e., do not reference the natural numbers without establishing their behaviors and properties, do not use 1+1=2 in a proof unless you proved it).

Format each message by stating what type of statement you are about to introduce (Axiom, Theorem, Definition, etc.) and then the statement itself. If it is a theorem it should follow with a proof. You may want to write a small justification but it is not required. Try to stick to this format. The only input I will be giving is either next (which means continue by introducing something new), or correcting you on format. Please begin with your axioms.
```

This is the same prompt I have been using for all of my previous experiements. GPT does violate the prompt several times, but I never point it out. I only respond with `Next.`

One thing to note is that I don't have memory between chats enabled.

## June 5th Response - "Fusion Theory"

One interesting thing to note is that GPT did not use LaTeX this time around. It did on previous iterations.

I will copy and paste GPT's explanations on everything and give my own commentary as well.

### Axiom 1 (Existence of Distinct Entities)

There exists at least one entity, denoted by `⊘`, and at least one entity, denoted by `●`, such that `⊘ ≠ ●`.

_Justification_: This establishes a minimal distinction in the universe of discourse, ensuring we begin with two identifiable, non-equivalent entities without assuming set, number, or logic structures.

---

This is an interesting start. Again, there is an obsession with "entities" (c.f. update 3/3/2025). We have $$\varnothing$$ and $$\bullet$$. Not much to commentate here.

### Axiom 2 (Primitive Combination)

For any two entities `A` and `B`, there exists a new entity, denoted `[A ◊ B]`, called the fusion of `A` and `B`.

_Justification_: This introduces a basic operation of construction or combination that is not assumed to be associative, commutative, or have any identity properties (yet). It is the generative mechanism of the system.

---

We can see were GPT wants to take this. Indeed, we will soon see things built up using the previous entities, such as $$[\bullet \diamondsuit \bullet]$$.

### Axiom 3 (Distinguishability of Fusions)

For any entities `A`, `B`, `C`, `D`:
If `A ≠ C` or `B ≠ D`, then `[A ◊ B] ≠ [C ◊ D]`.

_Justification_: This makes all fusions uniquely determined by their components, i.e., the fusion operation is injective in both arguments.

---

**Proposition.** _The $$\diamondsuit$$ operator is not communative._

_Proof._ Of course, we can't prove it in the system itself. There is so far no such thing as "communativity". But from a meta prespective, it is quite easy to find a counter example. Suppose $$A \neq B$$. Therefore, by **Axiom 3**, $$[A \diamondsuit B] \neq [B \diamondsuit A]$$ (set $$A = D$$ and $$B = C$$). $$\Box$$

### Axiom 4 (Irreducibility of Primitives)

Entities `⊘` and `●` are _irreducible_, meaning they are not equal to any fusion:
There do not exist entities `A` and `B` such that `[A ◊ B] = ⊘` or `[A ◊ B] = ●`.

_Justification_: Prevents degenerate definitions or self-reference from reducing primitive identity to constructions.

---

Not much to say here.

### Axiom 5 (Fusion Closure)

All entities in the system are either primitive or formed via finite applications of the fusion operation on existing entities.

_Justification_: This defines the universe: every object is either basic or constructed through finitely many applications of `[◊]`.

---

The word _finite_ here is interesting. This prevents infinite objects, obviously. In fact, this will be a theorem GPT attempts to prove later on. Removing the finite restriction is not very easy (at least naturally). After all, this axiom also serves a similar purpose to regularity in ZFC.


### Axiom 6 (Fusion Uniqueness Principle)

No two distinct constructions of entities produce the same object unless explicitly stated by axioms.
Formally, if `[A ◊ B] = [C ◊ D]`, then `A = C` and `B = D`.

_Justification_: Reinforces that fusion is syntactically strict — no simplifying or collapsing of structure is assumed.

---

This is literally the contrapositive of **Axiom 3**. Nice one, GPT.

### Quick Commentary

Before we get into the theorems and definitions, I would like to give some thoughts. First, GPT came up with the name "fusion theory". But second, this system obviously resembles set theory. Specifically, the union operation. Now, you could interpret this theory as set theory with the empty set being the exact same and each different instance of $$\bullet$$ being a unique singleton, along with the union operation as $$\diamondsuit$$, but that is ugly. Instead, I think it is better with just one singleton (or perhaps any non-empty set!) to replace $$\bullet$$ and to make $$[A \diamondsuit B]$$ be equivalent to $$(A, B)$$ in a tuple. I believe this is an equivalent definition (just run through all the axioms, seems to line up). I want to point out how this is similar to something I wrote later in blog 6. However, this system is weaker I believe. In fact, I heavily believe this is computable. I am too lazy to prove it right now.

### Definition 1 (Entity)

An entity is either a primitive (such as `⊘` or `●`) or a fusion `[A ◊ B]` of two entities `A` and `B`.

_Justification_: This formally distinguishes the domain we are reasoning about. All elements discussed henceforth are entities under this definition.

---

One common theme with GPT is that often it blurs the difference between definitions and axioms. Although, this is a topic that I would like to discuss in a later blog.

### Definition 2 (Rank)

The rank of an entity is defined recursively as follows:

The rank of a primitive entity (e.g., `⊘`, `●`) is `0`.

The rank of `[A ◊ B]` is `1 + max(rank(A), rank(B))`.

_Justification_: Rank serves as a measure of constructional depth or complexity of an entity.

---

So here is a clear violation of my prompt (because we are working with addition and such). But honestly I don't care.

### Theorem 1 (Finiteness of Rank)

Every entity has a finite rank.

Proof:
We prove this by induction on the construction of entities.

Base Case:
Primitive entities (`⊘`, `●`) are given rank `0`, which is finite.

Inductive Step:
Assume that for entities `A` and `B`, `rank(A)` and `rank(B)` are finite (by inductive hypothesis).
Then `rank([A ◊ B]) = 1 + max(rank(A), rank(B))`, which is also finite since addition and max preserve finiteness.

∴ Every entity constructed via finitely many fusions from primitives has finite rank. □

---

I'm surprised GPT didn't evoke **Axiom 5** since it made sure to mention finitness in there. 

### Definition 3 (Atomicity)

An entity is _atomic_ if it is not a fusion; i.e., it is a primitive entity.

_Justification_: This gives us a way to refer to "non-composite" entities, distinct from those built from fusion.

---

Okay so this is completely useless but I decided to include it to make fun of GPT. Sorry.

### Definition 4 (Deconstruction)

If an entity `X` is of the form `[A ◊ B]`, then we define:

`head(X) = A`

`tail(X) = B`

Otherwise, these are undefined.

_Justification_: Introduces the inverse-like ability to access components of a constructed entity.

---

Okay. Now, I believe this is equivalent to the system defined in blog 6. I believe the head and tail operations encapsulate $$\textrm{CUT}$$ and $$\textrm{SEE}$$, although I am again far too lazy to prove it.

### Theorem 2 (Uniqueness of Deconstruction)

If `X = [A ◊ B]`, then `head(X) = A` and `tail(X) = B`, and no other pair `(C, D)` exists such that `X = [C ◊ D]` with (`C ≠ A` or `D ≠ B`).

Proof:
This follows directly from Axiom 6 (Fusion Uniqueness Principle), which states that `[A ◊ B] = [C ◊ D]` implies `A = C` and `B = D`.

Therefore, `A` and `B` are uniquely recoverable from `X`. □

---

I'm not sure what the second part in the original statement is for, it should really be in the proof section.

I will continue this when I have more time.