from threading import Thread
import timeit
import random

t1 = Thread(target = Sleeper)
def Sleeper():
    for i in range (0,150000000):
        pass
    t1.join()

def Dice():
    print("You got a: ",end=" ")
    print(random.randint(0,6))
def Coin():
    n = random.randint(0,10)
    print("Its a: ", end=" ")
    if n%2==0 :
        print("Heads")
    else:
        print("Tails")
def Choice(choose):
    choose=input(">>> ").lower()


def NonBlocking():
    choose = ""
    while choose!="q":
        print("\nMenu\n(D)Throw a Dice\n(C)Toss a Coin\n(Q)Quit")
        t1.start()
        Choice(choose)
        if(choose!="" and t1.is_alive()):
            if choose=="q":
                t1.join()
                break
            if choose=="d":
                Dice()
                choose=""
            elif choose=="c":
                Coin()
                choose=""
            else:
                print("Invalid choice, please choose again\n")
        elif (t1.is_alive == False):
            print("Session Time out")
            break
    print("Thank you for playing")


NonBlocking()