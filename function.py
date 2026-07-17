#function is resuable block of code that perform a specific task.
#we write a code once inside the function and call it whenever needed.
 
#syntax
# #def function_name(parameters):   
# #    #code to exexcute
# #    return value
# #def is the keyword used to define a function
# #finction_name is the name of function
# #parameters are inputs to the function.
# #return sends a value back to the caller.

# #functuon without parameter
# # def greet():    
# #     print("hello,world")
# # greet()

# #function with parameter
# def add(a,b):
#     return a+b
# result=add(3,4)
# print(result)

# #function with default parametr
# def greet(name="priti"):
#     print("hello",name)
# greet("deepika")

# #function parameter and argument
# #parameter is a variable written inside the function definition .it work as a placeholder
# #example
# #def add(a,b):
# #   result(a+b)
# #   print(result)
# #here a and b are parameter

# #argument is the actual value that we pass to a function when calling it.
# def add(a,b):
#     print(a+b)  #10,20 are argument
# add(10,20)

# #return statemnet is used inside a function to send a value back to the place where the fumction was called.abs
# #it also ends the execution of the function.
# #syntax
# #def function-name():
# #return value

# #using print() only display the result
# #print() shows the output on the screen, but it does mot send the value back to the program
# def add(a,b):       #without return
#     print(a+b)
# result=add(4,5)
# print(result)   # output 9 none

# #using return = give value back and we can change\use it
# def add(a,b):
#     return(a+b)
# result=add(10,20)
# print(result)
# print(result+5)

# #function return multiple values at a time using the return statement
# #when a function return multiple values,python automatically stores them as a tuple
# #syntax
# #def fun_name():
# #    return value 1,value 2,value 3

# def calculate(a,b):  #function pack method
#     add=a+b
#     sub=a-b
#     mul=a*b
#     return(add,sub,mul)
# result=calculate(1,2)
# print(result)


# def calculate(a,b):  #function unpack method
#     add=a+b
#     sub=a-b
#     mul=a*b
#     return(add,sub,mul)
# x,y,z=calculate(1,2)
# print(x)
# print(y)
# print(z)

# #python return a tuple bcoz a function can return only one object ,so python combines multiple values into one tuple object
# def student():
#     return(10,20,30)
# result=student()
# print(type(result))

# #keyword argument ,,in this the order of argument does not matter bcox python matches values using parameter names.
# #position argument,  depend on order
# def student(name,age):  # keyword argument
#     print("name:",name)
#     print("age:",age)
# student(age=20,name="prit")

# #position argument
# def add(a,b):      #depend on order
#     print(a,b)
# add(5,10)

# # when we mix both then first we write position argumnet then keyword argument
# def student(name,age,city):
#     print(name,age,city)
# #student(name="priti",20,"delhi")  give error bcoz keyword argument come after position
# student("priti",age=20,city="delhi")

# def display(a,b):
#     print(a,b)
# display(a=10,20)   #syntax error bcoz first posiyion argument come

# def greet():
#     return "hello"
# print(greet())

#VARIABLE-length arguments:-
#we use them when we don't know in aadvance how many values will be passed to a function
#sometime we dont know the how many arguments will be passed to a function,,,in such case we use *args
# *args collect multiple value in tuple
#syntax
#def function_name(*args):
#  statement
def add(*number):
    sum=0
    for i in number:
        sum=sum+i
    print(sum)
add(1,2)
add(1,2,3,4)

def show_names(*names):
    for name in names:
        print(name)
show_names("jiya","priti","depika")

#you can combine regular parameter with *args
#regular parameter must come before *args
def student(name,*marks):
    print("name:",name)
    print("marks",marks)
student("priti",80,70,60)  # here priti assign to name,,,, remaining value assign to marks

#KEYWORD ARGUMENT in variable length-
#  .we use **arg,,,,,it store data in form of dictionary(key:value)
#syntax
#def function_name("**args")
#statement
#example

def students(**data):
    print(data)
students(name="priti",course="bca")

#accessing value using loop
def students(**details):
    for key,value in details.items():
        print(key,":",value)
students(name="priti",course="bca",age=19)

def students(**details):
    for key,value in details.items():
        print(key,value)
students(name="priti",course="bca",age=19)

##LOCAL AND GLOBAQL VARIABLES
#variable create inside function are called local variable.
language="python"
def my_function():
    print("language",language)
    print(language)
my_function()

count=0
def increase():
    global count
    count+=1
increase()
print(count)

##function documentation(docstring)
#it is a short description of what a function does.
#it is written inside a triple quotes(""")
##syntax
def function_name(parameters):
    """function documentation (docstring)"""
    statements

#example 1
def add(a,b):
    """this function add two number and returns the result."""
    return a+b
print(add(10,20))

#example 2
def square(number):
    """this function return the square of a number"""
    return number*number
print(square(5))
print(square.__doc__)  # this will write the statement what we write in documentation

##type hints in function
# type hint are used to indicate the excepted data type of function parameter and the return value.absthey make the code easier to raed and understand.
#it do not force the type at runtime,but thet make code easier to understand
# #syntax
def function_name(parameter:data_type)->return_type:
  statements
#example
def add(a:int,b:int)->int:
    return a+b
print(add(10,20))
#function returning nothing
def msg(name:str)->none:
    print("wlcm",name)
msg("priti")

##lambda function
#it is a small anonymous(nameless)function that is used to perform a simple operation in a singel line.
#it is called an anonymous function bcoz it is created without using the def keyword.
#syntax
lambda arguments:expression
  #lambda->keyword used to create a lampda function.
  #arguments->input values
  #expression->operation

add=lambda a,b:a+b
print(add(3,4))

square=lambda a:a*a
print(square(4))
#check even or odd
even=lambda n:n%2==0
print(even(5))
print(even(6))
#these are commomly used with function like map(),filter(),sorted()
 # 1] map() with lambda
 #map() applies a function to every elemement of an iterable(like a list) and teturn a map object.
 #syntax
#map(function,iterable)
#example
number=[1,2,3,4]
result=list(map(lambda x:x*x,number))   #map() appliesit to every element in the list
print(result)

#2]filter() with lambda-----it select only those element that satisfy a given condition.
#syntax------ filter(function,iterable)
#find even number
number=[1,2,3,4]
result=list(filter(lambda x:x%2==0,number))
print(result)

#3]sorted() with lambda function----it is used to sort elements of alist,tuple,or any iterable.
# a lambda function is often usedwith the key parameter to define a custom sorting rule.
#syntax
#sorted(iterable,key=lamba x:expression)
names={"ram","krishna","amit","riya"}
result=sorted(names,key=lambda x:len(x))
print(result)

#using  function with list in python 
#example--- function to print a list
def show_list(items):
    print(items)
num=[1.2,3,4]
show_list(num)

#function to find maximun element
def find_max(num):
    print(max(num))
nums=[5,7,4,9]
find_max(nums)

##function calling other function
#syntax
#def function1():
  #function2()
#def function2():
 #statements
def add(a,b):
    return a+b
def display():
    result=add(10,20)
    print("sum=",result)

display()

#NESTED FUNCTION
# a function inside another function
# . the outer function is called tje outer function.
#syntax
#def outer_function():
#    def inner_function():
#     statements
#inner_function

def outer():
    print("this is the outer function.")
    def inner():
        print("this is the inner function")
    inner()
outer()

def outer():
    def inner():
        print("hello")
    inner()
outer()  #correct
inner()  #error



 








