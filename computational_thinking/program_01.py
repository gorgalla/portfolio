def busqueda_binaria(num):
    n = num
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, n)
    res = (alto + bajo) / 2
    while abs(res**2 - n) >= epsilon:
        if res**2 < n:
            bajo = res
        else:
            alto = res
        res = (alto + bajo) / 2
    print(f"La raiz cuadrada de {n} es {res}")

def aproximacion(num):
    n = num
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

def operadores():
    n = int(input("Introduce el numero => "))
    print("¿Que algoritmo deseas usar?\n1 => busqueda binaria\n2 => aproximacion\n")
    decision = int(input("=> "))
    if decision == 1:
        busqueda_binaria(n)
    elif decision == 2:
        aproximacion(n)
    else:
        print("Parametro erroneo --Saliendo del programa")
operadores()