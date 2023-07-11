def is_palindrome(phrase):
    phrase = phrase.replace(" ", "").lower()

    return phrase == phrase[::-1]
