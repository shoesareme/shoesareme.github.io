# The Chair

TJCT 25/26 Rated In-House #2 Problem A

## Statement

Jason has a deep fear of chairs and would like to be as far away from them as possible. Jason in an $$n \times n$$ room $$(1 \leq n \leq 10^{9})$$ with a singular chair. Both Jason's coordinates $$(x_{j},y_{j})$$ and the chair's coordinates $$(x_{c},y_{c})$$ are integer values $$(1 \leq x_{j},y_{j},x_{c},y_{c} \leq n)$$.

Jason would like to maximize $$d = \max(|x_{c}-x_{j}|,|y_{c}-y_{j}|)$$. Jason can move to any of the 8 adjacent integer coordinates around him [^1], with the exception that he cannot go out of bounds (none of this coordinates can ever be $$<1$$ or $$>n$$). What is the minimum number of steps he must take in order to achieve the maximum $$d$$ value?

See pdf (to be added) for input/output format as well as sample cases.

## Solution

To be added :skull:

## Code

I'll clean up this code when I feel like it.

```py
def cheb_dist(x1, y1, x2, y2):
    return max(abs(x1-x2),abs(y1-y2))
 
def lazy(c1, c2):
    return cheb_dist(c1[0], c1[1], c2[0], c2[1])
 
t = int(input())
for _ in range(t):
    # i am way too lazy to properly solve this
    n, xj, yj, xc, yc = [int(i) for i in input().split(" ")]
    j = (xj, yj)
    c = (xc, yc)
    a = [(1,yj),(n,yj),(xj,1),(xj,n)]
    mstep = lazy(a[0], j)
    mdist = lazy(a[0], c)
    for i in range(1, 4):
        ne = lazy(a[i], c)
        if ne > mdist:
            mdist = ne
            mstep = lazy(a[i], j)
        elif ne == mdist and lazy(a[i], j) < mstep:
            mdist = ne
            mstep = lazy(a[i], j)
    print(mstep)
```

[^1]: This includes: $$(x_{j}-1,y_{j}-1)$$, $$(x_{j}-1,y_{j})$$, $$(x_{j}-1,y_{j}+1)$$, $$(x_{j},y_{j}-1)$$, $$(x_{j},y_{j}+1)$$, $$(x_{j}+1,y_{j}-1)$$, $$(x_{j}+1,y_{j})$$, $$(x_{j}+1,y_{j}+1)$$