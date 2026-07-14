---
layout: bare
title: My Special Page
---

# Notes on LEAN

> Version: 2
>
> Notes are by Jason Zhang. This follow's Euler Circle's LEAN class. 
>
> Please note that these are my own personal notes; I may choose to gloss over a topic if I am already familiar with it.

## Lecture 0 - Preface

The topics this course will cover mostly concerns how LEAN works and how it can be used in mathematics. More or less, we will not be covering any new mathematical content. We may go over specific foundations concepts related to LEAN, but the majority of these lectures will be on using LEAN itself to go over fairly simple concepts (e.g., calculus, analysis, etc.).

To start, we can re-interpret our regular conception of logic. We equip each proposition $P$ as either $\top$ or $\bot$ (true and false respectively). But, we say that $\top$ corresponds to *provable* (ignore Gödel for a second). Then, we can say the following about the logical connectives:

- $A \vee B \equiv ``A \textrm{ is provable or } B \textrm{ is provable.}"$ 
- $A \wedge B \equiv ``A \textrm{ is provable and } B \textrm{ is provable.}"$ 
- $A \rightarrow B \equiv ``B \textrm{ is provable whenever } A \textrm{ is provable.}"$ 
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

## Lecture 2 - Curry-Howard Isomorphism

LEAN is founded on (CoC / Dependent) Type Theory. This is slightly different than set theory for very subtle and foundational reasons. One of the distinctions is that computers generally show an aversion towards sets (although it is possible!). The reason why computers tend towards type theory is that type theory is a fundamentally computer science theory in the sense that typed $\lambda$-calculi are literally models of computation.

In type theory, we would write $x : X$ to mean something similar to $x \in X$. Notice the notation for writing a function: $f : \mathbb{R} \rightarrow \mathbb{R}$. We are already using type theory notation! This also means that $\mathbb{R} \rightarrow \mathbb{R}$ is a type, which it is, although this will be elaborated upon later.