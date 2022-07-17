import random

n = int(input("Please, enter the right border: "))

randNum = random.randint(1, n)
count = 0


def is_valid(yourNum):
    if 1 <= yourNum <= n:
        return True
    else:
        return False


act = True
while act:
    yourNum = int(input("Please, enter your guessed number: "))
    if is_valid(yourNum):
        if yourNum == randNum:
            count += 1
            print("Congratulations, you won!")
            print(f"The number of attemts to guess the number was {count}")
            print("If you want to play one more time, please, write'yes'")
            if input() == 'yes':
                n = int(input("Please, enter the right border: "))
                randNum = random.randint(1, n)
                act = True
            else:
                print("Ok,goodbye, thanks for the game!")
                act = False
        elif yourNum > randNum:
            count += 1
            print("Please, try again. Your number is bigger")
        elif yourNum < randNum:
            count += 1
            print("Please, try again. Your number is smaller")
    else:
        print(f"Please, enter the correct number in the range from 1 to {n}")
