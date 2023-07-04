import json

pets = {
    'name': "Charly",
    'age': 15,
    'meals': ['Purina', 'Hills'],
    'owner': {"fname": 'Bill', 'Sname': 'Gates'}
}

with open ('pets.jason', 'a') as pet_file:
    json.dump(pets, pet_file)
