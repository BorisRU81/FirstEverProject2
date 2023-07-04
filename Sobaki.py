import json

with open ('pets.json') as pet_file:
    string  = pet_file.read()
    data = json.load(string)

for item in data:
    if type(data[item]) == list:
        print(item, ','.join(data[item]))
    else if type(data[item]) == dict:
        print(item)
        for k, v, in data[item].items():
            print(item, k, v)