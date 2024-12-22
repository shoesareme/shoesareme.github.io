# Ordinal Programming Challenge (11/28/2024)

## Background

There are various types of infinite ordinals associated with well orderings on the natural numbers. The most common example is $$\omega$$. The ordering is $$0,1,2,3,4,...$$ Now, consider $$\omega + 1$$, which is $$1,2,3,4,5...0$$. We can continue going up and up.

## Challenge

Create a program (preferably python) that defines an ordering with the highest (countable) ordinal value.

More formally, your program should take in two distinct positive integers (so no 0) $$a$$ and $$b$$ and return true if and only if $$a < b$$ in some well ordering that has order type $$< \omega_{1}$$. Highest ordinal wins!

## Examples

Example of $$\omega$$:
```py
def relation(a, b):
  return a < b
```
This is of course the usual ordering of the positive integers.

Example of $$\omega + 1$$:
```py
def relation(a, b):
  if b == 1: return True
  if a == 1: return False
  return a < b
```
This is really bad way of doing this.

Example of $$\omega * 2$$:
```py
def relation(a, b):
  if b % 2 == a % 2: return a < b
  if b % 2 == 1: return False
  return True
```
The explanation on this is quite simple. We are aiming for $$1,3,5,7,9...2,4,6,8,10...$$ and thus if a and b have the same parity we compare them as so, if not and b is odd then a must be bigger, and if a is odd then b must be bigger.

## Submission

I don't really want to make a fancy submission portal. Just email to teammcpro3@gmail.com with a solution. There is no deadline. I may post a leaderboard here.

## Leaderboard

| Submitter    | Ordinal |
| -------- | ------- |
| shoesareme  | $$\omega * 2$$    |
| shoesareme | $$\omega + 1$$     |
| shoesareme    | $$\omega$$    |

## Notes

This was inspired by both [this](https://codegolf.stackexchange.com/questions/237291/infinite-ordinals-from-a-well-ordering) code golf post and [this](https://codegolf.stackexchange.com/questions/48931/make-the-largest-infinity-that-you-can) one. In fact, it is pretty much the same as the first one with the exception of the byte restraint. The second one is also really interesting and I may make a follow up on it!

## Some of my attempts

I will update this as I go.

## Update (12/22/2024)

I completely forgot about this. Whoopsies! I may revisit it soon, but I am busy with other things currently.
