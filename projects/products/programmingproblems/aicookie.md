# AI Cookie Monster wants Infinite Cookies at 3 AM 

TJCT 25/26 Rated In-House #4 Problem F

## Statement

It is 3 AM, and the Cookie Monster (unfortunately replaced by an AI), wants some cookies. He lives in a town of $$n$$ ($$1 \leq n \leq 10^{3}$$) buildings, each of which has a unique addr
ess ($$1 \leq i \leq n$$). Every building is either a house (denoted $$0$$) or a cookie shop (denoted $$1$$). At time $$t=1$$, he starts at address 1 and will proceed to move around the town. His movement is based on a directed graph and an infinite binary string $$s$$. Each building gets one node on the graph, and has edges specified as $$i$$ $$j$$ $$k$$ (one edge ($$i, j$$) and another ($$i, k$$)). At any given time $$t$$, if the Cookie Monster is at address $$i$$, he will move to $$j$$ at time $$t+1$$ if $$s_{t} = 0$$, otherwise he will go to $$k$$ (note that $$i = j$$ or $$i = k$$ or both may be true).  Cookie Monster is happy with a string $$s$$ if he is inside a cookie shop for an infinite amount of time. Note that every strongly connected component of the graph is either purely houses or purely cookie shops.

You are tasked with building a new town/graph with size $$m \leq n$$ such that Cookie Monster is happy with any $$s$$ in the new town if and only if he is happy with $$s$$ in the old town. Note that the new town also has to satisfy the strongly connected component requirement. Output the smallest $$m$$ where this is possible.

See pdf (to be added) for input/output format as well as sample cases.

## Solution

Left as an exercise.

(jk but to be added)