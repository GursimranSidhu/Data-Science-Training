import numpy as np

# 1.1 Create 1D array a
def create_array_a():
    a = np.random.randint(0, 100, size=10)
    return a

# 1.2 Create 2D array b
def create_array_b():
    b = np.random.randint(-10, 11, size=(3,4))
    return b

# 1.3 Flatten array b
def flatten_b(b):
    b_flat = b.flatten()
    return b_flat

# 1.4 Copy array a and modify first element
def copy_and_modify_a(a):
    a_copy = a.copy()
    a_copy[0] = -1
    return a_copy

# 1.5 Create array c from every second element of a
def create_array_c(a):
    c = a[::2]
    return c


# 2.1 Third element of a
def third_element_a(a):
    return a[2]

# 2.2 Last element of b
def last_element_b(b):
    return b[-1, -1]

# 2.3 First two rows and last two columns of b
def slice_b(b):
    return b[:2, -2:]

# 2.4 Second row of b
def get_b_row(b):
    b_row = b[1, :]
    return b_row

# 2.5 First column of b
def get_b_col(b):
    b_col = b[:, 0]
    return b_col


# 3.1 Create array d
def create_array_d():
    d = np.arange(1, 11)
    return d

# 3.2 Add arrays a and d element-wise
def add_arrays(a, d):
    e = a + d
    return e

# 3.3 Multiply b by 2
def double_b(b):
    b_double = b * 2
    return b_double

# 3.4 Matrix multiplication
def matrix_multiplication(b, b_double):
    f = np.matmul(b, b_double.T)
    return f

# 3.5 Mean values
def calculate_means(a, b, b_double):
    a_mean = np.mean(a)
    b_mean = np.mean(b)
    b_double_mean = np.mean(b_double)

    g = np.array([a_mean, b_mean, b_double_mean])
    return g


# 4.1 Sum of a
def sum_a(a):
    return np.sum(a)

# 4.2 Minimum of b
def min_b(b):
    return np.min(b)

# 4.3 Maximum of b_double
def max_b_double(b_double):
    return np.max(b_double)


# Main block
if __name__ == "__main__":

    a = create_array_a()
    b = create_array_b()

    b_flat = flatten_b(b)
    a_copy = copy_and_modify_a(a)
    c = create_array_c(a)

    third = third_element_a(a)
    last = last_element_b(b)
    b_slice = slice_b(b)
    b_row = get_b_row(b)
    b_col = get_b_col(b)

    d = create_array_d()
    e = add_arrays(a, d)

    b_double = double_b(b)
    f = matrix_multiplication(b, b_double)

    g = calculate_means(a, b, b_double)

    a_sum = sum_a(a)
    b_min = min_b(b)
    b_double_max = max_b_double(b_double)


    print("Array a:", a)
    print("Array b:\n", b)

    print("Flattened b:", b_flat)
    print("Modified copy of a:", a_copy)
    print("Array c:", c)

    print("Third element of a:", third)
    print("Last element of b:", last)

    print("First two rows and last two columns of b:\n", b_slice)

    print("Second row of b:", b_row)
    print("First column of b:", b_col)

    print("Array d:", d)
    print("Array e (a + d):", e)

    print("b multiplied by 2:\n", b_double)

    print("Matrix multiplication result f:\n", f)

    print("Means array g:", g)

    print("Sum of a:", a_sum)
    print("Minimum of b:", b_min)
    print("Maximum of b_double:", b_double_max)