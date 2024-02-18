import json

person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}

result = json.dumps(person)
print(result)
print(type(result))



obekt = {
    'name': 'Общество',
    'status': 'хуйня'
}

result = json.dumps(obekt)
print(result)
print(type(result))