def vowel_count(phrase):
    vowels = "aeiou"
    count = {}

    for char in phrase.lower():
        if char in vowels:
            count[char] = count.get(char, 0) + 1

    return count
