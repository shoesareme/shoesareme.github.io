# Blog 3 - A Discussion on Infinite Multiset Cardinality (9/18/2025)

I want to discuss a paper about *multisets* that I read awhile back. Specifically, the idea of the cardinality of infinite multisets. So, I want to cover some information about multisets, a review and interpretation of the paper, and my own ideas regarding this concept. The paper is titled "Infinite multisets: Basic properties and cardinality" by Milen V. Velev. All contents of this blog are adapted or in direct response to that paper.

We first develop a bunch of machinery to help us analyze multisets, most of which is found in the paper itself. If you have already read it, please skip to [insert section here].

## Background

**Definition.** A *multiset* $$A$$ is a an ordered pair $$A = (A^{*}, m_{A})$$ where $$A^{*}$$ is a set of elements (called the root set) and $$m_{A} : U \rightarrow \textrm{Card}$$ where $$U$$ is the universe. The function sends every element of $$A^{*}$$ to a nonzero cardinal denoting that element's *multiplicity*, and everything else to $$0$$. 

We can generalize this definition later, but for now it is sufficent. To distuinguish between a set and a multiset, we will write a given set $$A = \{\dots\}$$ and a multiset $$A = [\dots]$$. I write a multiset using square brackets because of the limitations of typesetting on markdown files. Sorry!

So, an example of a multiset would be $$A = [1,1,2]$$ where $$A^{*} = \{1,2\}$$ and $$m_{A}(1) = 2$$ and $$m_{A}(2) = 1$$. We will write $$A = [1,2]_{2,1}$$ to be a bit more general. That is, $$A = [a_{1},a_{2},\dots]_{m_{A}(a_{1}),m_{A}(a_{2}),\dots}$$.

### A Problem with Cardinality

Recall the usual definition of cardinality in choice-environments. 

**Definition.** Two sets $$X$$ and $$Y$$ have the same cardinality if and only if there exists a bijective function $$f : X \rightarrow Y$$. In which case we say $$\|X\| = \|Y\|$$.

How can we define cardinality for multisets? There obviously isn't a correspondence from $$[1,1]$$ to $$[1]$$. Let us try to sum the multiplicities.

**Definition.** For all multisets $$A$$, we let $$\mu(A) = \sum_{a \in A^{*}} m_{A}(a)$$.

However, at least by the paper, this will NOT be our definition of cardinality. The paper gives us this example to show us why isn't a proper generalization:

**Example.** Consider the multiset $$A = [a]_{3}$$ and $$B = [a,b]_{2,1}$$. Although $$\mu(A) = \mu(B)$$, but there is no bijection. In fact, the notion of a bijection doesn't even make sense!

We will define a proper generalization later. For now, let us define some basic things.

**Definition.** For all the definitions below, let $$A$$ and $$B$$ be multisets.
- We say that $$A$$ is a subset of $$B$$ if and only if $$m_{A}(x) \leq m_{B}(x)$$ for all $$x \in A^{*}$$.
- Two multisets are equal if and only if they are subsets of each other. This implies that $$m_{A}(x) = m_{B}(x)$$ for all $$x$$.
- The union $$A \cup B = (A^{*} \cup B^{*}, \max (m_{A}, m_{B}))$$. [^1] 
- The intersection $$A \cap B = (A^{*} \cap B^{*}, \min (m_{A}, m_{B}))$$.
- $$A + B = (A^{*} \cup B^{*}, m_{A} + m_{B})$$.
- $$A - B = (A^{*} \cup B^{*}, m_{A} - m_{B})$$.
- $$\Omega = []$$, the empty multiset.
- The complement of a multiset $$A$$ is $$\Omega - A$$.

We run into an interesting conundrum. The complement possibly implies negative multiplicities. Could this be an issue? Of course, we could instead define it with the universe and such but such a notion isn't also well defined. What multiplicity should each element of the universe have? As such, we will amend our definition of a multiset to allow for strange multiplicities. Now, any rational number along with the cardinals work. This means there is such a notion as $$[a]_{-\frac{1}{2}}$$. As there is already a plethora of work done on this, we will continue by. The paper proceeds to provide a definition for the cartesian product, domain, range, etc. I recommend you read the actual paper to process that information and check over it yourself, we will be proceeding straight into the actual content of the paper from hereon. I will give any definitions that we need often but I again encourage you to read the paper yourself.

## Infinite Multisets

### Proper Cardinality

The paper itself defines domain and range for relations on multisets, we will not be doing that and we will be going straight into functions. Simply put, a relation $$f$$ is a function if and only if for every element $$[a]_{r}$$ in $$\textrm{Dom} f$$, there exists exactly one element $$[b]_{l}$$ in $$\textrm{Ran} f$$ such that $$[a,b]_{r,l}$$ is in $$f$$ with the pair occuring $$m_{1}(a,b)$$ times. [^2] Let $$A$$ and $$B$$ be multisets for all the following definitions.

**Definition.** The multiset function $$f$$ is said to be m-injective if and only if $$f : A^{*} \rightarrow B^{*}$$ is injective and $$\mu(A) \leq \mu(B)$$.

**Definition.** The multiset function $$f$$ is said to be m-surjective if and only if $$f : A^{*} \rightarrow B^{*}$$ is surjective and $$\mu(A) \geq \mu(B)$$.

**Definition.** The multiset function $$f$$ is said to be m-bijective if and only if $$f : A^{*} \rightarrow B^{*}$$ is bijective and $$\mu(A) = \mu(B)$$.

From here, we can define cardinality as usual with m-injectivity now. I again recommend reading the actual paper for more in-depth explanations regarding this. Some interesting things arise.

