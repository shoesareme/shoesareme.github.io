---
layout: github
title: LEAN Notes
---

# Notes on LEAN

> Version: 3
>
> Notes are by Jason Zhang. This follow's Euler Circle's LEAN class. 
>
> Most code seen in here is directly from the lecture code examples, unless otherwise indicated.
>
> Please note that these are my own personal notes; I may choose to gloss over a topic if I am already familiar with it. Likewise, I might choose to go even deeper on a certain topic than said in class if I think it is relevant to the discussion.

## Lecture 0 - Preface

The topics this course will cover mostly concerns how LEAN works and how it can be used in mathematics. More or less, we will not be covering any new mathematical content. We may go over specific foundations concepts related to LEAN, but the majority of these lectures will be on using LEAN itself to go over fairly simple concepts (e.g., calculus, analysis, etc.).

To start, we can re-interpret our regular conception of logic. We equip each proposition $P$ as either $\top$ or $\bot$ (true and false respectively). But, we say that $\top$ corresponds to *provable* (ignore Gödel for a second). Then, we can say the following about the logical connectives:

- $A \vee B \equiv A \textrm{ is provable or } B \textrm{ is provable.}$ 
- $A \wedge B \equiv A \textrm{ is provable and } B \textrm{ is provable.}$ 
- $A \rightarrow B \equiv B \textrm{ is provable whenever } A \textrm{ is provable.}$ 
- $\neg A \equiv A \rightarrow \bot$.

Notice how we are already inching towards something similar to the BHK-interpretation. Regardless, we are getting ahead of ourselves. We can use formal logic to do a lot of things. For one example, see the Natural Number Game.

## Lecture 1 - Logic Background

Consider the folowing theorem:

**Theorem.** For all $n \in \mathbb{N}$, $n \cdot S(0) = n$.

How are we going to go about this in LEAN? Observe the following syntax:

```lean 
import Std

theorem example1 (n : Nat) : n * Nat.succ 0 = n := by 
    rw [Nat.mul_succ]
    rw[Nat.mul_zero]
    sorry
```

The name for this theorem is `example1`. The statement `n : Nat` declares that `n` is of type `Nat` (which we would write as $\mathbb{N}$). Now, `Nat` is able to grant us `Nat.succ` for free as it is part of an import (specifically, it comes from `import Std`). The `rw` command simply rewrites any instance of the goal statement with the structure given by what is in the brackets. 

Consider `rw [Nat.mul_succ]`. Using the command `#check Nat.mul_succ`, we are able to see what it says. LEAN tells us that is says `∀ (n m : Nat), n * m.succ = n * m + n`. In mathematical notation, that is $n \cdot S(m) = n \cdot m + n$. Notice that if we plug in $n=n$ and $m=0$, we would get $n \cdot S(0)$ which is our current situation. That is what `rw` does, it plugs in according to the rules. So, it would transform `n * Nat.succ 0 = n` to `n * 0 + n = n`. The next command `rw [Nat.mul_zero]` rewrites it to `0 + n = n`. This is not one of the Peano Axioms we assumed, so we might be a bit suck here. If we can't figure it out for now, we will just use `sorry` to mean that we don't have the solution yet. One should go through the Natural Number Game to be more familiar with basic commands such as `exact`, `induction`, etc. 

## Lecture 2 - Type Theory

LEAN is founded on (CoC / Dependent) Type Theory. This is slightly different than set theory for very subtle and foundational reasons. One of the distinctions is that computers generally show an aversion towards sets (although it is possible!). The reason why computers tend towards type theory is that type theory is a fundamentally computer science theory in the sense that typed $\lambda$-calculi are literally models of computation. Also, "data types" from your average AP CS course is literally

In type theory, we would write $x : X$ to mean something similar to $x \in X$. Notice the notation for writing a function: $f : \mathbb{R} \rightarrow \mathbb{R}$. We are already using type theory notation! This also means that $\mathbb{R} \rightarrow \mathbb{R}$ is a type, which it is, although this will be elaborated upon later.

Types arise by rules. These rules define which terms (which is the equivalent for element) are in the type, and when terms are equal. There is additional "data" given by each type. Consider the set $X=\lbrace1\rbrace$. This set $X$ can also be defined by $X=\lbracex \in \mathbb{R} : (x-1)^{2}=0\rbrace$. Indeed, in set theory, there isn't a distinction to be made here. The $x$ for which $(x-1)^{2} = 0$ is just $x=1$. But, from intuition, we know the second definition of $X$ gave us some more information. We know a bit more about the "context" surrounding $X$, there are infintely many ways to define the set $\lbrace1\rbrace$ including the trivial and solution way we just discussed. But we seemingly know a bit more about $X$ when we define it as the solutions to some set. This is the distinction that type theory grants upon us.

Type theory is also equipped with regular set theoretic tools, just under a different name (sometimes). Instead of unions, we have sum types notated $X+Y$. We also have product types, $X \times Y$, which does something analogous to the cartesian product in set theory.

We will define some more general types. Let $X$, $Y$ be types. Then,

1. The product and sum types $X \times Y$ and $X + Y$.
2. There is a type $X \rightarrow Y$ which is the type of all functions $X$ to $Y$.
3. There is a type $\varnothing$ or $\bot$ which is the empty type.
4. The unit type $\top$ or $\mathrm{Unit}$ which has just one term (akin to the singleton set from set theory). This term is usually written as $\star$.

