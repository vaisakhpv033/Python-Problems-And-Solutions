# Write a Python program that takes a list of numbers as input and calculates and prints the sum and average of those numbers

def sum_and_average(nums):
    total = sum(nums)
    avg = total / len(nums)
    print(total, avg)
    return total, avg 


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5] 
    sum_and_average(nums)