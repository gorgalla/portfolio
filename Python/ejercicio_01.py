user = input("Por favor, ingrese su nombre de ususario: ")
mail = input("Por favor, ingrese su correo electronico: ")
password = input("Por favor ingrese su contraseña: ")

print("Verificacion de datos: \n")
print("Usuario: ", user)
print("Correo: ", mail)
print("Contraseña: ", password)

res = input("¿Son correctos estos datos? S / N : ")
if res == 'S' or res == 's':
    print("Datos correctos")
else:
    print("Por favor vuelva a intentarlo mas tarde")