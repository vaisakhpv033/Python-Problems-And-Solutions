# Create a Python program that takes two lists and returns a new list containing
# elements that are common in both input lists.

def common(lst1, lst2):
    new_lst = [] 
    for i in lst1:
        if i in lst2:
            new_lst.append(i)
    return new_lst 

# alternative
def common_2(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 0, 8]
    print(common(list1, list2))
    print(common_2(list1, list2))