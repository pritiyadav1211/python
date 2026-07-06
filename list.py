#List==used to store multiple value in a singel variable.
# list are ordered,changebale,can contain duplicate value

#syntax
number=[1,2,5,6,7,86]
print(number)

#access through index
print(number[4])
print(number[-3])

#length function
print(len(number))

#type function
print(type(number))

#to add number at last
number.append(76)
print(number)

#insert number at a specific position
number.insert(2,12)
print(number)

#to remove a number from index
number.remove(5)
print(number)

#delete an element 
number.pop()
print(number)

#to sort the list
number.sort()
print(number)

#to reverse the list
number.reverse()
print(number)
print(number[3])
number[3]=56
print(number)

#slice function
print(number[2:4])

#using for loop in list
for i in number:
    print(i)

#adding two list
a=[2,4,5]
b=[4,5,6]
c=a+b
print(c)

#repetition two list
rep=2*a
print(rep)



