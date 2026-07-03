a= float(input("Entre x number = "))
b =float(input("Entre Y number ="))
print("add +")
print("sub -")
print("mul *")
print("div /")

choice = input("+,-,*,/ =" )

         

def add(a,b):
    return a + b

def sub(a,b):
    return a-b

def mul(a,b):
    return a * b

def div(a,b):
    return a/b


if choice == "+" :
    print(f"{a} + {b} = {add( a ,b  )}")

elif choice == "-" :
        print(f"{a} - {b} = {sub( a ,b  )}")


elif choice == "*":
     print(f"{a} * {b} = {mul( a ,b  )}")


elif choice == "/":
        print(f"{a} /{b} = {div( a ,b  )}")

else :
    print("invild")
                
        

