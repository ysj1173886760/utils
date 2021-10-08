import random

print("welcome to russian roulette, you can use this program to decide whether you should learn")
bullet = input("please enter the number of bullets, range from 1 to 5:")

bullet = int(bullet)
if bullet < 1 or bullet > 5:
    print("no cheatting!")
else:
    # (6 - number) / 6 * 0 + number / 6 * x = 10
    x = 60 / bullet
    ran = random.randint(0, 5)
    if ran < bullet:
        # bang
        print("you got shot, please go to learn for {} minutes".format(int(x)))
    else:
        print("lucky you, go for a entertainment now")
