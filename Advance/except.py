print("Wassup yall")
num=int(input("enter the numeraator"))
den=int(input("enter the denominator"))
try:
    res= num//den
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")
print("coding is easy")
