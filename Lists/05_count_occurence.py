# Write a Python function that takes a list and an element as input and counts how
# many times that element appears in the list.

def count(lst1, element):
    count = 0
    for i in lst1:
        if i == element:
            count += 1
    return count

# alternative using list comprehension time O(n) space O(n)
def count_1(lst1, element):
    return sum([1 for i in lst1 if i==element]) # sum of an empty list is considered as 0

# alternative using generator expression time O(n) space O(1)
def count_2(lst1, element):
    return sum(1 for i in lst1 if i == element)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 1]
    value = 1
    print(count(my_list, value))
    print(count_1(my_list, value))
    print(count_2(my_list, value))
