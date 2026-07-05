# # #dictionary is a built in data type 
#  #it store value in form of key and value pairs
# # #key is unique amd used to access the value

# # #syntax 1
# # dictionary_name={
# #     "key1":"value1",
# #     "key2":"value2",
# #     "key3":"value3"
# # }
# # #syntax 2 using method
person=dict(name="priti",age=18,course="bca")
print(person)

# # #example
student={
    "name":"priti",
    "age":10,
    "course":"bca"
}
print(student)

# # #lenght of dictionary
print(len(student))

# # #access method
print(student["name"])

# #access using get method ,,if we access wrong key then it will not do show error it show none
print(student.get("email"))
# #if we  don't want to print done you can type a msg
print(student.get("email","not available"))


# # #access method using loop
for i in student:
     print(i)
for i in student.values():
    print(i)
for i in student.items():
      print(i)

# #Ssorting the dictonary
print(sorted(student))

# #copying the dictionary
new_student=student.copy()
print(new_student)

# #empty dictionary
emp=dict()
print(type(emp))


# # #add method
student["address"]="haryana"
print(student)
# #update value
student["age"]=20
print(student)

# # #update method or add method
student.update({"course":"betch","emailid":"abc@gmail.com"})
print(student)

# #pop method removes the existing key value
student.pop("name")
print(student)
#ifwe want to print which value delete then make a new variable
new=student.pop("name")
print(new)

#popitem method remove the last key-value from dictionary
print(student.popitem())


# #clear
print(student.clear())

# #changing list in dictionary
pair=[("x",10),("y",20),("z",30)]
pair1=dict(pair)
print(pair1)

# printing only keys of the dictionary
print(student.keys())
#print only values of dict
print(student.values())
#print both key-value of dict
print(student.items())

# #nested dictionary
# student={
#     "student1":{
#         "name":"priti"
#         "course":"bca"
#         "age":19
#     },
#     "student2":{
#         "age":18
#         "name":"deepika"
#         "course":"bca"
#     },
#     "student3":{
#         "course":"bca"
#         "name":"jiya"
#         "age":19
#     }
# }
# print(students)
# #to print a
# #to print a specific value of a sub dict
# print(students["student2"]["name"])
