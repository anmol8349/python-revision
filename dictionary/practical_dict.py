data=[2,2,3,2,98,5]

freq={}

for x in data:
    freq[x] = freq.get(x,0)+1
    
print(freq)


text="python is easy and python is powerfull"
words = text.split()

count={}

for w in words:
    count[w]=count.get(w,0)+1
    
print(count)



d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = {**d1, **d2}
print(d3)
