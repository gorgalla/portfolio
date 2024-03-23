def p_area(a, b, c):
    if a and not b and c:
        res = a * c / 2
    elif a and b and not c:
        res = a * b
    elif a and not b and not c:
        res = a**2
    else:
        print("Parametros invalidos")
    print(res)

user = int(input("¿Que quieres calcular?\n1=> Cuadrado\n2=> Rectangulo\n3=> Tiangulo(Equilatero)\n=> "))
if user == 1:
    a = int(input("Introduce la altura del cuadrado => "))
    p_area(a,False, False)
elif user == 2:
    a = int(input("Introduce la base del rectangulo => "))
    b = int(input("Introduce la altura del rectangulo => "))
    p_area(a, b, False)
elif user == 3:
    a = int(input("Introduce la base del triangulo => "))
    c = int(input("Introduce la altura del triangulo => "))
    p_area(a, False, c)
else:
    print("ERROR")