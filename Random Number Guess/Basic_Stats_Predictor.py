import random
from collections import Counter


def top_n_least_repeated_numbers(n, nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    counter = Counter(flat_list)
    least_n = counter.most_common()[:-n - 1:-1]  # Getting least common elements
    return [num for num, _ in least_n]


def top_n_most_repeated_numbers(n, nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    counter = Counter(flat_list)
    top_n = counter.most_common(n)
    return [num for num, _ in top_n]


# Generate three lists of five random numbers
list1 = [random.randint(1, 100) for _ in range(5)]
list2 = [random.randint(1, 100) for _ in range(5)]
list3 = [random.randint(1, 100) for _ in range(5)]

# Create a nested list containing all three lists
input_list = [list1, list2, list3]

print(input_list)

n = 3  # Top 3 most repeated numbers
top_n_numbers = top_n_most_repeated_numbers(n, input_list)
print(f"Top {n} most repeated numbers:", top_n_numbers)

least_n_numbers = top_n_least_repeated_numbers(n, input_list)
print(f"Top {n} least repeated numbers:", least_n_numbers)
