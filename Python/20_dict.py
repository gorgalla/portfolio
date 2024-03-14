person = {
    'name' : 'Gorka',
    'last_name' : 'Gallardo',
    'langs' : ['python', 'c', 'javascript'],
    'age' : 20
}

print(person)

person['name'] = 'gorka'
person['age'] -= 3
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print("items")
print(type(person.items()))

print("keys")
print(person.keys())

print("values")
print(person.values())