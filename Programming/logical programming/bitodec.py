dec=int(input())
temp=1
bi=0
while dec>0:
    rem=dec%2
    bi=bi+temp*rem
    temp=temp*10
    dec=dec//2
    
print(bi)