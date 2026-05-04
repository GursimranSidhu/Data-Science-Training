def create_mixed_tuple():
    num = int(input("Enter an integer: "))
    decimal = float(input("Enter a float number: "))
    string = input("Enter a string: ")
    boolean = input("Enter boolean value (True/False): ")
    boolean = boolean.lower() == "true"

    return (num, decimal, string, boolean)


def access_tuple_element():
    numbers = tuple(map(int, input("Enter at least 5 numbers separated by space: ").split()))

    if len(numbers) < 5:
        return "Please enter at least 5 numbers."

    index = int(input("Enter index to access: "))

    if 0 <= index < len(numbers):
        return f"Value at index {index} is {numbers[index]}"
    else:
        return "Index out of range."


def get_fourth_from_end():
    numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

    if len(numbers) >= 4:
        return numbers[-4]
    else:
        return "Tuple contains fewer than 4 elements."


def add_item_to_tuple():
    original_tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))
    new_item = int(input("Enter the number you want to add: "))

    new_tuple = original_tuple + (new_item,)
    return original_tuple, new_tuple


def convert_tuple_to_dictionary():
    data = eval(input("Enter a tuple: "))

    try:
        result = dict(data)
    except:
        result = dict(enumerate(data))

    return result


def replace_last_element_in_tuples():
    n = int(input("Enter number of tuples: "))
    tuples_list = []

    for i in range(n):
        values = tuple(map(int, input(f"Enter elements of tuple {i+1}: ").split()))
        tuples_list.append(values)

    updated_list = []

    for t in tuples_list:
        if len(t) > 0:
            new_tuple = t[:-1] + (100,)
            updated_list.append(new_tuple)
        else:
            updated_list.append(t)

    return updated_list


if __name__ == "__main__":

    print("\n--- Create Mixed Data Type Tuple ---")
    print("Created Tuple:", create_mixed_tuple())

    print("\n--- Access Tuple Element ---")
    print(access_tuple_element())

    print("\n--- Retrieve 4th Element From End ---")
    print("Result:", get_fourth_from_end())

    print("\n--- Add Item To Tuple ---")
    original, updated = add_item_to_tuple()
    print("Original Tuple:", original)
    print("Updated Tuple:", updated)

    print("\n--- Convert Tuple To Dictionary ---")
    print("Dictionary:", convert_tuple_to_dictionary())

    print("\n--- Replace Last Element With 100 ---")
    print("Updated List:", replace_last_element_in_tuples())