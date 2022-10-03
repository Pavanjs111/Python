class empty(Exception):
    pass

class overflow(Exception):
    pass

class haswater(Exception):
    pass

try:
    cc=int(input("enter the capacity in tank"))
    if cc>100:
        raise overflow
    elif cc<=100 and cc>0:
        raise haswater
    elif cc==0:
        raise empty
except empty:
    print("there is no water in thee tank")
    
except haswater:
    print("there is some water in the tank")

except overflow:
    print("the water is overflowing")
