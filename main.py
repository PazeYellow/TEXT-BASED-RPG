import pickle
import os
from player import Player
from area import AreaManager
from shop import Shop

SAVE_FILE_PATH = "savefile.pkl"

def print_menu():
    print("1. Travel to Kingdom")
    print("2. Travel to Forest")
    print("3. Travel to Cave")
    print("4. Visit Shop")
    print("5. Rest and Heal")
    print("6. Save Game")
    print("7. Quit")

def save_game(player):
    with open(SAVE_FILE_PATH, "wb") as file:
        pickle.dump(player, file)
    print("Game saved.")

def load_game():
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "rb") as file:
            player = pickle.load(file)
        return player
    else:
        print("No save file found.")
        return None

def create_new_player():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    return player

def main():
    player = load_game()

    if not player:
        player = create_new_player()

    area_manager = AreaManager()
    shop = Shop()

    while True:
        print(f"\n-- {player.name}'s Adventure --")
        print(f"Health: {player.health}")
        print(f"Gold: {player.gold}")
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            area = area_manager.get_area("kingdom")
            enemy = area.get_random_enemy()
            print(f"\nYou encounter a {enemy.name} in the {area.name}!")
            # Add combat logic here

        elif choice == "2":
            area = area_manager.get_area("forest")
            enemy = area.get_random_enemy()
            print(f"\nYou encounter a {enemy.name} in the {area.name}!")
            # Add combat logic here

        elif choice == "3":
            area = area_manager.get_area("cave")
            enemy = area.get_random_enemy()
            print(f"\nYou encounter a {enemy.name} in the {area.name}!")
            # Add combat logic here

        elif choice == "4":
            print("\nWelcome to the Shop!")
            item_name = input("Enter the item you want to buy: ")
            shop.buy_item(player, item_name)

        elif choice == "5":
            player.heal(20)
            print("\nYou rest and recover some health.")

        elif choice == "6":
            save_game(player)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
