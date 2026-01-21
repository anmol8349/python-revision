# A tuple is an ordered, immutable collection of items.
# allow duplicates


t = (1, 2, 3)


t = (5,)   # comma is REQUIRED ||| , nahi lagane me int  rhega type
print(type(t))   # <class 'tuple'>


# mixed

t = (1, "Anmol", 99.5, True)
print(t)


t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[2])   # 30
print(t[-1])  # 40 (last element)


t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)


# how to make tuple mutable

t = (10, 20, 30)
lst = list(t)        # convert to list
lst[1] = 99
t = tuple(lst)      # convert back to tuple
print(t)            # (10, 99, 30)


# traverse

t = (10, 20, 30)

for x in t:
    print(x)

print(len(t)) 


# /packing and unpacking


t = 10, 20, 30
print(t)


a, b, c = (10, 20, 30)
print(a)  # 10
print(b)  # 20
print(c)  # 30




t = (1, 2, 3, 4, 5)

a, *b, c = t
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5



# ------------------------------------------

# tuple has only two methods

t = (10, 20, 30, 20)

print(t.count(20))   # 2
print(t.index(30))   # 2






t = (10, 20, 30, 40, 50)

total = 0
for x in t:
    total += x

print("Sum =", total)





largest = t[0]        # assume first element is max

for x in t:
    if x > largest:
        largest = x

print("Max =", largest)
