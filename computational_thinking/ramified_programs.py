print(2 == 4) #false
print(3 != 4) #true
print(2 > 3) #false
print(2 < 3) #true
print(2 <= 3) #true
print(2 >= 3) #false

print(True and True) # true
print(False and True) # false
print(False or True) # true
print(not True) #false

'''
if <condition>: 
    <expresion>
'''

if 5 <= 10: #true
    print("hello")
else:
    print("5 no es mayor a 10")

'''
if <condition>: 
    <expresion>
elif <condition>:
    <expresion>
else:
    <expresion>
'''

n1 = int(input("Introduce un numero => "))
n2 = int(input("Elige el segundo numero => "))

if n1 >= n2:
    print(f"{n1} es mayor o igual a {n2}")
elif n1 <= n2:
    print(f"{n1} es menor o igual a {n2}")
elif n1 == n2:
    print(f"{n1} es igual a {n2}")
else:
    print("Ha ocurrido un problema")