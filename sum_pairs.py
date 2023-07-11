def sum_pairs(nums, goal):
    seen = set()

    for num in nums:
        complement = goal - num
        if complement in seen:
            return (complement, num)
        seen.add(num)

    return ()


print(sum_pairs([1, 2, 2, 10], 4))  # (2, 2)
