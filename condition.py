#CONDITION in python is an expression that evaluate to either true or false.
#These are used to make decision in a program.

#if statemet=== it is used to execute a block of code only when a condition true.
age=19
if age>=18:
    print("eligible for vote")    # if condition is not true then it will not produce any output

 #if else statement is used to execute block of code when the condition is true and another whwn the condition is false
number=10
if number%2==0:
    print("even number")
else:
    print("odd number")

#if elif else is used when you need to check multiple conditions.
age=19
if age>=60:
    print("senior citizen")
elif age>=18:
    print("adult")
elif age>=13:
    print("teenager")
else:
    print("child")

#nested if ===it means placing one if statement inside another if statement.
#it is used when a second condition should be checked only if the first is true.


a=4
b=5
c=6
if a>b:
    if(b>a):
        print("b is greater")
    else:
        print("a is greater")
else:
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")

#example 2
age=17
pass_id=True
if(age>=18):
    if(pass_id):
        print("entery allowed")
    else:
        print("not eligible")
else:
    print("canot vote")