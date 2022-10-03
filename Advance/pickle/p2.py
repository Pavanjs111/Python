import pickle
raw_agent=["black tiger","major general","brown","blue"]
fh=None

try:
    fh=open("raw_agent_info.pkl","rb")

    raw_agent_details=pickle.load(fh)
    print(type(raw_agent_details))
    print(raw_agent_details)

except:
    print("no such file")

# finally:
#     if fh!=None:
#         fh.close()