# n=int(input())
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#             val+=1
#             if val>ord('Z'):
#                 val=ord('A')
#     else:
#         print(" ",end=" ")
#     print()

# n=int(input())
# val=ord('A')
# for i in range(n):
#     val+=1
#     if val>ord('Z'):
#         val=ord('A')
#     for j in range(n):
#         if i>=j:
#             print(chr(val-1),end=" ")    
#     else:
#         print(" ",end=" ")
#     print()


# n=int(input())
# val=1+n
# for i in range(n):
#     val-=1
#     if val<1:
#                 val=9
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")    
#     else:
#         print(" ",end=" ")
#     print()

# n=int(input())
# val=1
# for i in range(n):
    
#     val+=1
#     if val>9:
#         val=0
#     else:
#         print(" ",end=" ")
       
#     for j in range(n):
#         if i==j:
#             print(val,end=" ") 
            
#     else:
#         print(" ",end=" ")
#     print()

# n=int(input())
# spc=n-1
# str=1
# val=ord('A')+n-1
# for i in range(n):
#     val-=1
#     if val<ord('A'):
#             val=ord('Z')
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(str):
#         print(chr(val),end=" ")
#     print()
#     spc-=1
#     str+=2
    
    
# n=int(input())
# val=1
# for i in range(n):
#     print(" ",end=" ")
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#             val+=1
#         if val>9:
#             val=1
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# str=2*n-1
# spc=0
# for i in range (n):
#      print(" ",end=" ")
#      for j in range(spc):
#         print(" ",end=" ")
#      for k in range(str):
#             print("*", end=" ")
#      print()
#      spc+=1
#      str-=2

# n=int(input())
# str=2*n-1
# spc=0
# val=1
# for i in range (n):
#          for j in range(spc):
#              print(" ",end=" ")
#          for k in range(str):
#              print(val, end=" ")
#              if val>9:
#                  val=1
#          print()
#          spc+=1
#          str-=2
#          val+=1

# n=int(input())
# str=2*n-1
# spc=0
# val=1
# for i in range (n):
#     #  val+=1
#     #  if val>9:
#     #              val=1
#      for j in range(spc):
#              print(" ",end=" ")
#             #  val+=1
#             #  if val>9:
#             #      val=1
#      for k in range(str):
#              print(val, end=" ")
#              val+=1
#              if val>9:
#                  val=1
#      print()
#      spc+=1
#      str-=2
#     #  val+=1
        

# n=int(input())
# str=2*n-1
# spc=0
# val=1
# for i in range (n):
    
#     for j in range(spc):
#              print(" ",end=" ")
#              val+=1
#     for k in range(str):
#              print(val, end=" ")
#              val+=1
#              if val>9:
#                  val=1
#     print()
#     spc+=1
#     str-=2
    

n=7
for i in range (n):
    for j in range(n):
        if i==0 or i==4 or (i==1 and j==4) or (i==2 and j==3) or (i==3 and j==2):
             print("*",end=" ")
        else:
            print(" ",end="")
    print()
 
    
