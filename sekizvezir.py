import random


def oyunTahtasiYarat():
    val = [0] * 8
    for x in range(8):
        val[x] = [0] * 8
    return val


def check(tahta, queen_x, queen_y):
    istenmeyendurum = 0
    #sol çapraza gidiyor
    for i in range(1, 8):
        print("x: {} , y: {}".format(queen_x - i, queen_y + i))
        if queen_x - i > 0 and queen_y - i > 0:
            if tahta[queen_y - i][queen_x - i] != 0:
                print("geldi")
                istenmeyendurum = istenmeyendurum + 1
                print("y: {}  x: {}".format(queen_y - i, queen_x - i))
                break

    #sağ çapraza gidiyor
    for i in range(1, 8):
         print("x: {} , y: {}".format(queen_y - i, queen_x + i))
         if queen_x + i < 8 and queen_y - i > 0:
             if tahta[queen_y - i][queen_x + i] != 0:
                 print("geldi")
                 istenmeyendurum = istenmeyendurum + 1
                 print("x: {}  y: {}".format(queen_y - i, queen_x + i))
                 break
    for i in range(8):
        for j in range(8):
            if tahta.count(1) > 1:
                print("geldi")
                istenmeyendurum = istenmeyendurum + 1

    print(istenmeyendurum)
    if istenmeyendurum >= 5:
        #Bu değerin yerel optimum olduğu farzedilmiştir
        return check()




def vezirleriYerlestir(tahta):
    for i in range(8):
        tahta[random.randint(0, 7)][i - 1] = 1
    return tahta


tahta = oyunTahtasiYarat()
tahta = vezirleriYerlestir(tahta)

for i in range(8):
    print(tahta[i])

queen_x = int(input("x: "))
queen_y = int(input("y: "))
check(tahta, queen_x, queen_y)
