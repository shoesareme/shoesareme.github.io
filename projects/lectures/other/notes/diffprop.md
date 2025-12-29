# Differential Propositional Calculus

> Source: https://oeis.org/wiki/Differential_Propositional_Calculus_%E2%80%A2_Overview

## Introduction

> I will be notating slightly differently than the author to adhere to convention that I am used to.

Suppose $$a,b,c,d$$ are individuals being subjected to a proposition $$Q$$. We will say that $$\top$$ holds everywhere and $$\bot$$ nowhere. There is also the proposition $$Q$$ and $$\neg Q$$. Regardless, $$a,c$$ is not within the context $$Q$$ while $$b,d$$ are in the first iteration[^1]. In the second, we transform to $$c$$ being inside $$Q$$ while $$d$$ isn't. In this case, $$c,d$$ changed. Thus, to properly describe $$c$$, we need both $$Q$$ and $$\mathrm{d}Q$$. This means that $$c$$ is currently described by $$Q$$, but also $$c$$ has changed relative to $$Q$$. 

Of course, this isn't formal yet, just an illustrative example. If $$q$$ is a proposition, then if $$\mathrm{d}q$$ holds then infer $$\neg q$$. If $$\mathrm{d}q$$ doesn't hold, infer $$q$$ again. In other words, if $$\mathrm{d}q$$ holds, one should assume the negation of what $$q$$ currently is.

We will denote $$a \oplus b$$ to mean "exactly one of $$a$$ and $$b$$ are false." Note that this "exactly one" applies no matter how much we chain $$\oplus$$: $$\bigoplus_{i} a_{i}$$ is true if and only if exactly one $$a_{i}$$ is false. This distinguishes it from the usual XOR.

## Formal

First, let us denote $$\Sigma = \{``a_{1}",``a_{2}",\dots,``a_{n}"\}$$ as the *alphabet*. We will force it to be finite for convience. Now, it seems that we are slowly diving into first order logic as we start talking about properties of objects (in fact, the opening example is seen exactly as that). Regardless, we will form our domain/universe of discourse: $$\mathcal{U}$$. It will be a set of points $$A=\langle a_{i} : i < n \rangle$$ as well as a set of functions (perhaps propositions? predicates?) $$A^{\dagger} = \{f : A \rightarrow \mathbb{B} \}$$ where $$\mathbb{B}$$ is your typical $$0/1$$ boolean algebra.

## Proposition Classes

I recommend seeing the source material for good intuitive pictures. There are $$2^{n}$$ of every case. There are three important classes:

### Linear Propositions

These are those which can be written as 

$$
\bigoplus_{i<n} e_{i} = e_{1} \oplus e_{2} \oplus \cdots \oplus e_{n}
$$

where each $$e_{i}=a_{i}$$ or $$0$$.

### Positive Propositions

These are written as 

$$
\prod{i<n} e_{i} = e_{1} \cdot e_{2} \cdot \cdots \cdot e_{n}
$$

where each $$e_{i}=a_{i}$$ or $$1$$. In this case, $$\prod$$ is just logical AND.

### Singular Propositions

These are written as 

$$
\prod{i<n} e_{i} = e_{1} \cdot e_{2} \cdot \cdots \cdot e_{n}
$$

where each $$e_{i}=a_{i}$$ or $$\neg a_{i}$$. 

## Differentials

> To be finished

[^1]: Indeed, this must be strictly in a temporal logic-esque context.