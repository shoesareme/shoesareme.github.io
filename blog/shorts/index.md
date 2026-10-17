# Mathematical "Shorts"

Here is a list of mathematical "shorts" that I have written throughout the years that I think are interesting but not long enough to warrant a full blog page. Regardless, you can think of them as mini-blogs and "doom scroll" them if you wish.

Note: These were originally hosted on a different website, and I moved them over here. As such, some of the formatting might seem off.

## A Standard Peano Model (10/16/2026)

According to the Peano Axioms, $$E = \{1,e,e^2,e^3,\dots\}$$ could be a perfectly valid model for $$\mathbb{N}$$. Consider taking $$S(n)=n \cdot e$$ where $$\cdot$$ is the usual multiplication under $$\mathbb{R}$$, along with $$0_E = 1$$.

Exercises:
1. Find a valid form for multiplication over $$E$$. Hint: $$\ln e^{A} = A$$.
2. Checking the Robinson axioms is easy. Verify the induction schema instead.
3. Argue that, philosophically speaking, this implies that creating a full axiom list to uniquely pin down $$\mathbb{N} = \{0,1,2,\dots\}$$ as we understand it is not possible (your argument should be based on Russell's critique of the Peano axioms, not the incompleteness theorems, although you are free to reference them).


## An Abuse of Notation that Works (10/10/2026)

Consider the equation provided by 

$$
f - \int f = 1.
$$

How can we solve this? Well, physicists will tell you that mathematical rigor is for nerds, and here that might actually be true. We can solve this with ease ignoring the rigor. Let us factor $$f$$ out of the expression to achieve $$\displaystyle f(1 - \int) = 1$$. This $$\int$$ is not to be confused with $$\int 1 \mathrm{d}x$$, which evaluates to something. The $$\int$$ is just an integral symbol by itself. Now, divide both sides by $$\displaystyle (1 - \int)$$. We get $$\displaystyle f = \frac{1}{1 - \int} \cdot 1$$. Recall the geometric series sum formula, which states that $$\frac{1}{1-r} = 1 + r + r^{2} + \cdots$$. Thus,

$$
f = \left(1 + \int + \int^2 + \cdots \right) \cdot 1
$$

which is the same as

$$
f = \left(1 + \int + \iint + \cdots \right) \cdot 1 = 1 + \int 1 + \iint 1 + \cdots,
$$

which upon evaluating the integral gives us

$$
f = 1 + x + \frac{x^2}{2} + \cdots = \sum_{k=0}^{\infty} \frac{x^{k}}{k!} = e^{x}.
$$

This is the answer, and you can verify this from the original equation. 

## Evaluating $$e^{\mathrm{d}/\mathrm{d}x}$$ (10/5/2026)

Consider $$e^{\frac{\mathrm{d}}{\mathrm{d}x}}$$. Does this even mean anything? Well, consider taking the Maclaurin series for $$e^{x}$$.

$$
e^{\frac{\mathrm{d}}{\mathrm{d}x}} = \sum_{k=0}^{\infty} \frac{1}{k!} \left(\frac{\mathrm{d}}{\mathrm{d}x}\right)^{k} = 1 + \frac{\mathrm{d}}{\mathrm{d}x} + \frac{1}{2!} \left(\frac{\mathrm{d}}{\mathrm{d}x}\right)^{2} + \cdots.
$$

This looks a bit promising. Consider trying to evaluate $$e^{\frac{\mathrm{d}}{\mathrm{d}x}}f(x)$$ for some sufficiently nice function $$f : \mathbb{R} \to \mathbb{R}$$.

$$
e^{\frac{\mathrm{d}}{\mathrm{d}x}}f(x) = \sum_{k=0}^{\infty} \left(\frac{\mathrm{d}}{\mathrm{d}x}\right)^{k}\frac{f(x)}{k!}.
$$

The RHS also looks like a Taylor series, and in fact we can interpret it as one. It can be seen as a taylor series for $$f(x+1)$$, thus we arrive to our conclusion that

$$
e^{\frac{\mathrm{d}}{\mathrm{d}x}}f(x) = f(x+1).
$$

Cool! 

## (In)Direct Proofs (9/23/2026)

A proof by contradiction (techincally a proof of negation) is a direct proof since $$\neg A \equiv A \rightarrow \bot$$ so proving $$\neg A$$ is logically the same as assuming $$A$$ and proving $$\bot$$ via a direct proof. This process is the exact same for a proof by contradiction, thus proof by contradiction is a direct proof.

## An Abuse of Notation that Doesn't Matter (9/5/2026)

Technically, $$\mathbb{Q} \subset \mathbb{R}$$ is an abuse of notation. Indeed, $$\mathbb{R}$$ is the set of equivalence classes of Cauchy sequences of $$\mathbb{Q}$$ (aka the Cauchy completion of $$\mathbb{Q}$$). It is more formal to say that there is a certain injective homomorphism $$\mathbb{Q} \to \mathbb{R}$$ that satisfies certain field properties. This distinction becomes important when dealing with types and computer science.

## Big $$O$$ and Friends (9/3/2026)

In theoretical computer science, we actually consider three kinds of time complexity (which is actually different than AP CS). They are called $$O$$, $$\Theta$$, and $$\Omega$$. The intuition behind these three is that they mirror $$\leq$$, $$=$$, and $$\geq$$ respectively. For example, it is actually true that $$f(n) = n$$ is $$O(n^2)$$. This is because "$$n \leq n^2$$" for large enough $$n$$. So, $$O$$ behaves differently than taught in AP CS. Luckily, we have $$\Theta$$, which behave pretty much how you learned $$O$$ did in AP CS.

## Circularity in $$\mathbb{N}$$ Definition (8/8/2026)

The definition of $$\mathbb{N}$$ is circular in nature: The definition of $$\mathbb{N}$$ per Peano is a structure built from 0, and the successor operation. But, this already requires the coherency of strings length $$n$$ for arbitary $$n \in \mathbb{N}$$. For example, $$1 = S0$$ is a string of length 4, so to know "1 is well behaved" we must already know 4 is. Even if you patch this issue (which might be possible by adding a few more axioms) you still have an issue. That is, N defines the nature of "inductiveness". When you define $$\mathbb{N}$$, you will say something like "the numbers in N are $$0, S0, SS0, \ldots$$ and so on" but that and so on relies itself on the inductive properties of N which you are trying to establish. This philosophical problem does manifest in actual mathematics: namely its related to why we have nonstandard models for $$\mathbb{N}$$.

## 1+1=2 (7/7/2026)

**Theorem.** $$1+1=2$$.

*Proof.* Let us use the axiomization of Peano Arithmetic by Robinson + Induction Schema to prove this. The structure of $$\mathbb{N}$$ is defined by the operation $$S$$ (the successor operation). By definition, we obtain:

1. $$1 = S(0)$$,
2. $$2 = S(1)$$.

Now, consider the equation $$1+1=1+1$$ which is true by the refl equality axiom ($$\forall x (x=x)$$). Substitute in $$1=S(0)$$ to obtain $$1+1=1+S(0)$$, and by axiom 4 ($$\forall x,y (x+S(y)=S(x+y))$$) we obtain $$1+1=S(1+0)$$. From axiom 3 ($$\forall x (x+0=x)$$), we have $$1+1=S(1)$$. Finally, substitute in $$2=S(1)$$ to obtain $$1+1=2$$ as desired. $$\Box$$.

## Prove that $$0.\bar{9} = 1$$ (6/30/2026)

(Likely) Every proof that you've seen that $$0.\bar{9}=1$$ is wrong. Algebraic manipulations such as $$\frac{1}{3} = 0.\bar{3}$$ which eventually conclude $$0.\bar{9} = 1$$ do not constitute as proofs.

First, we must establish what $$0.\bar{9}$$ even means and if it even exists in $$\mathbb{R}$$. Well, we can consider the Cauchy Construction of the reals. Let 

$$
x_{n} = \sum_{i=1}^{n} 9 \cdot 10^{-i} = 0.\underbrace{999...999}_{n \textrm{ times}}.
$$

We consider the Cauchy Sequence $$x_{i}$$. 

**Lemma.** The $$\langle x_{i} : i \in \mathbb{Z}^{+} \rangle$$ is indeed a Cauchy Sequence.

*Proof.* For any $$n,m \in \mathbb{Z}^{+}$$ with $$m<n$$, the absolute value $$\|x_{n} - x_{m}\| \leq 10^{1 - m}$$ which can be pushed below any arbitary $$\varepsilon$$ tolerance. $$\Box$$

**Theorem.** $$0.\bar{9} = 1$$.

*Proof.* We just want to show that $$\lim_{n \to \infty} x_{n} = 1$$. That is, the sequence converges to $$1$$. Notice that $$\|x_{n} - 1\| = 10^{-n} < \frac{1}{n} < \varepsilon$$ whenever $$n > \frac{1}{\varepsilon}$$, showing the sequence converges as desired. $$\Box$$

## Mathematical Backrooms (6/29/2026)

Mathematics has its own "backrooms". Our example will be $${}^{*}\mathbb{N}$$. This set is special in the sense that it behave much like the $$\mathbb{N}$$ we all know and love, but deviates in very small ways that are hard to discern using mathematical machinery (this is why I refer to it as the backrooms). Roughly speaking, $${}^{*}\mathbb{N}$$ contains a copy of $$\mathbb{N}$$ proceeded by several infinite segments of "nonstandard natural numbers". These "natural numbers" are frauds and fakes: they are actually infinite and not natural numbers are all but were smuggled in via some difficult construction that I won't be covering.

$$
{}^{*}\mathbb{N} = \{\underbrace{0,1,2,\dots}_{\textrm{finite elements} \ (\mathbb{N})}, \ \underbrace{\dots, N-1, N, N+1, \dots}_{\textrm{infinite elements}}\}.
$$

This is a rough outline of what $${}^{*}\mathbb{N}$$ looks like. Now, just because elements like $$N$$ are infinite doesn't mean they behave like how we would expect $$\infty$$ to. In fact, it behaves exactly like a regular number. A generalized version of this is known as the "transfer principle", which states that "statements true in $${}^{*}\mathbb{N}$$ are also true for $$\mathbb{N}$$ and vice-versa". This is subject to certain restrictions and fine-print that nobody would have the patience to read. For example, the statement "for all $$n$$, $$n<n+1$$" is true in both $$\mathbb{N}$$ and $${}^{*}\mathbb{N}$$. Of course, there are analogs that give rise to $${}^{*}\mathbb{R}$$ and more complex sets (subject to fine-print here again). What is actually pretty cool is that the transfer principle tells us that these nonstandard sets are actually useful for proving stuff about the standard or usual sets. We can prove a conjecture $$P$$ true in $${}^{*}\mathbb{N}$$, and then conclude it is also true for $$\mathbb{N}$$ which we care about (as long as we handle the fine-print correctly which usually isn't hard). 

