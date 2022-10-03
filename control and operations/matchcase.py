opt=int(input("enter the options "))
print("\n1.Addition \n 2.Substraction\n 3.multiplication \n 4.division")
match opt:
    case 1:
        a=int(input("enter the value for a "))
        b=int(input("rnter the value for b "))
        res=a+b
        print("result",res)
    case 2:
        a=int(input("enter the value for a "))
        b=int(input("rnter the value for b "))
        res=a-b
        print("result",res)
    case 3:
        a=int(input("enter the value for a "))
        b=int(input("rnter the value for b "))
        res=a*b
        print("result",res)
    case 4:
        a=int(input("enter the value for a "))
        b=int(input("rnter the value for b "))
        res=a//b
        print("result",res)
    case _:
        print("condition not found")

