import json

with open("dane_json.json", 'r') as f:
    data = json.load(f)

print(data)
print(data["members"])
print(data["members"][2])
print(data["members"][2]['name'])
print(data["members"][2]['powers'][1])

person_dict = {'name': 'Tomek', 'age': 39, "children": True, "czy_pali": None}

with open("dane_2.json", 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# person_json = json.dumps(person_dict)
# print(person_json)
