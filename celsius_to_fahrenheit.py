def converter(c):
     f=((c*1.8)+32)        #(F=(C*1.8)+32)
     print("Temprature in Fahrenheit ",f)
     return f
C=int(input("Enter Temprature in celcius :"))
converter(C)