Wait a minute! $\top$? $\bot$? Aren't these the logical symbols for true and false? Great observation! In fact, an excellent observation. This is because these two different systems actually do correspond. This is the famous Curry-Howard Isomorphism. 

Back to set theory for a moment, ever notice how $\cap$ and $\cup$ behave sort of like $\wedge$ and $\vee$? I mean, the symbols even look alike! Well, there is a good reason for this that I will not be elaborating on. But, the similarity is even stronger in type theory. This is because, it isn't just a "similarity". It is an entire correspodence.

**Curry-Howard Correspondence.** Propositions are types, proofs are terms. This gives rise to the idea that mathematical proofs are programs.

| Type Theory (Computation Side) | Propositional Logic (Logical Side) | 
| -------- | -------- | 
| Type $A$ | Logical Formula / Proposition $A$ | 
| Term $a : A$ | Proof where $a$ certifies $A$ is true | 
| Unit Type | True | 
| Empty Type | False | 
| Function Type $X \rightarrow Y$ | If $X$ then $Y$ | 
| $X + Y$ | $X$ or $Y$ | 
| $X \times Y$ | $X$ and $Y$ | 

This can be extended beyond propositional logic to predicate logic where we can add in $\forall$ and $\exists$. Each of these also have corresponding things in type theory, although it is a bit more complicated. In type theory, we can truly think of everything as a type! Note that even though I said type theory was the "computational side", general computation would not be recognized as proofs. Consider the program that runs infinitely and never stops. What would this be equivalent in for a proof? Well, it would be a terrible proof since it would go on forever with no way of knowing whether the proof is correct or not. For this reason, LEAN is NOT Turing-Complete as that would mess everything up. Likewise, most people also accept a less radical version of Curry-Howard being "propositions as **some** types", where not every type is a proposition. This is not all too important though. 

There is another similar perspective to Curry-Howard called the BHK or realizability interpretation (although Curry-Howard and BHK are subtly different for technical reasons). However, BHK gives us more motivation/intuition on how computation and logic correspond to each other. Think about the function type $X \rightarrow Y$. Consider $x : X$ which again is a proof that $X$ is true. The function type $X \rightarrow Y$ would give us a function $f : X \rightarrow Y$ where $f(x) : Y$, which is a proof $Y$ is true. So, $f : X \rightarrow Y$ actually gives us a way to turn proofs of $X$ into proofs that $Y$ are true, which makes sense considering $f$ is supposed to be a proof that $X \rightarrow Y$ is true. 

It should be noted that if you accept the full complete "proposition as types", then most types are boring. For example, if you insist all types are propositions, then $\mathbb{N}$ is the proposition saying "there exists a natural number." Not very interesting in my opinion. 

The reason we discussed all of this is that this is how LEAN checks proofs behind the scenes. Indeed, it verifies that our proofs are of the desired type. It should be noted that one does not have to be an expert in type theory to use LEAN. To the working mathematician, there is virtually NO difference between set theory and type theory.

Consider the following LEAN code:

```lean
import Std
import Mathlib.Tactic.ByContra

variable {P Q : Prop}

theorem example1 (hp : P) (h : P → Q) : Q := by
  apply h
  exact hp
```

This is just Modus Ponens, which states that if $A \rightarrow B$ and $A$, then $B$. Notice that in the LEAN code, we are literally writing $h : P \rightarrow Q$ as we have discussed before. In fact, we can write this shorter:

```lean
theorem example1' (hp : P) (h : P → Q) : Q := by
  exact h hp
```

In regular math notation, we would write this as $h(hp)$. Recall our discussion about $f:X\rightarrow Y$ and $x : X$. This is the exact same thing! Below are the code examples for AND, OR, and NOT.

AND:
```lean
theorem example2 (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  · exact hp
  exact hq
```

OR:
```lean
-- left hand side proof
theorem example3 (hp : P) : P ∨ Q := by
  left
  exact hp

-- right hand side proof
theorem example3' (hq : Q) : P ∨ Q := by
  right
  exact hq

-- split into left and right hand cases
theorem example3'' (h : P ∨ Q) : Q ∨ P := by
  cases h with
  | inl hp =>
      right
      exact hp
  | inr hq =>
      left
      exact hq
```

One can accomplish `example3''` with `rcases h with h1 | h2 ...` as well.

Example of NOT being used (recall that $\neg A \equiv A \rightarrow \bot$):
```lean
theorem example4 (h1 : P → Q) (h2 : ¬ Q) : ¬ P := by
  intro hp
  have hq := h1 hp
  exact h2 hq
```
This one is a bit nontrivial. Here is the breakdown:

1. `intro hp` takes `¬P` which is the same as `P → False` and gives a hypothesis `P` back (since `P → False` is in the goal). The goal is now set to `False` or the empty type.
2. Now, `hq` will be set to `h1 hp` which is $h1(hp) : Q$.
3. $\neg Q$ is the SAME as the function type $Q \rightarrow \bot$, which means we can apply a term (or function) $h2 : \neg Q$ to $hq$. This gives us a proof of the empty type $\bot$, which is the same as the goal which concludes the proof.