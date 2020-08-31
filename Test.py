from threading import Thread
import timeit
import random

#To Simulate a clock...Basically to pass some Defined Time
def Sleeper():
    for i in range (0,150000000):
        pass

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
        t1 = Thread(target = Sleeper)
        t2 = Thread(target = Choice, args=(choose,))
        t1.start()
        t2.start()
        #print("choose is: ", choose)
        if(choose!="" and (t1.is_alive())):
            if choose=="q":
                break
            if choose=="d":
                Dice()
                choose=""
                t2.join()
            elif choose=="c":
                Coin()
                choose=""
                t2.join()
            else:
                print("Invalid choice, please choose again\n")
                t2.join()
        elif (t1.is_alive == False):
            print("Session Time out")
            choose = "q"
    print("Thank you for playing")

    NonBlocking()