import random

def play_game():
    player_health = 3

    print("\n=== ADVENTURE GAME ===")
    print("Your goal is to survive and escape.\n")

    print("You wake up in a dark forest.")
    print("There are two paths ahead:")
    print("1. A cave")
    print("2. A river")

    choice1 = input("Choose a path (1 or 2): ")

    # CAVE PATH
    if choice1 == "1":
        print("\nYou enter a dim cave.")
        print("A dragon sleeps atop a pile of treasure.")
        print("Nearby, you see a sword and a bow.")

        print("1. Grab the sword")
        print("2. Grab the bow")
        print("3. Sneak away")

        choice2 = input("What do you do? (1, 2, or 3): ")

        if choice2 == "3":
            print("\nYou step on a rock.")
            print("The dragon wakes up and burns you alive.")
            print("Ending: You died. ")
            return

        if choice2 in ("1", "2"):
            print("\nThe dragon wakes and attacks!")
            dragon_hits = 0

            while player_health > 0:
                print(f"\nYour health: {player_health}/3")

                attack = random.choice(["fire", "claws", "tail"])
                print(f"The dragon attacks with its {attack}!")

                print("1. Dodge")
                print("2. Block")
                print("3. Attack")

                action = input("Choose an action (1, 2, or 3): ")

                if action == "3":
                    if choice2 == "2":
                        print("\nYou fire an arrow into the dragon’s eye!")
                        print("The dragon flees the cave.")
                        print("Ending: You survive! ")
                        return
                    else:
                        print("\nYou strike the dragon with your sword!")
                        dragon_hits += 1
                        if dragon_hits == 2:
                            print("The dragon roars and retreats!")
                            print("Ending: Victory by strength! 🗡️")
                            return

                else:
                    print("The attack hits you!")
                    player_health -= 1

            print("\nThe dragon delivers a final blow.")
            print("Ending: You were defeated. ")
            return

    # RIVER PATH
    elif choice1 == "2":
        print("\nYou reach a rushing river.")
        print("A damaged motorboat is tied to the shore.")

        print("1. Try to hot-wire the boat")
        print("2. Swim across the river")

        choice2 = input("What do you do? (1 or 2): ")

        if choice2 == "2":
            print("\nThe current is too strong.")
            print("Ending: You drown. ")
            return

        if choice2 == "1":
            print("\nYou open the engine panel.")
            print("Two wires stick out: red and blue.")

            wire = input("Which wire do you connect? (red/blue): ").lower()

            if wire == "blue":
                print("\nThe engine explodes!")
                print("Ending: The boat is destroyed. ")
                return

            if wire == "red":
                print("\nThe engine starts!")
                print("You steer downstream.")

                print("1. Toward a village")
                print("2. Toward a dark canyon")

                direction = input("Which way do you go? (1 or 2): ")

                if direction == "1":
                    print("\nYou reach the village safely.")
                    print("Ending: You are rescued! ")
                    return
                else:
                    print("\nThe river speeds up!")
                    print("You plunge over a waterfall.")
                    print("Ending: You did not survive. ")
                    return

    # INVALID INPUT
    else:
        print("\nYou freeze in fear.")
        print("Ending: Lost forever in the forest. ")
        return

# PLAY AGAIN LOOP
while True:
    play_game()

    again = input("\nWould you like to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break