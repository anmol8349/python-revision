s = "I love Python programming very much"

words = s.split()      # Step 1
longest = words[0]     # Step 2

for word in words:     # Step 3
    if len(word) > len(longest):
        longest = word   # Step 4

print("Longest word:", longest)
