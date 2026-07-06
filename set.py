#set is a collection of unique and unordered elements
#set is mutable
#not allow duplicacy
#syntax
set={1,2,3,4,5}
print(set)

#access elements using for loop
for x in set:
    print(x)

#update element
name={"red","green"}
name1=["1","2","3"]
name.update(name1)
print(name)

#add element
name.add("yellow")
print(name) 

# #remove element ,if value not found it give value error
name.remove("red")
print(name)

#discard method,remove element but when not found does not found an error
name.discard("blue")
print(name)

#clear method
name.clear()
print(name)

#delete method
del name

#copy method==create a copy of the set
a={"apple","banana","mango","cherry"}
b=a.copy()
print(b)

# union method ==join two set
s1={1,2,3,4}
s2={3,4,5,77}
print(s1.union(s2))

#intersection method=common value will appear
s1={1,2,3,4}
s2={2,3,6,7}
print(s1.intersection(s2))

#difference method=return that are in first not in second
a={3,4,5,6}
b={6,7,8}
print(b.difference(a))

#issubset==it means all element are present or not
a={1,2}
b={2,3,1}
print(a.issubset(b)) 
print(b.issubset(a))

#issuperset==it means all element+extra element
a={1,2,3}
b={1,2}
print(a.issuperset(b))
print(b.issuperset(a))

#isdisjoint==checks wheteher two set have common element or not
a={1,2}
b={3,4}
print(a.isdisjoint(b))





