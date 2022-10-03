from asyncore import write


fh=None
try:
    fh=open("notes.txt","w")
    print(fh)
    if fh.writable()==True:
        print("File is opened in write mode")
        fh.write("Plese get your life togeather\n")
        fh.write("Be mature enough to give millions of people jobs\n")
        fh.write("Thagede leyyy")
except FileNotFoundError:
    print("handling error")
    print("no such file found")