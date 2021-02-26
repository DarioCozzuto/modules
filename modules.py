#Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

#To create a module just save the code you want in a file with the file extension .py:



#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name) 




#Now we can use the module we just created, by using the import statement:

#Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")






#Save this code in the file mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 





#Import the module named mymodule, and access the person1 dictionary:
import mymodule

a = mymodule.person1["age"]
print(a) 





#You can create an alias when you import a module, by using the as keyword:
#Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a) 





#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
#List all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x) 




#Import only the person1 dictionary from the module:
from mymodule import person1

print(person1["age"])

#When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
