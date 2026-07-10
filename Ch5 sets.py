#Set is a collection of well defined objects
s={1,5,32,54,5,5,5,"Harry"} #d{}= empty dictionary  e=set() don't use s={} this is empt dictionary not empty set
print(s)#Har value ek hi baar print hui
print(s,type(s))
s.add(566)
print(s,type(s))
s2={7,8,1,78}
print(s.union(s2))
print(s.intersection(s2))
#s.pop()to remove
#s.remove()
#len(s) tells about length of set
print(s-s2)
print(s2-s)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# add() -> Adds one element
A.add(10)
print("\nAfter add(10):")
print(A)

# update() -> Adds multiple elements
A.update([11, 12, 13])
print("\nAfter update([11, 12, 13]):")
print(A)

# remove() -> Removes an element (KeyError if not found)
A.remove(13)
print("\nAfter remove(13):")
print(A)

# discard() -> Removes an element (No error if not found)
A.discard(100)
print("\nAfter discard(100):")
print(A)

# pop() -> Removes a random element
removed = A.pop()
print("\nRemoved using pop():", removed)
print(A)

# copy() -> Creates a copy
C = A.copy()
print("\nCopied Set:")
print(C)

# union() -> Combines both sets
print("\nUnion:")
print(A.union(B))
print(A | B)

# intersection() -> Common elements
print("\nIntersection:")
print(A.intersection(B))
print(A & B)

# difference() -> Elements in A but not in B
print("\nDifference (A - B):")
print(A.difference(B))
print(A - B)

# symmetric_difference() -> Elements in either set but not both
print("\nSymmetric Difference:")
print(A.symmetric_difference(B))
print(A ^ B)

# issubset() -> Checks if one set is a subset of another
print("\nSubset:")
print({4, 5}.issubset(B))

# issuperset() -> Checks if one set is a superset of another
print("\nSuperset:")
print(B.issuperset({4, 5}))

# isdisjoint() -> True if no common elements
print("\nDisjoint:")
print({100, 200}.isdisjoint(B))

# len() -> Number of elements
print("\nLength:")
print(len(A))

# in / not in -> Membership operators
print("\nMembership:")
print(5 in B)
print(100 not in B)

# clear() -> Removes all elements
temp = B.copy()
temp.clear()
print("\nAfter clear():")
print(temp)