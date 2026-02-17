import random

# move around the dungeon until the exit is actually found
# monsters to hunt
# treasures to find

print ("""
How would you like to begin?""")
while 1:
    print("""Q - Get out of here!
    W - Walk forward
    A - Walk left
    S - Walk backwards
    D - Walk right""")
    choice = input(">>> ").strip().upper()
    if choice == "Q":
        print("Haha! Just kidding! You're stuck here forever!!!")
    elif choice in "WASD":
        print("You walk into the darkness...")
        roll : float = random.randint(1, 100)
        if  1 == roll:
            print("You found the exit! You win!")
            break
        elif roll in range(2, 11):
            print(f"A wild {random.choice(["hamster", "goldfish", "squirrel", "mouse"])} appears! EEEEEE!!")
        elif roll in range(67, 69):
            print(f"You found {random.choice(["a folex watch", "nikee shoes", "a TEMU game console"])}...")
            print("You die from bootleg goods exposure. The Lawyers sell your body for copyright infringement. You lose! Good day sir!")
            exit()
    else:
        print("wut?")

print("Somehow you got out without dying. Next time the hamsers will be bigger.")