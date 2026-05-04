def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


def largest_number(numbers):
    return max(numbers) if numbers else None


def smallest_number(numbers):
    return min(numbers) if numbers else None


def remove_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def is_empty(numbers):
    return not numbers


def largest_odd(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return max(odd_numbers) if odd_numbers else None


def remove_indexes(numbers):
    indexes_to_remove = [0, 4, 5]
    for index in sorted(indexes_to_remove, reverse=True):
        if index < len(numbers):
            numbers.pop(index)
    return numbers


def sort_tuples(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])


def count_lowercase_letters(words):
    count = 0
    for word in words:
        for ch in word:
            if ch.islower():
                count += 1
    return count


def extract_exact_k_consecutive(numbers, k):
    result = []
    i = 0
    n = len(numbers)

    while i < n:
        current = numbers[i]
        count = 1
        j = i + 1

        while j < n and numbers[j] == current:
            count += 1
            j += 1

        if count == k:
            result.append(current)

        i = j

    return result


if __name__ == "__main__":

    # -------------------- PART A --------------------
    print("\n--- Part A: Integer List Operations ---")
    user_input = input("Enter integers separated by space: ")
    numbers = list(map(int, user_input.split()))

    print("Product:", multiply_list(numbers))
    print("Largest:", largest_number(numbers))
    print("Smallest:", smallest_number(numbers))
    print("Without Duplicates:", remove_duplicates(numbers))

    if is_empty(numbers):
        print("List is empty")
    else:
        print("List is not empty")

    largest_odd_num = largest_odd(numbers)
    if largest_odd_num is not None:
        print("Largest Odd Number:", largest_odd_num)
    else:
        print("No odd numbers found")

    print("After Removing Index 0,4,5:", remove_indexes(numbers.copy()))

    # -------------------- PART B --------------------
    print("\n--- Part B: Tuple List Sorting ---")
    n = int(input("Enter number of tuples: "))
    tuple_list = []

    for _ in range(n):
        values = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
        tuple_list.append(values)

    print("Sorted Tuples:", sort_tuples(tuple_list))

    # -------------------- PART C --------------------
    print("\n--- Part C: Word List Analysis ---")
    words = input("Enter words separated by space: ").split()
    print("Total Lowercase Letters:", count_lowercase_letters(words))

    # -------------------- PART D --------------------
    print("\n--- Part D: Consecutive Element Extraction ---")
    numbers_d = list(map(int, input("Enter integers separated by space: ").split()))
    k = int(input("Enter value of k: "))

    print("Elements appearing exactly", k, "times consecutively:",
          extract_exact_k_consecutive(numbers_d, k))