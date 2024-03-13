edad = int(input("Ingresa tu edad => "))
nombre = input("Ingresa tu nombre => ")

if edad >= 18:
    print(f"Hola {nombre}, tu edad es {edad} por lo que puedes pasar al antro")
elif edad < 18:
    print(f"Hola {nombre}, no se aceptan menores de edad.")