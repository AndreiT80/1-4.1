immutable_var = (22,55,77,'окно',True,[1,2,3,4])
print( immutable_var )
immutable_var[5][1]=8
print(immutable_var)
#immutable_var[3]='дверь'    TypeError: 'tuple' object does not support item assignment
print(immutable_var)
#  кортеж относится к неизменяемым типам данных, тем не менее внутри он может содержать изменяемые типы.
#  Если обобщить, то кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные
#  типы данных.

# Создание изменяемых структур данных:
mutable_list = [ 33,'дверь',True]
print(mutable_list)
mutable_list [0]=55         #  изменяю первый элемент списка
mutable_list [1]='окно'     #  изменяю второй элемент списка
mutable_list [2]=75         #  изменяю третий элемент списка
print(mutable_list)
