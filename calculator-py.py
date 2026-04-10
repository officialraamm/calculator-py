print ("welcome to calculator.....")
print("1. Add")
print("2.sub")
print("3.mul")
print("4,divid")
print("5,DD")
print("6,remainder")

num1= int(input("enter your first number..."))
num2= int(input("enter your second number..."))
# num3=int(input("enter your third number"))
# num4=int(input("enter your forth number"))
choice = int(input('enter your choice...'))

if choice==1:
    print(num1+num2)
    if choice==2:
         print(num1-num2)
if choice==3:
    print(num1*num2)
if  choice==4:
    print(num1/num2)
if choice==5:
   print(num1//num2)
if choice==6:
   print(num1//num2*2)    
else: 
    print("thank you for using calculatorapp..")