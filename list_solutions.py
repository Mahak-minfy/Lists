# List Operations
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []

# List Manipulation
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], []))         # Should return [1, 2, 3]
print(merge_sorted_lists([], [4, 5, 6]))         # Should return [4, 5, 6]

# List Comprehensions

def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

# Example usage:
print(generate_matrix(3, 3))  # Should return [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
print(generate_matrix(2, 2))  # Should return [[0, 0], [0, 1]]



# Nested Lists
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))  # Should return [[1, 4], [2, 5], [3, 6]]