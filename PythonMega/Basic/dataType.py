#List of Methods
'''
dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__
format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__i
nit__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '_
_reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__size
of__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'po
p', 'remove', 'reverse', 'sort']
'''

#HELP
'''
>>> help(list.append)
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.
'''

temp_list = [50, 20, 30, 99]
temp_list.append(80)
print(temp_list)

# temp_list.clear()
# print(temp_list)

print( temp_list.index(80))

print(temp_list.__getitem__(2))

print("length of the list")
print(len(temp_list))

print("present a slice of a list")
print(temp_list)
print(temp_list[1:3]) #Present slice of a list

print("get last item with negative index")
print(temp_list)
print(temp_list[-1])

print("Characters index")
multi_list = ['hello', 2, 5]
print(multi_list)
print(multi_list[0][2])


