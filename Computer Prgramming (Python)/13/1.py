def list_number(list, num):
    if not list:
            return False
    return list[-1] == num or list_number(list[:-1], num)

list = [1,2,3,4,5,6]
print(list_number(list, 3))
print(list)
