from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    flattened_list = []
    for i in array:
        if isinstance(i,list) and not isinstance(i, str):
            flattened_list.extend(flat_list(i))
        elif isinstance(i, (int, float)):
            flattened_list.append(i)
    return flattened_list


print("Example:")
print(list(flat_list([1, 2, 3])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("And that's how you collect all values from a nested list into a combined flat list")