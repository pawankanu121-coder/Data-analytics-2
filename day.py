a=input("Enter your name: ")
print("MY name is;",a )

a = input("Enter your first no.: ")
print(int(a))

b = input("Enter your second no.: ")
print(int(b))

print("The value of",int(a),"+",int(b),"is:",int(a)+int(b))
print("The value of",a,"+",b,"is:",a+b)

age= int(input("Enter your age:"))
print("your age is:",age)
if age<13:
    print("you are a child")
elif age<20:
    print("you are a teenager")
elif age<60:
   print("you are a responsible adult")
else:
   print("you are a seniour citezen")