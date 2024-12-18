immutable_var = 1, 23.45, 'Pavel', True, [9,8,7,6]
print(immutable_var)
print(immutable_var[0])
# immutable_var[0] = 2 Изменять значение элементов котрежа, т.к. кортеж не поддерживает обращение по элементам.
immutable_var[-1][0] = 4 #тем не менее возможно изменять элементы внутри списка, который находится в кортеже
print(immutable_var)
mutable_list = [2 , 67.89, 'Klimov', False, [4,5,6,7]]
print(mutable_list)
mutable_list[0]= 3
mutable_list[-1]= 'Piton'
print(mutable_list)