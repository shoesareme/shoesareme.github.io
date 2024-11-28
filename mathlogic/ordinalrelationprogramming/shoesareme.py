# These are my attempts at my own challenge.

# omega
def relation1(a, b):
  return a < b

# omega + 1
def relation2(a, b):
  if b == 1: return True
  if a == 1: return False
  return a < b

# omega * 2
def relation(a, b):
  if b % 2 == a % 2: return a < b
  if b % 2 == 1: return False
  return True
