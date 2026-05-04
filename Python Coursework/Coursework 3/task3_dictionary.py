def sort_dictionary_by_value(data_dict):
    ascending = dict(sorted(data_dict.items(), key=lambda item: item[1]))
    descending = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
    return ascending, descending


def iterate_dictionary(data_dict):
    keys = []
    values = []
    key_value_pairs = []

    for key in data_dict:
        keys.append(key)

    for value in data_dict.values():
        values.append(value)

    for key, value in data_dict.items():
        key_value_pairs.append((key, value))

    return keys, values, key_value_pairs


def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def calculate_sum(data_dict):
    if not data_dict:
        return 0
    total = 0
    for value in data_dict.values():
        total += value
    return total


def calculate_product(data_dict):
    if not data_dict:
        return 0
    product = 1
    for value in data_dict.values():
        product *= value
    return product


def sort_dictionary_by_key(data_dict):
    return dict(sorted(data_dict.items(), key=lambda item: item[0]))


def remove_duplicate_values(data_dict):
    seen_values = set()
    result = {}

    for key, value in data_dict.items():
        if value not in seen_values:
            seen_values.add(value)
            result[key] = value

    return result


def input_dictionary():
    n = int(input("Enter number of key-value pairs: "))
    data = {}

    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = int(input(f"Enter numeric value for {key}: "))
        data[key] = value

    return data


if __name__ == "__main__":

    print("\n--- Part A: Sorting by Value ---")
    dict_a = input_dictionary()
    asc, desc = sort_dictionary_by_value(dict_a)
    print("Ascending by value:", asc)
    print("Descending by value:", desc)

    print("\n--- Part B: Iterating Through Dictionary ---")
    keys, values, pairs = iterate_dictionary(dict_a)
    print("Keys:", keys)
    print("Values:", values)
    print("Key-Value Pairs:", pairs)

    print("\n--- Part C: Merging Dictionaries ---")
    print("First Dictionary:")
    dict1 = input_dictionary()
    print("Second Dictionary:")
    dict2 = input_dictionary()
    merged = merge_dictionaries(dict1, dict2)
    print("Merged Dictionary:", merged)

    print("\n--- Part D: Aggregation Operations ---")
    print("Sum of values:", calculate_sum(dict_a))
    print("Product of values:", calculate_product(dict_a))

    print("\n--- Part E: Sorting by Key ---")
    sorted_by_key = sort_dictionary_by_key(dict_a)
    print("Sorted by key:", sorted_by_key)

    print("\n--- Part F: Removing Duplicate Values ---")
    no_duplicates = remove_duplicate_values(dict_a)
    print("After removing duplicate values:", no_duplicates)