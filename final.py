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
    print("Retry?: y = Yes, n = No")
    A = input()
    if A == "y":
        continue
    if A == "n":
        print("\n Decided for sure?: y = Yes, n = No")
        B = input()
        if B == "n":
            continue
        elif B == "y":
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