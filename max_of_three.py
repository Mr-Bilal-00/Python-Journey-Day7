def max(a1,b1,c1):
    if(a1>b1):
        if(a1>c1):
            print("Maximum No is ",a1)
        else:
            print("Maximum No is ",c1)
    elif(b1>c1):
        print("Maximum No is ",b1)
    else:
        print("maximum No is ",c1)

num1=int(input("Enter No : "))
num2=int(input("Enter No : "))
num3=int(input("Enter No : "))
max(num1,num2,num3)