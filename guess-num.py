import random
awnser = random.randint(1,100)
while True:
    guess = input("請猜一個1~100的整數: ")
    guess = int(guess)
    if guess == awnser:
        print("終於猜對了!")
        break
    elif guess > awnser:
        print("比答案大!")
    else:
        print("比答案小!")
