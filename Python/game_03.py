import random
import os

def choice(s):
    if s == "papel":
        return (0)
    elif s == "piedra":
        return (1)
    elif s == "tijera":
        return (2)
    else:
        print("Valor invalido, derrota")

def game():
    user = input("Elije tu jugada: Papel - Piedra - Tijera => ").lower()
    pc = random.randint(0, 2)
    eleccion = choice(user)

    if eleccion == pc:
        print(f"Has elegido {user}")
        print(f"Pc ha elegido {choice(pc)}")
        print(" " * 33)
        print("*" * 33)
        print("EMPATE")
        print("*" * 33)
    elif eleccion == 0 and pc == 1 or eleccion == 1 and pc == 2 or eleccion == 2 and pc == 0:
        print(f"Has elegido {user}")
        print(f"Pc ha elegido {choice(pc)}")
        print(" " * 33)
        print("*" * 33)
        print("VICTORIA")
        print("*" * 33)
    else:
        print(f"Has elegido {user}")
        print(f"Pc ha elegido {choice(pc)}")
        print(" " * 33)
        print("*" * 33)
        print("Derrota")
        print("*" * 33)

def main():
    os.system("clear")
    vidas = 3
    while vidas > 0:
        print(f"Numero de vidas {vidas}")
        game()
        vidas -= 1
        
main()