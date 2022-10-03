from multiprocessing.dummy import Value


print("program started")
try:
    a=int(input("enter a positive number"))
    if a<0:
        raise ValueError("enter value more than 0")
        
except ValueError as ve:
    print("the reason for exception is",ve)
print("program ended")