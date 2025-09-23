import random

def test_random():
    # สุ่มเลขระหว่าง 1 - 10 เก็บไว้ในตัวแปร random_number
    random_number = random.randint(1, 100)

    # รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปร guess_number
    guess_number = input("What is your guess number?: ")
    guess_number = int(guess_number)

    if random_number == guess_number:
        print("Congratulations")

    elif random_number < guess_number:
        print("Too much")

    elif random_number > guess_number:
        print("Too low")

    print(random_number)
    
test_random()
