# AND
print("AND")
print("True and True => ", True and True) #true
print("True and False => ", True and False) #false
print("False and True => ", False and True) #false
print("False and False => ", False and False) #false

print(10 > 5 and 5 < 10) #true
print(20 < 5 and 5 > 1) #false

stock = int(input("Ingrese el numero de stock => "))

print(stock >= 100 and stock <= 1000)

# OR

print("OR")
print("True or True => ", True or True) #true
print("True or False => ", True or False) #true
print("False or True => ", False or True) #true
print("False or False => ", False or False) #false

role = input("Ingresa tu rol => ").lower()
print(role == "admin" or role == "seller")