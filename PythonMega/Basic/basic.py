#Types
from zipfile import structCentralDir

x = 10  #Int
y = "10"  #Strint
z = 10.1   #Float

student_grades = [9.1, 80, 77, 60] #list
Temperatures = (50, 40, 7) #Tuple

print(x, y, z, Temperatures)
print((type(x)), (type(y)), (type(z)), type(student_grades), type(Temperatures))

# DIR package
print("hello".upper())
print("hello".title())

#Method VS Function
#Print is a Fuction ( Dont need use dot) print("test")
#upper is a Method ("hello".upper())

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#Dictionary Types
#Dictionaries represent pairs of keys and values:
dictionary_student_grades = {"marry": 99, "Amos": 87, "Dana": 69}
print(dictionary_student_grades.values())
print(dictionary_student_grades.keys())

#Tuple type
#Double canot append or remove item like  a list
#Tuples represent arrays of values that are not to be
# changed during the course of the program:
Ages = (50, 40, 7) #Tuple

'''
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)

To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)
'''
