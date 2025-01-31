# Write a program to remove duplicate values in the given string.

def remove_duplicate(word):
    new_list = [] 
    for i in word:
        if i not in new_list:
            new_list.append(i)
    return ''.join(new_list)


if __name__ == "__main__":
    word = "hello"
    print(remove_duplicate(word))
