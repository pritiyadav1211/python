# file=open("function.txt","x")
# #open a file
# file=open("function.txt","r")
# print(file.read())


# #read a limited no. of char
# #readline() method read one line at one time 
# # readlines() line read all line and return them as a list ,,
# to apply strip method we use for method in 
# #example counting lines 
# #counting word and caharacter

# file=open("new.py","r",encoding="utf-8")
# content=file.read()
# print(content)
# file.close()
# print(file.closed)

#file handling==it is used to create,read,write,append and manage files.
###open a file .....syntax: file=open("filename.txt","mode")
#que....why we need file handling?
#   *store data pemanently
#   *read saved data whenever needed .
#  *update existing data.
#   *maintain record
#real life example
#banking system,hospital record


#*# type of file...
#....1)text file(.txt)==store data as txt.
#......human readable
#.....example:student.txt
#2)binary file(.bin,.jpg,.pdf)
#.store data in binary format(0s,1s)
#.used for images,videos,pdf,audio

#open a file...file=open("filename.txt","mode")#mode specifies the operation to perform.

##file modes
#r =read the file .error if file does not exist.
#w=write to the file.create a new file or overwrites existing content.
#a=append data at the end of file.create the file if it does not exist.
#x=create a new file. error if the file already exist.
#rb=read a binary file
#wb=write a binary file
#r+=read and write
#w+=read and write(Overwrite files)
#a+=read and append


##reading a file==means retreiving the data stored in a file.
# methods
# 1]read()...read the entire content
file=open("new.py","r",encoding="utf-8")
print(file.read())
file.close() 

#2]read(size)....read only the specified number of characters
file=open("new.py","r",encoding="utf-8")
print(file.read(10))
file.close()

#3]readline()....read one line at a time.
file=open("new.py","r",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#4]readlines()....reads all lines and return them as a list.
file=open("new.py","r",encoding="utf-8")
print(file.readlines())
# file.close()

# #using with statement
with open("new.py","r",encoding="utf-8") as file:
     print(file.read())  # advantage of this file is automatically closed after reading.

# #closing a file....after working with a file,it should be closed.
file=open("new.py","r",encoding="utf-8")
print(file.read())
print(file.closed)

#EXAMPLE 1 ......counting words 
with open("new.py","r",encoding="utf-8") as file: #counting words
    data=file.read()
words=data.split()
print("total no. of words",len(words))

#EXAMPLE 2 ......counting characters
with open("new.py","r",encoding="utf-8") as file: #counting words
    data=file.read()
print("total no. of words",len(data))

#example 3.....counting lines
count=0
with open("new.py","r",encoding="utf-8") as file:
    for line in file:
        count+=1
print("total number of lines:",count)

#split() method.....it is usedto split a string into a list of words.
#syntax=string.split(seprator)    seprator is optional
text="hello python file handling"
words=text.split()
print(words)

#splitlines() method.... used to split text into a list of lines
#syntax=string,splitlines()
text="hello\n python file handling"
lines=text.splitlines()
print(lines)

##writibg text file...write() method is used to write text to a file.
file=open("new.py","w",encoding="utf-8") #w.. write method (create a new file if ir doesn't exist,or overwrite the existing file.)
file.write("text to be written")
file.close()

file=open("handling.py","w",encoding="utf-8") #w.. write method (create a new file if ir doesn't exist,or overwrite the existing file.)
file.write("text to be written")
file.close()

file=open("handling.py","w")
file.write("name:priti\n")
file.write("age:20")
file.close()





     






