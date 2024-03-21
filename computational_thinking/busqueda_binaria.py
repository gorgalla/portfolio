n = int(input("n => "))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, n)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - n) >= epsilon:
    print(f"Bajo => {bajo} - Alto => {alto} - Respuesta => {respuesta}")
    if respuesta**2 < n:
        bajo = respuesta
    else:
        alto =  respuesta
    respuesta = (alto + bajo) / 2
print(f"La raiz cuadrada de {n} es {respuesta}")