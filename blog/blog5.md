# Blog 5 - Analysis of $$\omega_{\dagger 1}$$ ordinals and above (TBD)

*The true magnitude of Absolute Totality* by Sergey Aytzhanov is an interesting paper that has a special place within my journey. Indeed, it is the paper that inspired me to learn how to read formal mathematics and to start my own journey in mathematical research. However, that is a story for another day. What I wanted to talk about here was solely the contents of the paper. I believe it was written by an enthusiast like myself. This is evident by the fact that I cannot find anything about the author online. I also recall a certain MathOverflow post saying that enthusiasts were trying to make a very similar argument to the author.

Regardless, I want to revisit it and talk about some of the ideas covered. The ideas are really interesting, but really nonstandard and involves analysis and thinking not commonly seen in mathematics. I have a particular fascination with these types of nonstandard ideas, and this one is especially interesting. I will be mostly expressing my own analysis on the ideas presented.

## Motivation

The motivation of the paper was to introduce a concept of cardinals/ordinals larger than anything currently concieved of in set theory. The paper tries to accomplish this fact in the same way that set theorists previously concieved of uncountable ordinals. 

The ideas introduced here are extremely philosophically thought-provoking, even if I disagree here and there, and I really recommend you read it through yourself. Despite first reading it around 2023, I still find myself revisting and revising my analysis on certain topics.

## Logical Sorts and Irreducibility

We say that a *logical sort* is a domain of discourse to quantify over. For example, if a theory has multiple sorts, then it has multiple domains to quantify over. Classical theories such as $$\mathrm{ZFC}$$ are all 1-sorted.

Let us notate $$\omega_{\dagger \beta}$$ as the least ordinal that cannot be expressed by any $$\beta$$-sorted structure. We will be extensively studying these ordinals.

First, let us take a look at $$\omega_{\dagger 1}$$. On the surface, it would violate an analog of the *Burali-Forti Paradox*. The original paradox prevents the existence of the "largest ordinal". In general, a Burali-Forti paradox has two solutions:

1. The object in question does not exist;
2. The object in question does not satisfy some property $$\phi$$.

Our goal with describing the $$\omega_{\dagger \beta}$$s is to aim for that second solution. In particular, we can view $$\omega_{\dagger 1}$$ as the supremum of all the 1-sorted ordinals. However, there appears to be a lingering problem.

**Lemma.** *$$\omega_{\dagger 1}$$ does not exist.*

*Proof.* Assume $$\omega_{\dagger 1}$$ is $$n$$-sorted. Now, there is an isomorphism

$$
(V_{1}, V_{2}, \dots, V_{n}, \in) \cong \left(\bigcup^{n}_{i = 1} \{i\} \times V_{i}, \in^{*}\right),
$$

as long as we choose $$\in^{*}$$ correctly, which is easy (choose based on the previous $$\in$$). Hence, the second solution to the Burali-Forti paradox cannot apply here, and so $$\omega_{\dagger 1}$$ does not exist. $$\Box$$

This proof is a generalized version of what C7X argued on [MathOverflow](https://mathoverflow.net/questions/100981/ultrainfinitism-or-a-step-beyond-the-transfinite/447922#447922) (this is the same post mentioned above). So, are we done? For a professional mathematician, maybe. But we are not here to review a paper for the most prestigous journal. We are here to learn about interesting ideas and analysis upon them, so we will continue.

It should be noted that Aytzhanov does seem to try to form a counterargument against this, if I am interpreting it correctly. Essientally, we form a "sort-nonstandard" theory $$\mathfrak{T}$$ with second order $$\mathrm{ZFC}_{2}$$ as the base theory. Constants are manually forced in, making $$\mathfrak{T}$$ internally 1-sorted but externally 1-sort irreducible. I'm not sure if this is a direct addressal to the above lemma, but it is a similar idea. It does seem like I'm missing something here, the ordinal $$\omega^{\mathfrak{M}}_{\dagger 1}$$ is briefly noted and is talked about like it is already an established concept, yet I cannot find anything about it. Any more information would be appreciated.

### Attempting to Rescue $$\omega_{\dagger 1}$$

Regardless, we will try to develop our own attempt at saving $$\omega_{\dagger 1}$$.
