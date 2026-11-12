def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower()in"aeiou":
            count += 1
    return count
text = input("enter a string:")
print("number of vowels:",count_vowels(text))
