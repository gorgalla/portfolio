'''
for i in range(20):
    print(i)
'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
    
tupla = ("Gorka", "Nicole", "Nikita")
for i in tupla:
    print(i)
    
producto = {
    'name' : 'Camisa',
    'precio' : 40,
    'stock' : 42
}

for element in producto:
    print(element)
    print(producto[element])
    
people = [
    {
        'name' : 'gorka',
        'edad' : 88
    },
    
    {
        'name' : 'nicole',
        'edad' : 21
    },
    
    {
        'name' : 'nikita',
        'edad' : 1
    }
]

for person in people:
    print("Name => ", person['name'])