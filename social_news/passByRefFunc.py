my_list = [1, 2, 3, 4]
my_var = 5


#####################################################


def minus_one(var):
    var -= 1

    print("-----")
    print(var)
    print("-----")


minus_one(my_var)
print(my_var)


#####################################################


def remove_one(a_list):

    a_list.pop(0)


remove_one(my_list)
print(my_list)


#####################################################


def remove_one_different(a_list):

    a_list = a_list[:4]


remove_one_different(my_list)
print(my_list)
