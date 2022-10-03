from re import S
import threading
import time

s=time.perf_counter()

def something():
    for i in range(10):
        print('do something')
        time.sleep(1)

def anything():
    for i in range(10):
        print("do anything")
        time.sleep(1)

    # something()
    # anything()
t1=threading.Thread(target=something)
t2=threading.Thread(target=anything)

t1.setName('ironman')
t2.setName('spiderman')

print(t1.getName())
print(t2.getName())

t1.start()
time.sleep(0.2)
t2.start()

print(t1.is_alive)
print(t2.is_alive)

e=time.perf_counter()

print('total time taken=',e-s)
print(t1.is_alive)
print(t2.is_alive)

t1.join()
t2.join()