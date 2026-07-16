---
layout: github
title: LEAN Notes
---

# Notes on LEAN

> Version: 4
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

Types arise by rules. These rules define which terms (which is the equivalent for element) are in the type, and when terms are equal. There is additional "data" given by each type. Consider the set $X=\lbrace1\rbrace$. This set $X$ can also be defined by $X=\lbrace x \in \mathbb{R} : (x-1)^{2}=0\rbrace$. Indeed, in set theory, there isn't a distinction to be made here. The $x$ for which $(x-1)^{2} = 0$ is just $x=1$. But, from intuition, we know the second definition of $X$ gave us some more information. We know a bit more about the "context" surrounding $X$, there are infintely many ways to define the set $\lbrace1\rbrace$ including the trivial and solution way we just discussed. But we seemingly know a bit more about $X$ when we define it as the solutions to some set. This is the distinction that type theory grants upon us.

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

## Lecture 3 - Implementing Basic Number Theory

**Definition.** Let $n,d : \mathbb{N}$. We say that
- $d$ divides $n$ (shortened to $d \mid n$) if $\exists k : \mathbb{N} \ (n = k \cdot d)$.
- $n$ is prime (technically irreducible) if $n > 1$ and $d \mid n \rightarrow d = 1 \vee d = n$.

**Example.** All variables are naturals. Prove the following as precisely as possible:
- Let $d \mid n$ and $d \mid m$. Show $d \mid n + m$.
- If $p$ is a prime number then $p^{2}$ is not.

*Solutions (natural language).* We will prove it using the definitions.
- First, we know $\exists k_{1} : \mathbb{N} \ (n = k_{1} \cdot d)$ and $\exists k_{2} : \mathbb{N} \ (m = k_{2} \cdot d)$. Therefore, $n+m=k_{1}\cdot d + k_{2}\cdot d = (k_{1}+k_{2})\cdot d$ by distrubution. Now, we can nominate $k=(k_{1}+k_{2})$ in the equation $\exists k : \mathbb{N} \ (n+m = k \cdot d)$, which works as we've already shown.
- Note that $p^{2}=p \cdot p$. Now, let $d \mid p^{2}$. We aim to show $d = p \neq p^{2}$ works. First, notice that $1 < p$ implies that $p < p^{2}$ since $p$ is not a unit element. Now, nominate $k = p$ in the equation $\exists k : \mathbb{N} \ (p^{2} = k \cdot d)$ . This comes out to $p^{2} = p \cdot p$, which we knew was already true. $\Box$

*Solution (LEAN).* Observe the following codes:
- The code below does what we want it to. The `rcases` introduce the variables $k_{1}$ and $k_{2}$ from our natural language proof, we nominate $k_{1} + k_{2}$ as desired, and then we show the two sides are equal.
```lean
theorem example1 (hn : d ∣ n) (hm : d ∣ m) : d ∣ n + m := by
  rcases hn with ⟨k, hk⟩
  rcases hm with ⟨l, hl⟩
  use k + l
  rw [hk, hl]
  exact Eq.symm (Nat.mul_add d k l)
  ```
- Similar in nature. See examples3.lean, `theorem example2`. $\Box$

Note that you can use `exact?` to lookup how to prove a specific statement. You can create sublemmas to do so.

Let us remind ourselves of proof by induction, an axiom of the naturals.

**Axiom Schema of Induction.** Let $\varphi(n)$ be a formula on $\mathbb{N}$. Then $\varphi$ holds for all $n : \mathbb{N}$ if 
- $\varphi(0)$ holds; and
- $\varphi(n) \implies \varphi(n+1)$.

**Example.** Prove the classic Gaussian sum $\sum_{k=0}^{n} k = \frac{n(n+1)}{2}$ for all $n : \mathbb{N}$.

*Solution (natural language).* Let $\varphi(n)$ be the statement $\sum_{k=0}^{n} k = \frac{n(n+1)}{2}$. Let us induct on $n : \mathbb{N}$.
- For $n=0$, we have $\sum_{k=0}^{0} k = 0 = \frac{0(0+1)}{2}$ so $\varphi(0)$ holds.
- Assume $\varphi(n)$ holds. Notice that $\sum_{k=0}^{n+1} k = \sum_{k=0}^{n} k + (n + 1) = \frac{n(n+1)}{2}+ (n + 1)$ by the induction hypothesis. This eventually simplifies to $\frac{(n+1)((n+1)+1)}{2}$ by virtue of trivial manipulations. $\Box$

*Solution (LEAN).* First, note that `Finset.range n` is the set $\lbrace 0, 1, \dots, n-1\rbrace$ and `∑ i ∈ Finset.range n, i` is $\sum_{i=0}^{n-1} i$. This can be checked by the `#check` command as usual. Now, here is the full code. 
```lean
theorem Gauss_sum (n : ℕ) : ∑ i ∈ Finset.range (n + 1), i = n * (n + 1) / 2 := by
  induction n with
  | zero => rfl
  | succ n ih =>
      calc
        ∑ i ∈ Finset.range (n + 1 + 1), i
          = (∑ i ∈ Finset.range (n + 1), i) + (n + 1) := by
            exact Finset.sum_range_succ (fun x ↦ x) (n + 1)
        _ = n * (n + 1) / 2 + (n + 1) := by rw [ih]
        _ = (n * (n + 1) + (n + 1) * 2) / 2 := by
          refine (Nat.add_mul_div_right (n * (n + 1)) (n + 1) ?_).symm
          exact Nat.succ_pos 1
        _ = (n + 2) * (n + 1) / 2 := by
              rw[Nat.mul_comm (n +1) 2, ← Nat.add_mul]
        _ = (n + 1) * (n + 2) / 2 := by
          rw[Nat.mul_comm (n + 2) (n + 1)]
```
First, we have the summation have finite set for $n+1$ since it always ends a position beforehand. Now, we have the `zero` case, which LEAN can instantly realize are equal by `rfl`. 

