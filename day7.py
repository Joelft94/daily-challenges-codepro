import random

player = input("Piedra, papel o tijera? ").lower() 


def computer_choice():
    options = ["piedra", "papel", "tijera"]
    return random.choice(options)

def game(player, computer):
    if player == computer:
        return "Empate"
    elif player == "piedra" and computer == "tijera":
        return "Ganaste!"
    elif player == "papel" and computer == "piedra":
        return "Ganaste!"
    elif player == "tijera" and computer == "papel":
        return "Ganaste!"
    else:
        return "Perdiste!"
    
computer = computer_choice()
print(f"La computadora eligió {computer}")
print(game(player, computer))

