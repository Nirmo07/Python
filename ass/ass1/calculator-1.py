print(":::Simple Calculator:::")
x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))

def add(x,y):
        c=x+y
        print("sum is:",c)
        return c

def sub(x,y):
        c=x-y
        print("sub is:",c)
        return c

def mul(x,y):
        c=x*y
        print("product is:",c)
        return c
                
def div(x,y):
        if y==0:
                print("Cannot divide by zero")
        else:
                c=x/y
                print("div is:",c)
        return c

while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")  
        d=int(input("enter no. between 1 to 5:"))
        
        if d==1:
                add(x,y)

        elif d==2:
                sub(x,y)

        elif d==3:
                mul(x,y)

        elif d==4:
                div(x,y)
        
        elif d==5:
                exit(0)
        else:
                print("Invalid choice. Please try again.")  

