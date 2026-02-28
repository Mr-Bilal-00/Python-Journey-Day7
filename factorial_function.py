def factorial(a):
    fac=1
    f=1    
    while(f<=a):
        fac=fac*f
        f=f+1
    print("Factorial of ",a,"is ",fac)

num=int(input("Enter No : "))
factorial(num)