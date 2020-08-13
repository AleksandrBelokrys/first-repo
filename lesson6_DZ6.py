#Задача 1
my_list = ["qwe", "rty", "ewq", "ytr", "wrt"]
my_list_new = []
for index, value in enumerate(my_list):
    if index % 2:
        my_list_new.append(value[::-1])
    else:
        my_list_new.append(value)
print(my_list_new)
###################################################
#Задача 2
my_list = ["qae", "aty", "awq", "yar", "art", "att", "daf", "fdf", "dra"]
my_list_new = []
for value in my_list:
    if not value.find("a"):
        my_list_new.append(value)
print(my_list_new)


######################################################
#Задача 3
my_list = ["qwe", "aty", "waq", "ytr", "art", "fda"]
my_list_new = []
for value in my_list:
    if "a" in value:
        my_list_new.append(value)
print(my_list_new)
######################################################
#задача 4
my_list = ["qwe", 8, "waq", "ytr", 9, "fda"]
my_list_new = []
for value in my_list:
    if type(value) == str:
        my_list_new.append(value)
print(my_list_new)
#######################################################
# Задача 5
my_str = "qqqqweerttttyyyyassssdffffghhkkk"
my_str_set = set(my_str)
for value in my_str_set:
    if my_str.count(value) == 1:
        print(value)
#######################################################
# Задача 6
my_str_1 = "qwerty"
my_str_2 = "qwerty123456789"
set_1, set_2 = set(my_str_1), set(my_str_2)
set_new = set_1.intersection(set_2)
print(set_new)
########################################################
# Задача 7
my_str_1 = "qweertyy"
my_str_2 = "qweertyy123456789"
set_1, set_2 = set(my_str_1), set(my_str_2)
for value in my_str_1:
    if my_str_1.count(value) > 1:
        set_1.discard(value)
        for value_2 in my_str_2:
            if my_str_2.count(value_2) > 1:
                set_2.discard(value_2)
print(set_1.intersection(set_2))
#########################################################
# Задача 8
person = {"LastName": "Bilokrys",
          "Name": "Aleksandr",
          "Age": 29,
          "Address": {"Country": "Ukraine",
                      "City": "Kryvyi Rih",
                      "Street": "Tynka"},
          "Job": {"Availability": "yes",
                  "Position": "Owner"}

          }
print(person)
###########################################################
#Задача 9

cake_recipe = {"Коржи": {"Мука": "600 г",
                         "Молоко": "250 г",
                         "Масло": "150 г",
                         "Яйцо": "4 шт"
                         },
               "Крем": {"Сахар": "300 г",
                        "Масло": "150 г",
                        "Ваниль": "1 пакетик",
                        "Сметана": "250 г"
                        },
               "Глазурь": {"Какао": "150 г",
                           "Сахар": "200 г",
                           "Масло": "100 г"}

               }

print(cake_recipe)











