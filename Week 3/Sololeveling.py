#Author: Simire Simeon Obamiegie

# Solo Leveling: A Python Script to Simulate Character Leveling
# Creativity Add-On: Includes nested survival logic, multiple endings, and formatted output for dramatic effect.
# This game is from came from my inspiration of an Japanese anime. Unliike the animated series this game program give an alternate option to the user
# where all option leads to the development of the character.

def solo_leveling_game():
    print("Welcome to Solo Leveling!\n")
    
    # Level 1 – The Double Dungeon Trap
    user = input("Please enter your name: ")
    print(f"\nYou are {user}, a weak hunter striving to become the strongest.")
    print("Complete quests and defeat monsters to level up!\n")
    
    print("Your raid party enters a \033[1mD-RANK DUNGEON\033[0m, but inside you discover a \033[1mSECOND HIDDEN ROOM\033[0m.")
    print("Choices: \033[1mENTER / LEAVE\033[0m")
    choice = input("What will you do? ").upper()
    
    survived = False  # Track survival for awakening

    if choice == "ENTER":
        print("\nThe doors slam shut. You are trapped with deadly \033[1mSTATUES\033[0m that move when rules are broken.")
        print("The statues begin to move towards you. You must act quickly!")
        print("Choices: \033[1mKNEEL / RUN / FIGHT\033[0m")
        action = input("What will you do? ").upper()

        if action == "KNEEL":
            print("\nThe statues pass by you as you kneel in submission. You survive!")
            survived = True

        elif action == "RUN":
            print("\nYou break the rule of staying still! The statues catch you. You perish. \033[1m(Game Over)\033[0m")

        elif action == "FIGHT":
            print("\nYou attempt to fight the statues, but they are too powerful.")
            print("Choices: \033[1mDODGE / ATTACK / HIDE\033[0m")
            fight_choice = input("What will you do? ").upper()

            if fight_choice == "DODGE":
                print("\nYou skillfully dodge the statues' attacks and survive!")
                print("But not for long... You need to level up to face greater challenges ahead.")
                survived = True

            elif fight_choice == "ATTACK":
                print("\nYou break the rule of not attacking! The statues overpower you. You perish. \033[1m(Game Over)\033[0m")

            elif fight_choice == "HIDE":
                print("\nYou hide successfully, avoiding the statues' notice. You survive!")
                print("But not for long... There is no place to hide in this Challenge.")
                survived = True

            else:
                print("\nInvalid choice. The statues overwhelm you. \033[1m(Game Over)\033[0m")

        else:
            print("\nInvalid choice. The statues catch you while you hesitate. You perish. \033[1m(Game Over)\033[0m")

        # Awakening logic
        if survived:
            print("\nYou awaken in a hospital bed, but something feels different...")
            print("A \033[1mSYSTEM WINDOW\033[0m appears before your eyes.")
            print("Choices: \033[1mACCEPT / IGNORE\033[0m")
            sys_choice = input("What will you do? ").upper()

            if sys_choice == "ACCEPT":
                print("\nYou accept the system's offer. You feel a surge of power!")
                print("Congratulations! You have leveled up to \033[1mLEVEL 2\033[0m!")
                print("New Ability Unlocked: \033[1mSHADOW EXTRACTION\033[0m – Extract shadows from defeated enemies to gain strength.")
                print("\033[1mYou Win!\033[0m")

            elif sys_choice == "IGNORE":
                print("\nYou ignore the system's offer. You remain weak, missing your chance at greatness. \033[1m(Game Over)\033[0m")

            else:
                print("\nInvalid choice. The system vanishes. You lose your chance. \033[1m(Game Over)\033[0m")

    elif choice == "LEAVE":
        print("\nThe party mocks you for cowardice, but you survive while others perish.")
        print("You live... but remain weak. \033[1m(Game Over)\033[0m")

    else:
        print("\nInvalid choice. The dungeon consumes you. \033[1m(Game Over)\033[0m")


solo_leveling_game()