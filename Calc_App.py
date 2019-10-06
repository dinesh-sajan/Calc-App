a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("What do you want to do? \n")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n")
print("Enter your choice: \n")
c=int(input())
if c==1:
    print("The addition is %r" %(a+b))
    
elif c==2:
    print("The subtration is %r" %(a-b))
    
elif c==3:
    print("The multiplication is %r" %(a*b))
    
elif c==4:
    print("The divison is %r" %(a/b))
    
else:
    print("Your option is wrong")
