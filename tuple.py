#Tuple is a data type used tgo store multiple values in a singel variable
# syntax of tupple
num=(10,55,12,34,55,56)

#unpack method
n1,n2,*n3=num  
print(n1)
print(n2)
print(n3)
print(num)

#type function
print(type(num))

#index function
print(num.index(55))  #to find the position of an element

#if we have 2 same value and want to know the index of 2nd value
first=num.index(55)
second=num.index(55,first+1)
print(second)

#count function
print(num.count(55))

#conversion of tuple into list
num1=list(num)
print(num1)  #covert into list
num1.insert(2,34)
print(num1)
num1.remove(12)
print(num1)
num=tuple(num1)  #list convert into tupl4e
print(num)

#if we want to print singal element in a tuple we use comma bcoz if we write it wiyhout comma it is consider as integer
a=(2,)
print(a)

#slice method
print(num[2:6])
 
   



