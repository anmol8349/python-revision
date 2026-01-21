s = "Python"
print(len(s))   # 6


s = "banana"
print(s.count("a"))   # 3
print(s.count("b"))   # 1
print(s.count("z"))   # 0


s = "Apple"
print(s.count("a"))   # 0
print(s.count("A"))   # 1


s= "programming"

freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
        
    else:
        freq[ch]=1


print(freq)

for ch in sorted(freq, key=freq.get):
    print(ch, ":", freq[ch])

#   without dic------------

s = "banana"

for ch in s:
    print(ch, ":", s.count(ch))



# unique only -------

print("unique only ")

s = "banana"
seen = ""

for ch in s:
    if ch not in seen:
        print(ch, ":", s.count(ch))
        seen += ch
