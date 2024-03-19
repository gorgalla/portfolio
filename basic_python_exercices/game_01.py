import random

def choice(choice):
    if choice == 1:
        return("Papel")
    elif choice == 2:
        return("Piedra")
    elif choice == 3:
        return("Tijera")
    else:
        return("Derrota")

user = int(input("1 => Papel \n2 => Piedra \n3 => Tijera \nElije una opcion => "))
pc = random.randint(1, 3)

if pc == user:
    print(f"Has elegido: {choice(user)}")
    print(f"PC ha elegido: {choice(pc)}")
    print("*" * 19)
    print("Empate")
elif (user == 1 and pc == 2 or user == 2 and pc == 3 or user == 3 and pc == 1):
    print(f"Has elegido: {choice(user)}")
    print(f"PC ha elegido: {choice(pc)}")
    print("*" * 19)
    print("Has ganado!!")
elif user not in range(1, 3):
    print("Has elegido perder")
else:
    print(f"Has elegido: {choice(user)}")
    print(f"PC ha elegido: {choice(pc)}")
    print("*" * 19)
    print("Has perdido :(")