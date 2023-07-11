def is_odd_string(word):
    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())
