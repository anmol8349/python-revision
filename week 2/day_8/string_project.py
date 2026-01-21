def count_words(s):
    words = s.split()
    print("Total words:", len(words))


def longest_word(s):
    words = s.split()
    
    if not words:
        print("String is empty!")
        return
    
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    print("Longest word:", longest)
    print("Length:", len(longest))


def char_frequency(s):
    freq = {}
    
    for ch in s:
        if ch != " ":   # ignore spaces
            freq[ch] = freq.get(ch, 0) + 1
    
    print("Character Frequency:")
    for ch, count in freq.items():
        print(ch, ":", count)


def remove_duplicates(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
    
    print("After removing duplicates:", result)


# 🔹 Main Menu Loop
while True:
    print("\n--- STRING MENU ---")
    print("1. Count words")
    print("2. Find longest word")
    print("3. Character frequency")
    print("4. Remove duplicate characters")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting program...")
        break

    s = input("Enter a string: ")

    if choice == "1":
        count_words(s)

    elif choice == "2":
        longest_word(s)

    elif choice == "3":
        char_frequency(s)

    elif choice == "4":
        remove_duplicates(s)

    else:
        print("Invalid choice! Please enter 1-5.")



