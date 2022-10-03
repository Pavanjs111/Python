sum_even=0
sum_odd=0
for i in range(1,11):
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd+=i
print("odd sum ",sum_odd)
print("even sum ",sum_even)