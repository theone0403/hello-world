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

input(f"\n{I}: Where am I, why is it so quiet here")
input(f"\nenemey {I}: You’ve activated my trap card, lets fight!")
input(f"\n{I}: Wait doppelganger was real? ?")
input(f"\nenemy {I}: kahahahaha lets start the battle I going to take your body after beating you")
input(f"\n{I}: ? ? ? !")

enemyhealth = 50
enemyarmor = 0
enemyattack = 7
enemyenergy = 0
enemymental = 0
print(f"enemy {I}'s health: {enemyhealth}")
health1 = health

while 1:
    print(f"\n{I}'s turn! ! !")
    time.sleep(1)
    N = input("q)attack w)defend e)skill r)run\n")
    if N == "q":
        print(f"{I} attacked enemy")
        attack1 = attack + random.choice([1, 2, 3, 5, 8])
        if attack1 - enemyarmor <= 0:
            print("enemy shield your attack")
            enemyarmor -= attack1
        else:
            enemyhealth -= (attack1 - enemyarmor)
            print(f"enemy's remain health = {enemyhealth}")
            enemyarmor = 0
    elif N == "w":
        armor += 5 + mental
        print(f'{I} prepared to shield the attack. Defense power became {armor}')
    elif N == "e":
        energy += 1
        print("energy power~")
        if energy ==2:
            print(f"{I} throw energy wave")
            enemyhealth -= mental + random.choice([10, 15, 20, 25, 30])
            print(f"enemy's remain health = {enemyhealth}")
            energy = 0
    elif N == "r":
        escape = random.random()
        if escape < luck/10:
            print(f"{I} successfully runaway from enemy but makes me feel awkward...")
            escape += 1
            break
        else:
            print("I failed to runaway! ! !")
    if enemyhealth <= 0:
        print(f"enemy {I}: damn.... I failed it again I will be back")
        break
        
    N = random.randrange(1, 4)
    print("\nenemey's turn! ! !")
    time.sleep(1)
    if N == 1:
        enemyattack1 = enemyattack + random.choice([1, 2, 3, 5, 8])
        if enemyattack1 - armor <= 0:
            print("I sheild enemy's attack :)")
            armor -= enemyattack1
        else:
            print("enemy striked suddenly")
            health -= (enemyattack1 - armor)
            print(f"{I}'s remain health = {health}")
            armor = 0
    elif N == 2:
        enemyarmor += 5 + mental
        print(f'enemy prepared to shield the attack. Defense power became {enemyarmor}')
    elif N == 3:
        enemyenergy += 1
        print("energy power~")
        if enemyenergy == 2:
            print("enemy's energy wave!")
            health -= enemymental + random.choice([10, 15, 20, 25, 30])
            print(f"{I}'s remain helath = {health}")
            enemyenergy = 0
    if health <= 0:
        print("I'm losing my conciousness")
        print("\ntip: huh..... developer gonna laugh at you :(")
        Count = input("Continue? q: retry w: retry e: retry.\n... ")
        if Count != "if you got this your genious :)":
            t = 4
            while t >= 1:
                t = t - 1
                time.sleep(1)
                print(f" loading {t}second")
                health = health1
                enemyhealth = 50
                enemyarmor = 0
                armor = 0
                continue
