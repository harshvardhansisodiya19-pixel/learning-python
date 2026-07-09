#   DICTIONARY AND SETS
# It is unorderd mutable indexed and cannot contain duplucate keys
marks={"Harry":100,
    "Shubham":56,
    "Rohan":23,
    0:"Harsh"
}
# print(marks, type(marks))
# print(marks[0]) error
print(marks["Harry"])
#Dictionary ka fayda => fast lokup
#It is indexed doesnt run everything directly goes to indexed value
#DICTIONARY METHODS
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99,"Renuka":100})#Updates the dictionary since its mutable and does which are not present is added
print(marks.get("Harry2"))#Prints NONE
# print(marks["Harry2"])# Ye wali error degi if not in dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    "Harsh": 99
}

# Print the whole dictionary
print("Original Dictionary:")
print(marks)

# ---------------------------
# keys() -> Returns all keys
# ---------------------------
print("\nKeys:")
print(marks.keys())

# -----------------------------
# values() -> Returns all values
# -----------------------------
print("\nValues:")
print(marks.values())

# items() -> Returns key-value pairs------
print("\nItems:")
print(marks.items())

# get() -> Returns value of a key
# Returns None if key does not exist---------
print("\nUsing get():")
print(marks.get("Harry"))
print(marks.get("Rahul"))    # None

# [] -> Gives KeyError if key doesn't exist---------
print("\nUsing []:")
print(marks["Harry"])
# print(marks["Rahul"])   # Uncomment to see KeyError

# update() -> Updates/Adds key-value pairs------
marks.update({"Harry": 95, "Renuka": 100})

print("\nAfter update():")
print(marks)

# -------------------------------
# pop() -> Removes a specific key
# -------------------------------
marks.pop("Rohan")

print("\nAfter pop('Rohan'):")
print(marks)

# popitem() -> Removes last inserted item--
marks.popitem()

print("\nAfter popitem():")
print(marks)

# copy() -> Creates a shallow copy
new_marks = marks.copy()

print("\nCopied Dictionary:")
print(new_marks)

# setdefault() -> Returns value if key exists
# Otherwise inserts key with default value
print("\nUsing setdefault():")
print(marks.setdefault("Aman", 75))
print(marks)

# clear() -> Removes all items
temp = marks.copy()
temp.clear()

print("\nAfter clear():")
print(temp)

# len() -> Number of key-value pairs
print("\nLength of dictionary:")
print(len(marks))
