import random


def game():
    options = ["papel", "piedra", "tijera"]
    user_choice = int(input("Ingresa tu elección\n0 => Papel\n1 => Piedra\n2 => Tijera\nElección => "))
    pc_choice = random.randint(0,2)

    if user_choice == pc_choice:
        print(f"Has elegido => {options[user_choice]}")
        print(f"PC ha elegido => {options[pc_choice]}")
        print("*" * 22)
        print("EMPATE!")
    elif user_choice == 0 and pc_choice == 1 or user_choice == 1 and pc_choice == 2 or user_choice == 2 and pc_choice == 0:
        print(f"Has elegido => {options[user_choice]}")
        print(f"PC ha elegido => {options[pc_choice]}")
        print("*" * 22)
        print("Victoria!!")
    elif user_choice not in range(0,2):
        print("Has elegido perder")
    else:
        print(f"Has elegido => {options[user_choice]}")
        print(f"PC ha elegido => {options[pc_choice]}")
        print("*" * 22)
        print("DERROTA!")

game()