In the inductive case (or successor case), we are going to use `calc` which lets us compute manipulations quickly. The `_` indicates a new step of the calculation is starting. Another new tactic is `refine`, which allows you to use a theorem for which we do not know all the hypothesis are true. These hypothesis that we have not yet shown become goals. The rest is just annoying manipulations. $\Box$

**Theorem (Strong Induction).** $\varphi(n)$ holds on all $n : \mathbb{N}$ if
- $\varphi(0)$ holds; and
- $\forall n : \mathbb{N}$, $(\forall m \leq n \ \varphi(m)) \implies \varphi(n+1)$.

*Proof (natural language).* Let $\psi(n) := \forall m \leq n \ \varphi(m)$. Here are four observations to make:

1. $\psi(0) \iff \varphi(0)$
2. $\psi(n) \implies \varphi(n)$
3. $\forall n : \mathbb{N} \ \psi(n) \implies \forall n : \mathbb{N} \ \varphi(n)$
4. $(\psi(n) \rightarrow \varphi(n+1)) \implies (\psi(n) \rightarrow \psi(n+1))$.

As for the proofs:

1. Trivial (by definition, since the only $m \leq 0$ is $m=0$). 
2. Also trivial (also by definition, since $n \leq n$).
3. Also trivial (by #2).
4. The left hand side implies $\forall m \leq n \ \varphi(m)$ and $\varphi(n+1)$ whenever $\psi(n)$, so $\forall m \leq (n+1) \ \varphi(m)$ equals $\psi(n+1)$ holds.

Our theorem statement can be rewritten as:

$\varphi(n)$ holds on all $n : \mathbb{N}$ if

- $\varphi(0)$ holds; and
- $\forall n : \mathbb{N} \ (\psi(n) \implies \varphi(n+1))$.

Now, let us assume that 

- $\varphi(0)$ holds; and
- $\forall n : \mathbb{N} \ (\psi(n) \implies \varphi(n+1))$.

(aka the restated theorem hypothesis)

Our goal is now to prove that $\forall n : \mathbb{N} \ \varphi(n)$. Let us induct on $n$ over $\psi$.

- Observation #1 and the first hypothesis of the theorem grants us that $\psi(0)$ holds.
- Assume $\psi(n)$. The left hand side of observation #4 is true by the second hypothesis of the theorem. Therefore, we obtain $(\psi(n) \rightarrow \psi(n+1))$, and since we assumed $\psi(n)$ we get $\psi(n+1)$ as desired.

Because we proved $\forall n : \mathbb{N} \ \psi(n)$, observation #3 grants us $\forall n : \mathbb{N} \ \varphi(n)$. $\Box$

*Proof (LEAN).* First, define the relevant notation

```lean
variable (P : ℕ → Prop)

def complete_induction : Prop :=  (P 0 ∧ (∀ n, (∀ m, m ≤ n → P m) → P (n + 1))) → ∀ n, P n

def Q (P : ℕ → Prop) (n : ℕ) : Prop := ∀ m, m ≤ n → P m
```

Note we have $P$ for $\varphi$ and $Q$ for $\psi$. It is certainly possible to prove the below, but we'll just `sorry` them away since we are lazy. These will be left as exercises.

```lean
lemma lemma0 : P 0 → Q P 0 := by
  sorry

lemma lemma1 (n : ℕ) : Q P n -> P n := by
  sorry

lemma lemma2 (n : ℕ) : (Q P n -> P (n + 1)) -> (Q P n -> Q P (n + 1)) := by
  sorry

lemma lemma3 : (∀ n, Q P n) -> ∀ n, P (n) := by
  sorry
```

These were the four observations we made. From here, the theorem is proven almost exactly like we said above.

```lean
theorem induction_implies_complete_induction : complete_induction P := by
  intro ⟨hP0, hQP⟩
  have hQall : ∀ n, Q P n := by
    intro n
    induction n with
    | zero =>
        exact lemma0 P hP0
    | succ n ih =>
        exact lemma2 P n (hQP n) ih
  intro n
  exact lemma3 P hQall n
end
```

This concludes the proof. $\Box$

Now, consider induction on a finite set. Classically, finite sets can be well-ordered. So, we can describe a finite set as functions $f : I \rightarrow \mathbb{N}$, or maybe even $f : I \rightarrow X$ for type $X$. We would use the induction axiom schema on the size of $I$. Likewise, our $I$ can have elements of a general type $T$. Therefore, inducting on the index set itself is not too different than the finite set. We will now consider inducting over subsets of finite sets.

**Theorem (Finite-Set Induction).** Consider the proposition $\varphi$. We say that $\varphi(I)$ for all finite sets $I$ if 

- $\varphi(\varnothing)$ holds; and
- If $\varphi(I)$ then $\varphi(I \cup \lbrace x \rbrace)$ holds for $x : T$.

*Proof.* Exercise. $\Box$

Briefly note that we are fine to use "$I \cup \lbrace x \rbrace$" and even the terminology "set" here despite the type theory underlying this because the distinction does not matter here and LEAN handles it correctly anyways.