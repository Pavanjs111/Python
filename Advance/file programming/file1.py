fh=None
try:
    fh=open("note1.txt","r")
    print(fh)
except FileNotFoundError:
    print("handling error")
    print("there is no files you are searching for")
