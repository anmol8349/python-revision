# A set is a collection of unique and unordered elements.
# Mutable
# Much faster than lists for searching
# sets ignore order & duplicates.


s = {1, 2, 3, 4,4}
print(s)

s = set([1, 2, 2, 3, 4])
print(s)   # {1, 2, 3, 4}


s = {}      # This creates a dictionary
s = set()


# s = {10, 20, 30}
# print(s[0])   # ❌ Error :  cannot use indexing:


for item in s:
    print(item)


s = {1, 2}
s.add(3)
print(s)   # {1, 2, 3}

s.update([4, 5, 6]) #multiple add
print(s)


# ------------removing --
s2 = {1, 2, 3, 4}

s2.remove(2)
s2.discard(10)  # no error
s2.pop()   #Removes random element
s2.clear()  #Empties set

# -------------------



s = {10, 20, 30}

print(20 in s)     # True
print(40 in s)     # False


# -------- remove duplicates---of list ----

nums = [1, 2, 2, 3, 4, 4, 5]

unique_nums = list(set(nums))
print(unique_nums)

# Set Comprehension (Like List Comprehension)


squares = {x*x for x in range(1, 6)}
print(squares)



# -----Frozen Set (Immutable Set)
# Used when don’t want data to change.


fs = frozenset([1, 2, 3])
# fs.add(4)  ❌ Error
print(fs)




a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.isdisjoint(b))

if a & b:
    print("Not disjoint")
else:
    print("Disjoint")


word = "programming"
unique_letters = set(word)
print(unique_letters)


word = "programming"
unique_letters = list(dict.fromkeys(word)) #  withh order
print(unique_letters)

