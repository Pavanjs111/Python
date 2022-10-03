print("to calculate the grade of the student")
marks=(input("enter the marks grade -->"))
match marks:
    case 'A+':
        a=int(input("enter the marks->"))
        res=a>=85
        print(res)
    case 'A':
         a=int(input("enter the marks->"))
         res=a>=60
         print(res)
    case 'B':
         a=int(input("enter the marks->"))
         res=a>=45
         print(res)
    case 'C':
         a=int(input("enter the marks->"))
         res=a>=40
         print(res)
    case 'F':
        a=int(input("enter the marks->"))
        res=a<35
        print(res)
    case _:
        print("please enter the valid option")