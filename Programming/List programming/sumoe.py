l1=[23,45,62,44,36,81,90]
sum_even=0
sum_odd=0
for i in range(0,len(l1)):
    if l1[i]%2==0:
        sum_even+=l1[i]
    else:
        sum_odd+=l1[i]
print("the even sum is ",sum_even)
print("the odd sum is ",sum_odd)