import random


def my_print(x) -> str:
    return "***" + x + "***"


def my_print_1(x: str, y="*"):
    return f"{y.ljust(len(x), '*')}\n{x}\n{y.ljust(len(x), '*')}"


def my_print_2(x: str, y="*", c="***"):
    return f"{y.ljust(len(c+x+c), '*')}\n{c+x+c}\n{y.ljust(len(c+x+c), '*')}"


#Задача 1
my_list = [i for i in range(1, 100)]
my_list = random.sample(my_list, 20)
print(my_list)
#################################################
#Задача 2
triangle = {"A": (random.randint(0, 9), random.randint(0, 9)),
            "B": (random.randint(-8, 9), random.randint(0, 9)),
            "C": (random.randint(0, 9), random.randint(0, 9))
            }
print(triangle)
##################################################
#Задача 3
my_str = "I'm the string"
print(my_print(my_str))
###################################################
# Задача4
my_str_1 = "I'm the string"
print(my_print_1(my_str_1))
####################################################
# Задача 5
my_str_2 = "I'm the string"
print(my_print_2(my_str_2))