## Minority Rule (6/29/2026)

> I might make this one into a longer blog post.

Imagine a voting game where you must vote `Yes` / `No` against other people. The **minority** side wins. If we have 12 `Yes` and 10 `No`, then `No` wins. Any draws result in revotes. Believe it or not, if you reveal which side you are voting for, you gain an advantage (assuming some type of rationality in your opponents)!

Suppose there are 4 players including yourself. You confidently tell everyone that you will vote `No` and demonstrate it to them (i.e., they know that you will vote `No` for a fact and that this isn't a bluff). Now, here might be the thought process of another (as I said before, rational) player:
"If I wish to join the minority, then I would need to vote `Yes`. Unfortunately, if the two other players also believe that, then we will all lose to the `No` voter. However, if vote `No`, then I cannot possibly win this round. This is because there will be at least 2 `No` votes, which is greater than or equal to half of the players, meaning it will never be the minority. My best hope in that case would be a tie."

The other players are not completely lost yet! Besides forming a team, there's something someone else can do to even the playing field a little.

## Diophantine Undecidability (6/27/2026)

Diophantine equations are *Turing complete*, meaning that they are able to simulate general computation. Specifically, the equation solution sets can be any recursively enumerable set, and also if some machine doesn't halt it means that the corresponding Diophantine has no solutions. For example, there is a Diophantine who's solutions are the prime numbers (for a specific variable). But, this is the least interesting example. More interestingly, we have a certain Diophantine where there exists integer solutions $$\vec{v}$$ to $$D(\vec{v}) = 0$$ if and only if ZFC is inconsistent. I'm also fairly certain that this Diophantine is constructible! One can find the coefficents. Note that the usage of ZFC here is not special, one can easily substitute for Peano Arithmetic or anything they desire. Another interesting (non-set theoretic) Diophantine that can be constructed is one which has solutions if and only if Goldbach's conjecture is false. As a reminder: Goldbach's Conjecture: Every even integer $$n > 2$$ can be expressed as the sum of two prime numbers.

Now, consider some Turing Machine (or Python Program) $$T$$ that enumerates even $$n > 2$$ and checks every combination of prime numbers below, seeking for a sum that works. If the conjecture is false and some $$m > 2$$ does not satisfy it, then $$T$$ will pick it up and HALT right after. Now, by the correspondence (formalized in the MRDP theorem) we established, there is therefore some Diophantine $$D$$ such that if there are integer solutions $$\vec{v}$$ where $$D(\vec{v}) = 0$$, that means the machine halts and thus Goldbach is false. If no such solutions exist, then it is a proof that Goldbach works. This is particularly powerful because we do not care at all how efficent $$T$$ is. You can do similar things for the Riemann Hypothesis I believe. 

In fact, you can practically solve mathematics! Imagine you had a magical Diophantine solver oracle which can tell you the solutions to any Diophantine if any. Suppose there is some conjecture $$P$$ you want to decide. Let us assume ZFC consistent (plus we could just use a Diophantine to see if it is or not). Now, starting from the axiom of ZFC, our machine $$T$$ will enumerate through every possible true statement it can make. Every proof possible, even the dumbest statements. If $$T$$ ever hits the statement $$P$$, it halts. Otherwise, it continues running forever. So, if the corresponding Diophantine $$D$$ has solutions, we know for certain that $$P$$ is true. If it doesn't, then $$P$$ is false (or undecidable by ZFC but we can work around this by working in $$\mathrm{ZFC} + P$$ and check consistency).

## On Curry and Lobs (6/20/2026)

Imagine we are trying to decide a conjecture $$\phi$$. Here is a very interesting proof tactic that is completely valid!

Assume "$$\phi$$ is provable". Now, imagine we are now able to conclude $$\phi$$ from this. In other words, we prove that "($$\phi$$ is provable) implies $$\phi$$." 

Then, $$\phi$$ is true in general. This is of course the famous Lob's theorem which is closely related to Curry's paradox.

To be specific on Curry's Paradox:

1. Let the special sentence read: "If the special sentence (this sentence) is true, then pigs do fly."
2. If the special sentence is true, then the special sentence is true. (Obvious: If X then X)
3. If the special sentence is true, then "If the special sentence is true, then pigs do fly." (Substitute in)
4. If the special sentence is true, then pigs do fly. (By contraction: X -> (X -> Y) is the same as X -> Y).
5. But #4 is the same as the special sentence, so the special sentence is true.
6. Because the special sentence is true: pigs fly!

Notably, this is immensly powerful when translated through the aformentioned Curry-Howard Correspondence.
Most importantly, the reason why Curry's paradox shows that simple untyped lambda calculus is inconsistent is the same reason why Turing Complete systems are inconsistent\* by Curry Howard Isomorphism.

(\*Technicalities apply.)

Thus, by Curry Howard Isomorphism, Java would translate to an inconsistent logic.

The fundamental reason why is of course because of recursion.

## Cauchy's FE (6/15/2026)

The fact that Cauchy's Functional Equation has nonlinear solutions is a consequence of the fact that every connected graph has a spanning tree.

## (Ultra)Finitism (6/7/2026)

Perhaps one of the most interesting philosophies concerning mathematics is that of "ultrafinitism". To understand this philosophy, we must first understand "finitism" in mathematics.

Roughly, finitism is the belief that only finite objects have actual ontological existence in math. Every natural number exists, but the set N does not. This is an actual school of thought in mathematics with theories developed surrounding it (to contrast it with the fact that many mathematical "cranks" love taking finitism for their own agenda). 

One step further are the ultrafinitists. They (roughly) claim that "sufficiently large" quantities do not actually exist either (usually defined with some sort of physical actualization). For example, the number e^e^e^79 is not a number in (some) ultrafinitist belief systems. There are many different approaches to developing a formal theory for ultrafinitism (some having a largest number, and some not having one). 

If this sounds completely absurd to you, good. However, maybe the following argument will make it sound slightly less crazy:

If you were to ask some ultrafinitists whether $$2$$ exists, they would answer yes without hesitation. Ask them whether $$2^2$$ exists, and it would also be almost immediately yes. Ask $$2^3$$, and you get some noticeable delay before the yes. Ask for $$2^4$$, and you get quite some delay before the yes. Now, if you ask for $$2^100$$, you'll certainly get a "yes", but only after $$2^99$$ times longer than it took to answer yes to $$2$$. Good luck waiting that long! 

## Well-Ordering Paradoxes (5/17/2026)

Alice and Bob are playing a game on the positive integers. On each of their turns, they can color the next n>=1 integers their color, where n is their choice (e.g., Alice colors the numbers 1-3, then Bob colors 4-9, etc.). Their goal varies, but Alice wants the set of numbers she colors to form a certain condition and Bob just wants to stop Alice. Alice goes first.

For example, the condition might be "the set contains an infinite number of primes". If this were the case, Alice has a winning strategy. Alice can just color up to the next prime, and there is nothing Bob can do because there are an infinite number of primes. If the condition was "the set does not have an infinite number of primes", then Alice would be out of luck. Bob can just color right before the next prime number, and since Alice has to color at least one square on her turn, she'll color an infinite number of primes.

This game has no draws, the win condition is  predetermined before hand with no randomness and both players have perfect information and are perfectly logical.

If you believe, given the win condition, that one player has a winning strategy, then the well ordering theorem fails. In other words, if you believe in the well ordering theorem, then there exists some win condition where neither Alice nor Bob has a winning strategy (in fact, I can provide such a construction!).

This may tempt you to believe that the well-ordering theorem is not true. Just note that if the well-ordering theorem is not true, then there exists a family of nonempty sets such that the cartesian product of that family is empty (note that the cartesian product of {1, 2} and {3,4} is {(1,3), (1,4), (2,3), (2,4)}). 

Another weird consequence:

There are 100 prisoners who are playing a game to earn their freedom. The prisoners will each go into seperate rooms where they cannot communicate, each with infinite boxes labelled 1, 2, 3, ... Each box contains a real number, and boxes with the same number are identical between the rooms (so box 1 will have the same number inside in all the rooms). Prisoners may open any number of boxes they want, but they must leave at least one closed. Once they are done, they must pick a closed box and guess the number inside. If at least 99/100 are correct, then they all go free. The prisoners can discuss strategy beforehand, but the warden can listen in and pick the numbers in the boxes however he wants. How can you guarantee the prisoners' freedom?

If the well-ordering theorem is true: you can do it!

Alternatively, if the well-ordering theorem fails, then the following is possible:

There exists a tree T with no leaves and no infinite paths. That is, every finite path can be extended another step but there is no path that goes forever.

Essentially, when it comes to whether you believe in the well-ordering theorem or not, neither choice is a good one.

## Constructivism (5/16/2026)

I suppose I'll be the substitute fact for today.

At the turn of the 20th century, a new and radical idea was brewing among mathematicians who rejected many of the established analysis and principles by the mainstream.

I am of course referring to constructive mathematics (sometimes known as "intuitionistic" although there is a subtle difference). Constructive mathematics was and is a new emerging paradigm that redefines what math is and what truth means. It is not a preference, or just a different way of doing things. It is a radically new ideology on what is true within mathematics. It is currently being pushed by category theorists and computer scientists alike.

Very generally and roughly, constructivists think that proofs should always be constructive and that propositions are true if there is a valid construction that satisfies it. For example, a proof by contradiction is (usually) not allowed because it does not construct anything to show the truthness of a proposition. If you use proof by contradiction to show that something must exist, we are still none the wiser to what that thing is. On a more fundamental level, constructivists reject the law of the excluded middle (for every proposition, either P or not P is true), and double negation (not not P = P). That is NOT to say that constructivists think those are never true; instead they think we cannot say they are true in every case (to see why, use the semantics of "statement is true iff there exists a construction". For example, if i know there is not a construction for not P, does that mean I can construct something for P?). Of course, there are so many technicalities with this and the picture I've presented is not 100% accurate.

The rejection of the above principles have led to some classically outrageous results. Here is a short list of things that are all classically true but constructively false in some contexts:

1. For every real number x, either x = 0 or x is not 0.
2. All subsets of a finite set are finite.
3. Every continuous function attains a maximum on [0, 1].

If you are interested and up for the challenge, I recommend reading Bauer's "Five Stages of Accepting Constructive Mathematics". The first few pages (minus one or two paragraphs) should be intelligible to anyone with basic knowledge on proofs.

## To be continued!

I am working on archiving more of these here. Stay tuned!
