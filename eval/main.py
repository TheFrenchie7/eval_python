import random
import time
from joueur import Joueur1, Joueur2 

J1 = Joueur1()

J2 = Joueur2()

case = []

for i in range(20):
    case.append(random.randint(0, 200))
for i in range(20):
    case.append(random.randint(-450, -1))

random.shuffle(case)


def game(x):

    d = 0
    d = (random.randint(1,6) + random.randint(1,6))
    x.position = x.position + d

    if x.position >= 30:
                
        x.position = x.position - 31
                
    else:

        x.money = x.money + case[(x.position)]

    print("Le joueur",x.name ,"à fait", d)
    time.sleep(1)
    print("le joueur",x.name ,"est sur la case", x.position, "qui est à :",case[(x.position)],"€")
    print("Le joueur",x.name ,"à:", x.money,"€")
    time.sleep(2)
    print("")

if __name__ == "__main__":

    while J1.money > 0 and J2.money > 0:

        game(J1)

        game(J2)

    if J1.money <= 0:

        print("Le joueur 1 à perdu.")

    else:

        print("Le joueur 2 à perdu")   
