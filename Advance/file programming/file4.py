fh=None
try:
    fh=open("notes2.txt","r")
    if fh.readable()==True:
        print("the file is being read")

        pos=fh.tell()
        print("current cursor position is at->",pos)

    lines=fh.readlines()
    print(type(lines))
    print(lines)
    for msg in lines:
        print(msg,end=" ")
    
except FileNotFoundError:
    print("The file we are searching is not found")

finally:
    if fh!=None:
        fh.close()
        print("The connection we established is closed")