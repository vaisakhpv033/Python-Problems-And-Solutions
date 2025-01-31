# Write Program to check whether given string is a palindrome (reads the same forwards and backwards).

def is_palindrome(word):
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1 
    return True

# alternative way using slicing
def is_palindrome_2(word):
    return word == word[::-1]

# alternative way using recursion
def is_palindrome_3(word):
    if len(word) <= 1:
        return True 
    return word[0] == word[-1] and is_palindrome_3(word[1:len(word)-1])

if __name__ == "__main__":
    word = "malayalam"
    print(is_palindrome(word))
    print(is_palindrome_2(word))
    print(is_palindrome_3(word))
