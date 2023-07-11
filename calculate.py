def calculate(operation, a, b, make_int=False, message="The result is"):
    result = None

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b

    if make_int:
        result = int(result)

    if result is not None:
        return f"{message} {result}"
    else:
        return None


print(calculate("multiply", 1.5, 2))
