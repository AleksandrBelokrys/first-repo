# Задание 1
value = 68
new_value = value // 2 if value < 100 else -value
print(new_value)
###########################################################
# Задание 2
value = 98
new_value = 1 if value < 100 else 0
print(new_value)
#############################################################
# Задание 3
value = 99
new_value = True if value < 100 else False
print(new_value)
#############################################################
# Задание 4
my_str = "qwerty"
my_str = my_str.upper()
print(my_str)
##############################################################
# Задание 5
my_str = "QWERTY"
my_str = my_str.lower()
print(my_str)
##############################################################
# Задание 6
my_str = "qwer"
my_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_str)
##############################################################
# Задание 7
my_str = "qwer"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
##############################################################
# Задание 8
my_str = "qwer  ty  123456 .,..,,.,.//"
for symbol in my_str:
    if symbol.isalnum():
        print(symbol)
################################################################
# Задание 9
my_str = "qwer ty 123456 .,..,,.,.//"
for symbol in my_str:
    if not symbol.isalnum():
        print(symbol)
################################################################
#Задание 10
my_str = "qwer           ty  123456 .,..,,.,.//"
for symbol in my_str:
    if not symbol.isalnum() and not symbol.isspace():
        print(symbol)
