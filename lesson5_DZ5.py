# Задача 1

my_int = 2304503000
my_int = str(my_int)
print(my_int.count("0"))

##########################################
# Задача 2

my_int = 230450300
count = 0
while True:
    if my_int % 10 == 0:
        count += 1
        my_int = my_int // 10
        if my_int % 10 > 0:
            break
print(count)
#############################################
# Задача 3

my_list_1 = [2, 4, 6, 8, 10]
my_list_2 = [2, 4, 6, 8, 10]
my_result = []
for index, my_val_1 in enumerate(my_list_1):
    if index % 2 == 0:
        my_result.append(my_val_1)
for index, my_val_2 in enumerate(my_list_2):
    if index % 2 != 0:
        my_result.append(my_val_2)
print(my_result)
#############################################
# Задача 4
my_list = [1, 2, 3, 4]
my_list_new = []
for value in my_list:
    my_list_new.append(value)
my_list_new.insert(len(my_list_new), my_list_new.pop(0))
print(my_list_new)
############################################################
# Задача 5
my_list = [1, 2, 3, 4]
my_list.insert(len(my_list), my_list.pop(0))
print(my_list)
#############################################################
# Задача 6
my_str = "43 больше чем 34 и больше чем 39"
my_str = my_str.split()
my_list = []
for value in my_str:
    if value.isdigit():
        my_list.append(int(value))
print(sum(my_list))
#############################################################
#Задача 7

my_str = "abcd"
n = 2
my_list = []
for a in range(0, len(my_str), n):
    my_list.append(my_str[a:a+n])
print(my_list)
###########################################
# Задача 8
my_str = "My long string"
l_limit = "o"
r_limit = "t"
sub_str = my_str[(my_str.index("o")) + 1:my_str.index("t")]
print(sub_str)
#################################################################
# Задача 9
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[(my_str.index("o")) + 1:my_str.rindex("g")]
print(sub_str)




# Задача 10
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for x in range(1, len(my_list) - 1):
    if my_list[x-1] < my_list[x] > my_list[x+1]:
        count += 1
print(count)





















