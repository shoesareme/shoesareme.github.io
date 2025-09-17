# Logic and Proofs

Suppose you had some statement you would like to show to be true. How would you go about proving this? In the real world, you might gather physical evidence such as photos and transcripts. But what about in the land of the abstract? We often rely on pure reasoning to go about this. In this module, we will learn about various different proof techinques to strengthen reasoning skills as well as the underlying logic behind it.

## Proofs

Mathematically, a proof is a set of deductions that go from one true statement to another, often resulting in showing some goal is true. We will cover three main types of proofs. Note that there are many more types of proofs and I encourage you to find more for yourself. However, the three main types we will learn encompass most problems and other proofs.

1. Direct Proof
2. Proof by Contradiction
3. Proof by Induction

### Direct Proof

This is the simplest type of proof. Go from one true statement to another using definitions, axioms, and previous theorems. Here is an example:

**Theorem.** _If a natural number[^1] $$n$$ is even, then $$n^{2}$$ is also even._

Before we begin the real proof, let us first define what it means to be even. One thought that should come to mind is "2 is a factor of $$n$$". But how should we formalize this? It actually isn't that hard, we simply say "all even numbers $$n$$ can be expressed as $$2m$$ where $$m$$ is also a natural number". Verify that this definition is equivalent to "$$n$$ is divisible by 2". Now, we can restate the theorem as "If a natural number $$n$$ is equal to $$2m$$ where $$m$$ is also natural, then $$n^{2}$$ is equal to some $$2q$$ where $$q$$ is also natural." This restated theorem directly implies our goal, so we only need to prove the restated one. We are ready to do the proof now.

_Proof._ Let us rewrite $$n$$ as $$2m$$ in $$n^{2}$$. Evidently, it is $$(2m)^{2} = 4m^{2} = 2(2m^{2})$$. Taking $$q=2m^{2}$$, we can see that $$n^{2}=2q$$ which completes the proof. $$\Box$$

**Exercise 1.1.** Prove that if $$n$$ is odd and $$m$$ is odd, then $$n + m$$ is even.

<details>

<summary>Hint</summary>

Find what it means to be odd.

</details>



### Proof by Contradiction

Suppose we want to prove some statement $$p$$. What if we assume $$p$$ is false, and then show that is absurd? This is the technique known as _proof by contradiction_. It is one of the most useful proof techniques, but it is also a bit controversial for reasons we will not get into[^2]. Let us do an example.

**Theorem.** _There is no smallest positive rational number._

_Proof._ Suppose for the sake of contradiction that $$r$$ is the smallest positive rational number. Consider $$\frac{r}{2}$$. We know this is a rational number because if $$r = \frac{p}{q}$$ then $$\frac{r}{2} = \frac{p}{2q}$$ where $$p, q$$ are nonzero integers ($$q$$ cannot be 0 for obvious reasons and $$p$$ cannot be 0 because then $$r$$ wouldn't be positive). Importantly, $$\frac{r}{2} < r$$ which contradicts the statement "r is the smallest positive rational number". Therefore there is no smallest positive rational number. $$\Box$$

Play close attention to the proof I just described. I assumed the theorem was false, and then reached a state where something was both true and false (a contradiction!). You should use the direct proof methods after you assume something for a contradiction. 

**Exercise 1.2.** Prove that $$\sqrt{2}$$ is irrational.

This exercise is not easy, but you should complete it before moving forward.

### Proof by Induction

Let's say that there some assortment of dominos laid out. You know two things about the dominos: 

1. If a domino gets knocked down, then it will knock down the next domino.
2. The first domino gets knocked down.

From this, you can conclude that all dominos get knocked down. This is the idea behind proof by induction. Suppose we know that some property is true for $$n=1$$, and we know that if it is true for $$n=k$$, then it is true for $$n=k+1$$. From this, we can conclude it is true for all natural numbers $$n \geq 1$$. 

**Theorem.** _$$1+2+3+\dots+n=\frac{n(n+1)}{2}$$_

_Proof._ We can easily verify this to be true for $$n=1$$. Compute $$\frac{1(1+1)}{2}=1$$. Now, assume this is true for $$n=k$$. In other words, $$1+2+3+\dots+k=\frac{k(k+1)}{2}$$. Now, add $$(k+1)$$ to both sides. By the induction hypothesis, $$1+2+3+\dots+k+(k+1)$$ should equal $$\frac{(k+1)((k+1)+1)}{2}$$. But we also know it should equal $$\frac{k(k+1)}{2}+(k+1)$$. So we need to prove $$\frac{k(k+1)}{2}+(k+1)=\frac{(k+1)((k+1)+1)}{2}$$. Rearranging, we can see $$\frac{k(k+1)}{2}+(k+1)=\frac{k(k+1)}{2}+\frac{(2k+2)}{2}=\frac{k^{2}+k+2k+2}{2}=\frac{k^{2}+3k+2}{2}=\frac{(k+1)(k+2)}{2}$$ as desired. $$\Box$$

[^1]: Note that the natural numbers ($$\mathbb{N}$$) is $$\{ 0,1,2,\dots \}$$ in our case. Some people will omit $$0$$ but it is useful for us.
[^2]: You will probably find out why if you pursue theoretical computer science. 
