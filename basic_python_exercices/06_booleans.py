num = int(input("Escribe un numero entero: "))
greater = False
if num < 10:
    print(not greater)
elif num > 10:
    print(greater)
else:
    print("error")