class Age(Exception):
    pass
class minor(Age):
    pass
class major(Age):
    pass 
try:
    age=int(input("input the age of the person "))
    if age>=18:
        raise major
    elif age<18:
        raise minor
except major:
    print("eligible for voter ID")
except minor:
    print("Not eligible for voter ID")