def titleize(phrase):
    """Return phrase in title case (each word capitalized)."""
    # Split the phrase into a list of words
    words = phrase.split()

    # Capitalize the first letter of each word and convert the rest to lowercase
    titleized_words = [word.capitalize() for word in words]

    # Join the titleized words back into a single string with spaces in between
    titleized_phrase = " ".join(titleized_words)

    # Return the titleized phrase
    return titleized_phrase
