import random
import sys

# move around the dungeon until the exit is actually found
# monsters to hunt
# treasures to find
playerHealth : float = 100.0
roll : int = 0
print("""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-Lee|  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888(FL)888
You open a door you just found under your computer desk, and are pulled
in... Perhaps you should get out... but wait... you can't? Better look
around for an exit!\n
""")
print ("How would you like to begin?")
while 1 != roll:
    print("""Q - Get out of here!
    W - Walk forward
    A - Walk left
    S - Walk backwards
    D - Walk right""")
    print(f"Your health is {str(playerHealth)}")
    choice = input(">>> ").strip().upper()
    if "Q" == choice:
        print("Haha! Just kidding! You're stuck here forever!!!")
    elif choice in "WASD":
        print("You walk into the darkness...")
        roll : int = random.randint(1, 100)
        if  1 == roll:
            print("Somehow you got out without dying. Next time the hamsers will be bigger.")
            break
        elif roll in range(2, 11):
            print(f"A wild {random.choice(["hamster", "goldfish", "squirrel", "mouse"])} appears! EEEEEE!!")
        elif 66 == roll:
            print("""You found treasure! No, I mean it!
            ... Though it doesn't really change your present situation.
            You're still in the dungeon.""")
        elif roll in range(67, 69):
            print(f"You found {random.choice(["a faulex watch", "nikee shoes", "a TEMU game console"])}...")
            print("You die from bootleg goods exposure. The Lawyers sell your body for copyright infringement.")
            playerHealth = 0
        elif roll in range(random.randint(12, 20), random.randint(25, 32)):
            print("""You hurt yourself embarassingly." \
            "When you get out you'll tell everyone you survived a brutal trap!""")
            playerHealth -= random.randint(1, 11)
        elif roll in range(random.randint(32, 38), random.randint(39, 45)):
            print("Don't worry. We won't tell anyone you just ate something off a dirty floor.")
            playerHealth += random.randint(1, 5) if bool(random.random()) else -random.randint(1, 5)
        elif roll in range(50, 66):
            monsterName = random.choice(["Wumpus", "Chungus", "Milhouse"])
            print(f"A wild {monsterName} appears!")
            monsterHealth : int = random.randint(7, 15)
            while monsterHealth > 0 and playerHealth > 0:
                damage = random.randint(1, 5)
                playerHealth -= damage
                if 0 >= playerHealth:
                    continue
                print(f"The {monsterName} hits you for {damage} damage! Your health is now {playerHealth}.")
                print("""What do you do?
                A - Attack
                R - Run""")
                fightChoice = input(">>> ").strip().upper()
                if "A" == fightChoice:
                    damage = random.randint(1, 5)
                    monsterHealth -= damage
                    print(f"You hit the {monsterName} for {damage} damage!")
                elif "R" == fightChoice:
                    print("You try to run, but fail in a way that you'll never forget, but can never describe.")
                    damage = random.randint(2, 6)
                    playerHealth -= damage
                    print(f"The {monsterName} kicks you while running for {damage} damage.")
                else:
                    damage = random.randint(1, 5)
                    playerHealth -= damage
                    print(f"You're hesitant nature got you punched in the face. {damage} damage.")
    else:
        print("wut?")
    if 0 == int(playerHealth):
        print("Thou art dead. You Lose! Good day sir!")
        sys.exit()