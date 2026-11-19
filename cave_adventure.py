"""
Cave Adventure - A Text-Based Adventure Game
A simple game to learn Python basics: variables, functions, loops, and if/else.
"""

import time

# ---------- Game state ----------
player = {
    "name": "",
    "health": 100,
    "has_torch": False,
    "has_key": False,
    "has_treasure": False
}


def slow_print(text):
    """Prints text one line at a time with a tiny pause, for dramatic effect."""
    print(text)
    time.sleep(1)


def show_status():
    print(f"\n--- {player['name']}'s Status ---")
    print(f"Health: {player['health']}")
    print(f"Torch: {'Yes' if player['has_torch'] else 'No'}")
    print(f"Key: {'Yes' if player['has_key'] else 'No'}")
    print("-------------------------\n")


def intro():
    slow_print("=== THE CAVE ADVENTURE ===")
    player["name"] = input("Enter your name, brave explorer: ")
    slow_print(f"\nWelcome, {player['name']}! You stand before a dark cave entrance.")
    slow_print("Legend says a treasure lies deep within... but so do dangers.\n")


def entrance():
    slow_print("You are at the CAVE ENTRANCE.")
    print("1. Enter the cave")
    print("2. Check your status")
    print("3. Leave (end game)")

    choice = input("> ")

    if choice == "1":
        torch_room()
    elif choice == "2":
        show_status()
        entrance()
    elif choice == "3":
        slow_print("You walk away. Maybe another day...")
        exit()
    else:
        slow_print("Invalid choice. Try again.")
        entrance()


def torch_room():
    slow_print("\nIt's pitch black inside. You spot an old TORCH on the ground.")
    print("1. Pick up the torch")
    print("2. Continue without it (risky!)")

    choice = input("> ")

    if choice == "1":
        player["has_torch"] = True
        slow_print("You grab the torch. Now you can see!")
        fork_room()
    elif choice == "2":
        slow_print("You venture forward in the dark... and trip on a rock!")
        player["health"] -= 20
        slow_print(f"You lose 20 health. Current health: {player['health']}")
        if player["health"] <= 0:
            game_over()
        else:
            fork_room()
    else:
        slow_print("Invalid choice.")
        torch_room()


def fork_room():
    slow_print("\nThe path splits in two directions.")
    print("1. Go LEFT (you hear water dripping)")
    print("2. Go RIGHT (you see a faint glow)")

    choice = input("> ")

    if choice == "1":
        water_room()
    elif choice == "2":
        glow_room()
    else:
        slow_print("Invalid choice.")
        fork_room()


def water_room():
    if not player["has_torch"]:
        slow_print("\nWithout light, you fall into an underground river!")
        player["health"] -= 30
        slow_print(f"You lose 30 health. Current health: {player['health']}")
        if player["health"] <= 0:
            game_over()
        else:
            slow_print("You crawl out, soaked but alive.")
            treasure_room()
    else:
        slow_print("\nWith your torch, you spot a shiny KEY in the shallow water.")
        player["has_key"] = True
        slow_print("You picked up the key!")
        treasure_room()


def glow_room():
    slow_print("\nThe glow turns out to be glowing mushrooms. Harmless, but useless.")
    slow_print("You continue deeper into the cave.")
    treasure_room()


def treasure_room():
    slow_print("\nYou reach a large chamber. A locked chest sits in the center.")

    if player["has_key"]:
        print("1. Use the key to open the chest")
    print("2. Try to force it open (risky)")
    print("3. Leave it and go home")

    choice = input("> ")

    if choice == "1" and player["has_key"]:
        player["has_treasure"] = True
        win_game()
    elif choice == "2":
        slow_print("You force it open, but a trap triggers!")
        player["health"] -= 40
        slow_print(f"You lose 40 health. Current health: {player['health']}")
        if player["health"] <= 0:
            game_over()
        else:
            player["has_treasure"] = True
            win_game()
    elif choice == "3":
        slow_print("You leave empty-handed, but alive.")
        end_game()
    else:
        slow_print("Invalid choice.")
        treasure_room()


def win_game():
    slow_print(f"\n\U0001F389 Congratulations, {player['name']}! You found the TREASURE!")
    slow_print(f"Final health: {player['health']}")
    slow_print("You exit the cave a legend. THE END.")


def game_over():
    slow_print(f"\n\U0001F480 {player['name']}, you have perished in the cave...")
    slow_print("GAME OVER.")


def end_game():
    slow_print(f"\nThanks for playing, {player['name']}!")


# ---------- Run the game ----------
if __name__ == "__main__":
    intro()
    entrance()
