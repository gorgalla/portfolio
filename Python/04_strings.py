user = input("Por favor, introduzca su nombre de usuario: ")
email = input("Por favor, introduzca su correo electronico: ")
name = input("Por favor, introduzca su nombre real: ")
last_name = input("Por favor, introduzca su apellido: ")
space = ' '
full_name = name + space + last_name

print("Gracias por responder al formulario:")

print("Usuario: ", user)
print("Correo: ", email)
print("Nombre: ", name)
print("Apellidos: ", last_name)

print("Nombre completo: ", full_name)

res = "Hola {}, bienvenido a este programa!".format(user)
print(res)

res = "Su correo es: {} y su nombre completo es {}".format(email, full_name)
print(res)

res = "Ejercicio finalizado"
print(res)