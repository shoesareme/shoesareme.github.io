# Blog 5 - Response to "The true magnitude of Absolute Totality" (TBD)

*The true magnitude of Absolute Totality* by Sergey Aytzhanov is an interesting paper that has a special place within my journey. Indeed, it is the paper that inspired me to learn how to read formal mathematics and to start my own journey in mathematical research. However, that is a story for another day. What I wanted to talk about here was solely the contents of the paper. I believe it was written by an enthusiast like myself. This is evident by the fact that I cannot find anything about the author online. I also recall a certain MathOverflow post saying that enthusiasts were trying to make a very similar argument to the author.

Regardless, I want to revisit it and talk about some of the ideas covered. The ideas are really interesting, but really nonstandard and involves analysis and thinking not commonly seen in mathematics. I have a particular fascination with these types of nonstandard ideas, and this one is especially interesting. I will go through the paper and express my commentary along the way. 

## Motivation

The motivation of the paper was to introduce a concept of cardinals/ordinals larger than anything currently concieved of in set theory. The paper tries to accomplish this fact in the same way that set theorists previously concieved of uncountable ordinals. 

## Irreducibility

**Definition (Aytzhanov).** $$\Omega$$ is the supremum of all well orderings amenable to a single logical sort[^1].

What this means is that $$\Omega$$ is the well ordering of all well orderings that can be expressed in a single logical sort. By an analogue to the *Burali-Forti Paradox*, $$\Omega$$ cannot be amenable to a singular logical sort.

We will notate well orderings $$\alpha$$ that are $$\beta$$-sort irreducible to be $$\alpha_{\dagger \beta}$$. The least such of these well orderings for a particular $$\beta$$ is $$\omega_{\dagger \beta}$$. We should view 1-sort irredicubility to be the same as the uncountableness of $$\omega_{1}$$.

### Does this even work?

But does this concept even work? Does this make sense? I think not. Especially after what user C7X argued on [MathOverflow](https://mathoverflow.net/q/447922) (which is the same post as above).

In essence, the idea is that we can reduce a two sorted theory $$(V,W,\in)$$ to a one sorted theory $$(\{0\} \times V \cup \{1\} \times W, \in^{*})$$ which means "sorted-ness" isn't really all the special.

So, are we done? Is it already over? To a professional mathematician, probably. But we are here to have fun! Not to publish a research paper or anything. So we will entertain this idea and keep moving on. This will be a recurring theme.

### Standard Model Tangent

### Larger Cardinals

[^1]: A logical sort is a bit hard to define precisely but is easy to think of in practice. Most set theories are of a single sort. They operate over one time of object, a set. Some two sorted set theories may involve two different kinds of sets that are in different domains of discourses in a sense. Models may have to be identified as $$(V, W, \in)$$ instead of just $$(V, \in)$$.
