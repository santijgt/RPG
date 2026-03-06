import pokemons
import random

experience_points = 0
party = []

def choose_starter():
    choose_starter = input("Choose your starter pokemon (Pikachu, Charmander, Squirtle): ")
    match choose_starter:
        case "Pikachu":
            add_to_party(pokemons.pokemons[0])
            return pokemons.pokemons[0]
        case "Charmander":
            add_to_party(pokemons.pokemons[1])
            return pokemons.pokemons[1]
        case "Squirtle":
            add_to_party(pokemons.pokemons[2])
            return pokemons.pokemons[2]
        case _:
            print("Invalid choice, defaulting to Pikachu.")
            add_to_party(pokemons.pokemons[0])
            return pokemons.pokemons[0]
        
def add_to_party(pokemon):
    if len(party) < 6:
        party.append(pokemon)
        print(f"{pokemon.name} added to your party!")
    else:
        print("Your party is full! You can't add more pokemon.")

def battle(pokemon1, wild_pokemon):
    while pokemon1.is_alive() and wild_pokemon.is_alive():
        pokemon1.deal_damage(wild_pokemon)
        if not wild_pokemon.is_alive():
            print(f"{pokemon1.name} wins!")
            break
        wild_pokemon.deal_damage(pokemon1)
        if not pokemon1.is_alive():
            print(f"{wild_pokemon.name} wins!")
            break

def catch(pokemon):
    print(f"You caught a {pokemon.name}!")
    add_to_party(pokemon)

def level_up(pokemon):
    pokemon.hp += 10
    pokemon.attack += 5
    print(f"{pokemon.name} leveled up! HP: {pokemon.hp}, Attack: {pokemon.attack}") 

def heal(pokemon):
    pokemon.hp += 20
    print(f"{pokemon.name} healed! HP: {pokemon.hp}")

def encounter():
    i = random.randint(0, 26)
    print(f"You encountered a wild {pokemons.pokemons[i].name}!")
    wild_pokemon = pokemons.pokemons[i]
    return wild_pokemon

def options_encounter(pokemon1, wild_pokemon):

    global experience_points

    while(wild_pokemon.is_alive() and pokemon1.is_alive()):
        print("1. Battle")
        print("2. Catch")
        print("3. Run")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                battle(pokemon1, wild_pokemon)
                experience_points += 1
                if experience_points == 3:
                    level_up(pokemon1)
                    experience_points = 0
                break
            case "2":
                catch(wild_pokemon)
                break
            case "3":
                print("You ran away!")
                break
            case _:
                print("Invalid option, try again.")

def full_encounter(pokemon1):
    wild_pokemon = encounter()
    options_encounter(pokemon1, wild_pokemon)