l1=[10,20,30,20,10]
j=len(l1)-1
for i in range(len(l1)):
    if l1[i]!=l1[j]:
        print("List is not palindrome")
        break
    j-=1
else:
    print("List is a palindrome")