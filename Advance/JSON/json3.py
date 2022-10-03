import json
bikes={"name":"RE meteor","color":"black","fuel_type":"petrol","speed":"1000kmph"}
print(type(bikes))
bike_details=json.dumps(bikes)
print(type(bike_details))
print(bike_details)