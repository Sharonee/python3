#Types
from zipfile import structCentralDir

x = 10  #Int
y = "10"  #Strint
z = 10.1   #Float

student_grades = [9.1, 80, 77, 60] #list

print(x, y, z)
print((type(x)), (type(y)), (type(z)), type(student_grades))

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
dictionary_student_grades = {"marry": 99, "Amos": 87, "Dana": 69}
print(dictionary_student_grades.values())
print(dictionary_student_grades.keys())



