def partition(lst, fn):
    return [[elem for elem in lst if fn(elem)], [elem for elem in lst if not fn(elem)]]


def is_even(num):
    return num % 2 == 0


def is_string(el):
    return isinstance(el, str)
