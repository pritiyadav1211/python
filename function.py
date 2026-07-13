#function is resuable block of code that perform a specific task.
#we write a code once inside the function and call it whenever needed.
 
#syntax
#def function_name(parameters):   
#    #code to exexcute
#    return value
#def is the keyword used to define a function
#finction_name is the name of function
#parameters are inputs to the function.
#return sends a value back to the caller.

#functuon without parameter
# def greet():    
#     print("hello,world")
# greet()

#function with parameter
def add(a,b):
    return a+b
result=add(3,4)
print(result)

#function with default parametr
def greet(name="priti"):
    print("hello",name)
greet("deepika")

#function parameter and argument
#parameter is a variable written inside the function definition .it work as a placeholder
#example
#def add(a,b):
#   result(a+b)
#   print(result)
#here a and b are parameter

#argument is the actual value that we pass to a function when calling it.
def add(a,b):
    print(a+b)  #10,20 are argument
add(10,20)

#return statemnet is used inside a function to send a value back to the place where the fumction was called.abs
#it also ends the execution of the function.
#syntax
#def function-name():
#return value

#using print() only display the result
#print() shows the output on the screen, but it does mot send the value back to the program
def add(a,b):       #without return
    print(a+b)
result=add(4,5)
print(result)   # output 30 none

#using return = give value back and we can change\use it
def add(a,b):
    return(a+b)
result=add(10,20)
print(result)
print(result+5)

#function return multiple values at a time using the return statement
#when a function return multiple values,python automatically stores them as a tuple
#syntax
#def fun_name():
#    return value 1,value 2,value 3

def calculate(a,b):  #function pack method
    add=a+b
    sub=a-b
    mul=a*b
    return(add,sub,mul)
result=calculate(1,2)
print(result)


def calculate(a,b):  #function unpack method
    add=a+b
    sub=a-b
    mul=a*b
    return(add,sub,mul)
x,y,z=calculate(1,2)
print(x)
print(y)
print(z)

#python return a tuple bcoz a function can return only one object ,so python combines multiple values into one tuple object
def student():
    return(10,20,30)
result=student()
print(type(result))

#keyword argument ,,in this the order of argument does not matter bcox python matches values using parameter names.
#position argument,  depend on order
def student(name,age):
    print("name:",name)
    print("age:",age)
student(age=20,name="prit")




