# #airthmetic operator
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# print("addition:",a+b)
# print("subtraction:",a-b)
# print("multiplication:",a*b)
# print("divisiom:",a/b)
# print("modular division:" ,a%b)
# print("power:",a**b)

#assignment operator
a=8
b=4
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)

#relational operator
a=5
b=4
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)

#logical operator
a=5 
b=7
print("and operator:" , a>15 and b<8)
print("or operator:" ,a<6 or b>7)
print("not operator:" , not(a<7))

#bitwise operator
a=5 
b=4
print("a=" , a)
print("b=" , b)
print("bitwise and:" , a&b)
print("bitwise or:" , a|b)
print("bitwise not:" , ~a)
print("bitwise xor:" , a^b)
print("left shift:" , a<<b)
print("right shift" , a>>b)

#Mmembership operator== used to check whether a value exist in a sequence
#in means exist
#not in means does not exit
name="python"
print("p" in name)
print("z" not in name)

#identity operator ==used to compare wheter two object are the same
# is ==same object
# is not ==different object
a={1,2,3}
b=a
print(b is not a)







