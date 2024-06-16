def binary_search(list, item):
    if len(list) < 1:
        return None

    counter = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        counter += 1
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid, counter
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

print(binary_search(my_list, 23))
print(binary_search(my_list, 1))
print(binary_search(my_list, 12))
print(binary_search(my_list, 24))
print(binary_search(my_list, -1))
