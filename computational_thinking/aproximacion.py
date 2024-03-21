num = int(input("Introduce un numero enter => "))
epsilon = 0.001
i = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - num) >= epsilon and respuesta <= num:
    print(abs(respuesta**2 - num), respuesta)
    respuesta += i

if abs(respuesta**2 - num >= epsilon):
    print(f'No se encontró la raiz cuadrade de {num}')
else:
    print(f"La raiz cuadrada de {num} es {respuesta}")