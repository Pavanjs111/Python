from tkinter import EXCEPTION


class phase(Exception):
    pass

class neutral(Exception):
    pass

class earthing(Exception):
    pass

try:
    volts=int(input("enter the volts"))
    if volts>0 and volts<225:
        raise phase
    elif volts == 0:
        raise neutral
    elif volts>225:
        raise earthing

except phase:
    print("The circuit board is safe if its between 0 to 225")

except neutral:
    print("it has power but nothing to worry")

except earthing:
    print("More than 225 earthing will activate")

finally:
    print("this saves the costly resources")
