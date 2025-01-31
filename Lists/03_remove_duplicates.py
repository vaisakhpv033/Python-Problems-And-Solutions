# Create a Python function that takes a list as input and removes duplicate
# elements, preserving the order of the elements. Return the new list

def remove_duplicates(lst):
    new_lst = []
    cache = set()
    for i in lst:
        if i not in cache:
            new_lst.append(i)
            cache.add(i)
    return new_lst 

# alternative
def remove_duplicates_1(lst):
    return list(dict.fromkeys(lst))

if __name__ == "__main__":
    my_lst = [1, 2, 3, 4, 4, 4, 2, 2, 5, 8, 9, 10, 2]
    print(remove_duplicates_1(my_lst))
        