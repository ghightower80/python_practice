def flip_case(phrase, to_swap):
    result = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            char = char.swapcase()
        result += char
    return result


print(flip_case("Aaaahhh", "a"))  # 'aAAAhhh'
