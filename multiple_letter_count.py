def multiple_letter_count(phrase):
    letter_count = {}
    for letter in phrase:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count
