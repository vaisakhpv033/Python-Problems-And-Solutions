# Write a Python function that takes a list and returns a new list with the elements
# reversed. Do this without using the built-in reverse method.

def reverse(lst):
    return lst[:: -1]


if __name__ == "__main__":
    my_list = ['a', 1, 2, 3, 4, "hello"]
    print(reverse(my_list))