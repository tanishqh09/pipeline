import json

d={

    "id":1,
    "name":"t",
    "orders":{
        "jan":2,
        "feb":4,
        "march":6
    }
}

try:
    f=open("data1.json",'w')
    json.dump(d,f)
    print("data1.json created successfully")
finally:
    f.close()
