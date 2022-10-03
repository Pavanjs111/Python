l=["I am going to make a lot of money\n",
  "I will use it for good deeds\n ",
"I will be the most respected person on the planet\n",
  "I will make everything I touch blossom\n"
]
fh=None
try:
    fh=open("note1.txt","w")
    if fh.writable()==True:
        print("file opened in the write mode")
        fh.writelines(l)

except FileNotFoundError:
    print("File not present")

finally:
    if fh!=None:
        fh.close()
        print("file connection is closed")

