
x=20
def show():
 global x
 x=10
 print("local variable:",x)
show()
print("outide variable",x)
a="hello all"
print(len(a))
print(a[2:7])
message="my name is priti"
#print("priti" in message)
if"are" in message:
   print("present")
else:
  print("not present")
   
name="hello world"
print(name[-4:-2])
print(name.upper())
print(name.lower())
h1="hello"
h2="world"
result=h1+h2
print(result)
msg="   hello world  "
print(msg.replace('world','all'))
print(msg.strip())