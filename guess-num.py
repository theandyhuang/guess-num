import random
awnser = random.randint(1,100)
count = 0
while True:
    guess = input("請猜一個1~100的整數: ")
    guess = int(guess)
    count += 1
    if guess == awnser:
        print("終於猜對了!")
        print("你共猜了", count , "次")
        break
    elif guess > awnser:
        print("比答案大!")
    else:
        print("比答案小!")
    print("你猜", count , "次了")
