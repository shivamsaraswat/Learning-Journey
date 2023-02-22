"""Python program to get the largest number from a list of random numbers."""

def largest(arr):
    max_element = arr[0]

    for index in range(1, len(arr)):
        if arr[index] > max_element:
            max_element = arr[index]

    return max_element

print(largest(list(map(int, input("Enter a list of numbers: ").split()))))