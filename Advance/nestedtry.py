# print("program started")

# try:
#     print("entered outer try block")
#     try:
#         print("entering inner try block")
#         a,b=10,0
#         print(res=a//b)
#     except ZeroDivisionError as ze:
#         print("reson for exception",ze)
# except:
#     print("I can handle any exceptions")
# finally:
#     print("I am outer finally block")
# print("prigram ended")

a=int(input("enter the number"))
b=int(input("enter the number"))
try:
    res=a//b
    print(res)
except:
    print("Handling exception")
    print("denominator cannot be zero sp handling the exception")
    try:
        b=int(input("enter the number"))
        res=a//b
        print(res)
    except:
        print("WTF seriously")
finally:
    print("bye bye")

