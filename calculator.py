while True:
    a = input("Enter first number or 'exit': ")
    if a.lower()=="exit":
        break
    b=int(input("Enter second number: "))
    
    print("only '+' '-' '*' '/' ")
    c=input()
    a=int(a)
    if c == "+":
        print(a+b,"added")
    elif c=="-":
        print(a-b,"sub")
    elif c=="*":
        print(a*b,"mul")
    elif c=="/":
        if b!=0:
            print(a/b,"div")
        else:
            print("Error: Division by zero")
    else:
        print("Error raa puka valli operation narchuko")