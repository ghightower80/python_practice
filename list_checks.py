def list_check(lst):
    for item in lst:
        if not isinstance(item, list):
            return False
    return True


print(list_check([[1], [2, 3]]))
