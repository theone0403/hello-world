import random
print ("select your name")
I = input()

health = 75
armor = 0
attack = 0

power = 0
mental = 0
luck = 0

energy = 0
escape = 0

while 1:
    power = random.randrange(5, 11)
    health = health + power*1
    attack = power
    mental = random.randrange(1, 6)
    luck = random.randrange(1, 6)
    print(f"power ={power}, defense power = {mental}, escape = {luck}")
    print("Retry?: a = Yes, b = No")
    A = input()
    if A == "a":
        continue
    if A == "b":
        print("\n Decided for sure?: a = Yes, b = No")
        B = input()
        if B == "b":
            continue
        elif B == "a":
            print("\n You've been decided")
            print(f"""
        [Status]
        name = {I}
        job = soldier
        health = {health}
        fighting power = {power}
        defense power = {mental}
        escape = {luck}""")
            break

print("Are you ready to adventure?")

#I really like the idea. I get some nice turn based rpg style vibes.
#Your code is looking nice, I suppose now you gotta create a little story where the player gets to choose their path.
#The problem with this is that it can quickly turn into a whole lot of work with all the branches the player could take.
#I would maybe recomend keeping the story simple where the there are only a couple endings and branches end up merging to give the elusion of choice like in The walking dead games.
