from random import randint


def binary_search(my_list, value):
    lower_line = 0
    upper_line = len(my_list) - 1
    while lower_line <= upper_line:
        center = (lower_line+upper_line) // 2
        if my_list[center] == value:
            return center
        elif my_list[center] > value:
            upper_line = center - 1
        elif my_list[center] < value:
            lower_line = center + 1

    return -1


x = [randint(0, 10) for a in range(10)]
x = sorted(x)
print(x)
print(binary_search(x, 5))




