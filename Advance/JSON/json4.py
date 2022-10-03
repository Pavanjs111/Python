import json
movie_name={"name":"KGF2","cast":"Yash and Nidhi","type":"Action","Producer":"Hombale","director":"prashanth neil"}
fh=None

try:
    fh=open("movie_info.json","w")
    json.dump(movie_name,fh)
except:
    print("no such file ")

finally:
    if fh!=None:
        fh.close()