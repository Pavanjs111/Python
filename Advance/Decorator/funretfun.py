def say_hello(name):
    return f" hello {name}"

def bewithme(name):
    return f" hey {name} be with me,we are awesome"

def awesome(val):
    return val("Sam")

print(say_hello("Thor"))
print(bewithme("captian Marvel"))
print(awesome(say_hello))
print(awesome(bewithme))