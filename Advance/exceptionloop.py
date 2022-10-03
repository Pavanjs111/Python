print("Started learning python")
try:
    num=int(input("Enter the value for numerator"))
    den=int(input("Enter the value for denominator"))
    res=num//den
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("value can't be a character")
except TypeError:
    print("Denominator can't be a character")
except:
    print("handle the exception handler")

print("python rocks and it is very easy")