import random
import os

user = 0
pc = 0
def puntuacion():
    global user, pc
    print(f"User => {user} points")
    print(f"PC => {pc} points")

def game():
    global user, pc
    print("Papel - Piedra - Tijera")
    puntuacion()
    user_choice = input("¿Cual es tu elección? => ").lower()
    pc_choice = random.randint(0, 2)
    options = ['papel','piedra', 'tijera']
    
    if pc_choice == 0:
        pc_choice = options[0]
    elif pc_choice == 1:
        pc_choice = options[1]
    elif pc_choice == 2:
        pc_choice = options[2]

    if user_choice == pc_choice:
        print(f"Has elegido {user_choice}")
        print(f"PC ha elegido {pc_choice}")
        print("Resultado => EMPATE")
    elif user_choice == options[0] and pc_choice == 'piedra':
        print(f"Has elegido {user_choice}")
        print(f"PC ha elegido {pc_choice}")
        user += 1
        print("Resultado => VICTORIA")
    elif user_choice == options[1] and pc_choice == 'tijera':
        print(f"Has elegido {user_choice}")
        print(f"PC ha elegido {pc_choice}")
        user += 1
        print("Resultado => VICTORIA")
    elif user_choice == options[2] and pc_choice == 'papel':
        print(f"Has elegido {user_choice}")
        print(f"PC ha elegido {pc_choice}")
        user += 1
        print("Resultado => VICTORIA")
    else:
        print(f"Has elegido {user_choice}")
        print(f"PC ha elegido {pc_choice}")
        pc += 1
        print("Resultado => DERROTA")


os.system("clear")
for i in range(6):
    game()
    input("Pulsa cualquier tecla para continuar...")
    os.system("clear")

print(f"Resuldo final: \nUser => {user} points!\nPC => {pc} points!")
if user > pc:
    print("Has ganado!")
elif user == pc:
    print("El resultado es un empate!")
else:
    print("Has sido derrotado por la IA :(")
print("\n" * 3)
input("Pulsa cualquier tecla para salir del programa...")