**Example.** Consider the multisets $$A = [a,b,c]_{1,1,1}$$ and $$B = [x,y]_{2,1}$$. There is a m-surjection but no m-injection, thus we say that $$\|A\| > \|B\|$$.

### Infinite Cardinalities

Let us identify a bunch of new infinities. I will be notating slightly differently than in the paper.

**Definition.** Let $$\mathcal{M}_{1} = \|[1]_{\aleph_{0}}\|$$. We write $$\mathcal{M}_{n+1} = \|[1]_{\mathcal{M}_{n}}\|$$. More generally, define the function $$\mathcal{M}(S) = \|[1]_{S}\|$$.

**Theorem.** $$\aleph_{0} > \mathcal{M}_{1} > \mathcal{M}_{2} > \mathcal{M}_{3} > \cdots > 1$$.

*Proof.* We will first prove that $$\mathcal{M}_{n} > \mathcal{M}_{n+1}$$, and then prove $$\mathcal{M}_{n} > 1$$. For the first claim, proceed by induction on $$n$$. First, let us discuss $$\aleph_{0}$$, which can be thought of as $$\mathcal{M}_{0}$$. We can easily realize that $$f : \mathcal{M}_{1} \rightarrow \aleph_{0}$$ is m-injective (there is an injection upon the root sets and the multiplicities are equal), but not m-surjective (the root sets do not admit a surjection). We just need to show that $$f : \mathcal{M}_{n+2} \rightarrow \mathcal{M}_{n+1}$$ is m-injective but not m-surjective given $$\mathcal{M}_{n} > \mathcal{M}_{n+1}$$. The mapping on the root sets are just singleton to singleton, which obviously exists. Realize that $$f$$ must be m-injective because $$\mathcal{M}_{n+1} < \mathcal{M}_{n}$$ (by the induction hypothesis), so the multiplicity is less as desired. Now we need to show that $$\mathcal{M}_{n} > 1$$ generally. Again, proceed inductively. The base case is trivial, and $$\mathcal{M}_{n+1} = \|[1]_{\mathcal{M}_{n}}\|$$, in which $$\mathcal{M}_{n} > 1$$ by induction hypothesis so $$\mathcal{M}_{n+1} > 1$$. $$\Box$$

This theorem idea can be extended to more general $$S$$.

We have essientally identified an infinity that is somehow less than $$\aleph_{0}$$ but still nonetheless an infinity. Such idea of course makes no sense in the usual set theory. The paper then goes on to play around with rational and negative multiplicities. But the core idea is indeed the $$\mathcal{M}$$ function,

## Evaluation

I will now express a lot more of my own ideas.

### Behavior of Multisets

The paper claims that De Morgan's Law holds, but I believe this is false. The problem lies within the fact that $$\bar{A} = (A^{*}, -m_{A})$$, so the root set is still the same. In the author's proof of the De Morgan's law, the root set becomes $$\bar{A^{*}}$$, but this isn't the case with our definition. Unless I am misunderstanding the concept of negative multiplicities. Consider $$A = [1,2]_{1,1}$$ and $$B = [2,3]_{2,1}$$. $$\bar{A \cup B} = [1,2,3]_{-1,-2,-1}$$, and $$\bar{A} \cap \bar{B}$$ is completely messed up. It should be $$(A^{*} \cap B^{*}, \min(-m_{a},-m_{b}))$$ as per our definition, but the root set is $$\{2\}$$ while our multiplicity function tells us that there should be a $$-1$$ involved with the elements $$1,3$$. According to our definition, we should disregard those two which would give us $$[2]_{-2}$$. But if we allow it, then De Morgan's Law appears to work (at least for the cases I checked, I could be wrong) but still the definition is messed up. It seems that the concept of a root set is impeding our multiset definition, so perhaps we should simply define a multiset by the multiplicity function.

### Ordering of the M-Cardinals

**Theorem.** $$<$$ is not a linear ordering of the M-Cardinals.

*Proof.* Consider the m-cardinal $$\kappa$$ with the usual $$\aleph_{0} = \|\mathbb{N}\|$$.[^3] We let the multiset $$S = [1]_{\aleph_{1}}$$ with $$\kappa = \|S\|$$. We claim there is no m-injection from $$S$$ onto $$\mathbb{N}$$, and vice-versa. There is an injection from the root set $$S^{*}$$ onto $$\mathbb{N}$$, but $$\mu(S) > \mu(\mathbb{N})$$. It's more hopeless for $$\mathbb{N} \rightarrow S$$, there isn't even an injection on the root sets. Hence $$\kappa \nleq \aleph_{0}$$ and $$\aleph_{0} \nleq \kappa$$. $$\Box$$

Despite not being linearly ordered, we still want to be able to analyze the m-cardinal structure since it leads to interesting ideas. So we will attempt to discern the structure of the m-cardinals.



[^1]: Perhaps an abuse of notation, however functions will be treated like numbers in the sense that for functions $$f,g : X \rightarrow Y$$, we say that for some function $$h : Y \times Y \rightarrow Y$$, the notation $$h(f,g)$$ denotes the same as $$h_{f,g} : X \rightarrow Y$$ such that for every $$x \in X$$, $$h_{f,g}(x) = h(f(x),g(x))$$.

[^2]: As per the paper, $$m_{1}(a,b)$$ denotes the count of first coordinate in the ordered pair.

[^3]: I identify $$\mathbb{N}$$ to be the representative of $$\aleph_{0}$$ purely for the sake of formality. Despite the naturals usually being considered a set, we can cast it to a multiset simply by having $$m$$ send all elements to $$1$$.
