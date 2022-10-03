import pickle
laptop=["macbook","white","140000","1.5kg","ml chip"]
print(type(laptop))
lap1=pickle.dumps(laptop)

print(type(lap1))
print(lap1)

unpickle=pickle.loads(lap1)
print(type(unpickle))
print(unpickle)