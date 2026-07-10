#loop is usedto execute a block of code repeadely until a condition becomess false or until all items are processed.
#use of loop
    #to reduce code repetition
    #to processcollection of data
    #to perform repested calculation
    #save time
#use for loop when we know the iteration
#use while loop when we repeat until a condition become false
#for loop
#it is used to repeat a block of code for each item in a sequence

#using range()
for x in range(5):
 print(x)

#print number from 1 to 6
 for x in range(1,7):
    print(x)

#loop through a list
fruits=["apple","mango","litchi"]
for i in fruits:
    print(i)

#loop through a string
name="priti"
for i in name:
    print(i)

#check even 
for i in range(1,11):
 if i%2==0:
   print(i)

#print odd number
for x in range(1,11,2):
    print(x)


#while loop

#print number from 1 to 5
i=1
while i<6:
    print(i)
    i=i+1

#print odd number
i=1
while i<11:
    print(i)
    i=i+2


