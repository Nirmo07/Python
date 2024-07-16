def celsius_to_fahrenheit(celsius):
    fahrenheit=(9/5*celsius)+32
    print("Conversion of", celsius, "is ", fahrenheit )
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    print("Conversion of", fahrenheit, "is", celsius )
    return celsius

while True:
    print("1.convert celsius to fahrenheit:")
    print("2.convert fahrenheit to celsius:")
    print("3.Exit")
    
    d=int(input("Choose between 1 to 3:"))
    
    if d==1:
        celsius=float(input("enter celsius:"))
        celsius_to_fahrenheit(celsius)
        
    elif d==2:
        fahrenheit=float(input("enter fahrenheit:"))
        fahrenheit_to_celsius(fahrenheit)
        
    elif d==3:
        exit(0)
        
    else:
        print("invalid")
        
    
    
        