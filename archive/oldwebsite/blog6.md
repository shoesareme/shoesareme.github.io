# String Mathematical Foundation (3/7/2025)

_Originally titled: Theory of Concatenation Mathematical Foundation_

~~So, I found a reddit post talking about mathematical cranks (post for another day), and they mentioned the "theory of concatenation" as a mathematical foundation. I could find literally nothing about it as a foundation, so I decided to do it myself.~~

Update: Well, I found it! Yeah, I just remember that I found it awhile back while researching something else. So I guess this blog is useless. Well, it is still an interesting exercise I would say.

## Naive Intuition

So, how do we want to go about this? Well, instead of sets, we will have strings. We can concatenate strings together, at that is the only operation we can do (by the nature of the system). However, this isn't really useful. We can only increase string length, and we can never see what's inside. What is the point? We will add another operator that allows us to get the first character, and another one to delete the first one. Notice how this is very similar to LISP. I have done it this way because it is the easiest. We will also make a way to check if two characters are equivalent.

We can replace one character with another by concatenating several strings together while removing the faulty ones. We can simply "hard code" numbers with an infinite number of definitions. Now, what are characters? Well, they are simply _atomic strings_. This is probably getting confusing, so let's be a bit more formal.

## Formal Definitions

Let us build this off of first order logic. This is the only obvious choice. We will also denote a string with a prime tick.

We will denote atomic strings with $$s^{\prime}_{n}$$, where if $$n \neq m$$ then $$s^{\prime}_{n}$$ is different than $$s^{\prime}_{m}$$. There is no particular meaning to the ordering given by $$n, m$$. The only distiniction is that they are different. Let us denote this as 

$$
\forall n, m (n \neq m \rightarrow s^{\prime}_{n} \neq s^{\prime}_{m}) \quad \textrm{Atomic String Definition}
$$

Now, we will define how the concatenation works. We don't want the potential for some $$s^{\prime}_{n} + s^{\prime}_{m} = s^{\prime}_{q}$$, as this can give rise to infinite loops and such. Therefore,

$$
\forall n, m, q (n \neq m \wedge m \neq q \wedge n \neq q \rightarrow s^{\prime}_{n} + s^{\prime}_{m} \neq s^{\prime}_{q}) \quad \textrm{Atomic Property Preservation}
$$

Additionally, we will say that the concenation of different strings is different. 

$$
\forall a^{\prime}, b^{\prime}, c^{\prime}, d^{\prime} (a^{\prime} \neq c^{\prime} \vee b^{\prime} \neq d^{\prime} \rightarrow a^{\prime} + b^{\prime} \neq c^{\prime} + d^{\prime}) \quad \textrm{Uniqueness Property}
$$

There is one special atomic string, $$\varepsilon^{\prime}$$, which is the empty string. We will define this to be different than any of the $$s^{\prime}_{n}$$ atomic strings as it has fundamental different properties. Namely,

$$
\forall n^{\prime} (n^{\prime} + \varepsilon^{\prime} = \varepsilon^{\prime} + n^{\prime} = n^{\prime})
$$

We want concatenation to be associative (but not communative!). I am not going to bother to define parenthesis, this is not Principia Mathematica. This is not Metamath.

$$
(a^{\prime} + b^{\prime}) + c^{\prime} = a^{\prime} + (b^{\prime} + c^{\prime})
$$

Let us denote $$\textrm{CUT}(x^{\prime})$$ and $$\textrm{SEE}(x^{\prime})$$ as the operations for cutting off the first element and seeing the first element as follows.

If $$x^{\prime}$$ is of the form $$s^{\prime}_{n} + a^{\prime}$$, then $$\textrm{CUT}(x^{\prime})=a^{\prime}$$ and $$\textrm{SEE}(x^{\prime})=s^{\prime}_{n}$$.

Let an alphabet be a collection denoted as follows:

$$
\Sigma^{\prime} = s^{\prime}_{n} + s^{\prime}_{m} + \cdots
$$

## Some Basic Theorems and Functions

Functions will work in terms of concentation. Namely, a general function $$f : Str \rightarrow Str$$ takes in strings and gives back strings. We can define $$\textrm{CUT}$$ and $$\textrm{SEE}$$ with this as well (although the gurauntee that these functions work is axiomatic in nature).

We can define the natural numbers as follows. Let $$0^{\prime}$$ be an atomic string. In fact, just let all the natural numbers be an atomic string. There is probably some clever recursive thing you could do to stop yourself from having infinite constants, but who cares? I don't. Now, define the successor relation be defined as follows (a hard coded approach):

$$
S(0^{\prime}) = 1^{\prime} \\
S(1^{\prime}) = 2^{\prime} \\
\cdots
$$

We can define an analogous predecesor function. This allows us to achieve "loops". From here, recursion can be used and many other techniques. There is probably some proof for the strength of this system, but that will be left as an exercise to the reader. Overall, interesting system. Set theory is still better.