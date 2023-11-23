### Importing

import random
import time

### Choosing Pokemon

def choosing_pokemon():
    print()
    print("Starter Choices: ")
    print("1. Sprigatito, a Grass Type feline")
    print("2. Fuecoco, a Fire Type croc")
    print("3. Quaxly, a Water Type duckling")
    print()
    
    pokemon = ""
    while pokemon == "":
        choice_1 = input("Choose your starter (1, 2, 3): ")
        
        if(choice_1 == "1"):
            print("You have selected Grass Type Sprigatito!")
            pokemon = "Sprigatito"
        elif(choice_1 == "2"):
            print("You have selected Fire Type Fuecoco!")
            pokemon = "Fuecoco"
        elif(choice_1 == "3"):
            print("You have selected Water Type Quaxly!")
            pokemon = "Quaxly"
        else:
            print("Invalid Choice! Try Again with another answer!")

    return pokemon

### Choosing Trainer

def choosing_trainer():
    print()
    print("Trainer Choices: ")
    print("1. Florian, a Male Pokemon Trainer")
    print("2. Juliana, a Female Pokemon Trainer")
    print()

    trainer = ""
    while trainer == "":
        choice_2 = input("Choose your trainer (1, 2): ")
        
        if(choice_2 == "1"):
            print("You have selected Florian!")
            trainer = "Florian"
        elif(choice_2 == "2"):
            print("You have selected Juliana!")
            trainer = "Juliana"
        else:
            print("Invalid Choice! Try Again with another answer!")

    return trainer

### Game Introduction

def game_intro(pokemon, trainer):
    print()
    print("Welcome to Pokemon Scarlet and Violet!")
    print("You will be exploring the Paldea Region!")
    print(f"Your starter pokemon is {pokemon}.")
    print(f"Your trainer is {trainer}.")
    print("Good luck!")
    print("Have fun and catch'em all!")

### Decision

def decision():
    print()
    print("1. Do you want to battle a wild Pokemon?")
    print("2. Do you want to attempt to catch a wild Pokemon with an Ultra Ball?")
    print()

    decision = ""
    while decision == "":
        choice_3 = input("Choose your option (1, 2): ")

        if(choice_3 == "1"):
            print("You have selected to battle!")
            decision = "battle"
        elif(choice_3 == "2"):
            print("You have selected attempt a catch!")
            decision = "attempt a catch"
        else:
            print("Invalid Choice! You have selected to do nothing! Select 1 or 2!")

        return decision
    
### Battle / Attempt a Catch

def battle_or_catch(decision):
    battle_pokemon = ["Chikorita", "Cyndaquil", "Totodile"]
    result_1 = ["won", "lost"]
    result_2 = ["successful", "not successful"]
   
    if(decision == 1):
        print("You confront a wild Pokemon!") 
        print("It is a " + random.choice(battle_pokemon) + "!")
        print("You have " + random.choice(result_1) + " the battle!")

    elif(decision == 2):
        print("You attempt to catch a wild Pokemon!")
        print("It is a " + random.choice(battle_pokemon) + "!")
        print("You have used 1 Ultra Ball.")
        print("Your attempt was " + random.choice(result_2) + "!")

### Manage Health

def manage_health(decision):
    pokemonhp = 100
    enemy_dmg = random.randint(0, 100)

    if(decision == 1):
        pokemonhp = pokemonhp - enemy_dmg
        print(f"You have taken {enemy_dmg} damage from wild Pokemon!")
        print(f"Your remaining health is {pokemonhp}.")

    elif(decision == 2):
        pokemonhp = pokemonhp
        print(f"You have taken 0 damage from wild Pokemon!")
        print(f"Your remaining health is {pokemonhp} and was not affected.")

    return pokemonhp

### Bonus Points

def bonus(pokemonhp):
    if(pokemonhp == 100):
        print("You have a perfect score because you took 0 dmg.")

    elif(90 <= pokemonhp <= 99):
        print("You have a near perfect score because you took 1 to 10 dmg.")
    
    elif(50 <= pokemonhp <= 89):
        print("You have an okay score because you took 11 to 50 damage.")

    elif(20 <= pokemonhp <= 49):
        print("You have a not bad score but your pokemon is under 50% hp now.")

    else:
        print("You have a bad score and your pokemon almost died as it is under 20% hp.")

### Game Completion

def game_comp():
    print()
    print("You have finished the game.")
    print("You have completed your Pokemon journey for now.")
    print()
    print(bonus)

### Running the Game

pokemon = choosing_pokemon()
time.sleep(1)
trainer = choosing_trainer()
time.sleep(1)
game_intro(pokemon, trainer)
time.sleep(1)
pokemon_decision = decision()
time.sleep(1)
battle_or_catch(pokemon_decision)
time.sleep(1)
pokemonhp = manage_health(pokemon_decision)
time.sleep(1)
bonus(pokemonhp)
time.sleep(1)
game_comp()
    


        


