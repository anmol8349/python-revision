sq={x: x*x for x in range (1,6)}
print(sq)

even_sq={x :x*x for x in range (1,11) if x%2==0}
print(even_sq)

d = {"b": 2, "a": 5, "c": 3}

print(dict(sorted(d.items())))


print(dict(sorted(d.items(), key=lambda x: x[1])))
