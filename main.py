import random
def decrease_attempts(attempts):
    return attempts-1
def choose_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level=="easy":
        return 10
    if level=="hard":
        return 5
    else:
        return choose_difficulty()

def start_guess():
    rand_number=random.randint(1,100)
    print(rand_number)
    attempts_number=choose_difficulty()
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    finished=False
    while not finished:
        print(f"You have {attempts_number} remaining to guess the number.")
        guess_number=int(input("Make a guess "))
        attempts_number=decrease_attempts(attempts_number)
        if guess_number>rand_number:
            print("Too hight")
        if guess_number<rand_number:
            print("Too low")
        if guess_number==rand_number:
            finished=True
            print("You win")
        if attempts_number==0:
            finished=True
            print("You lose")
start_guess()
while input("You want to start again? to start again type 'Y', to exit type any key ").lower()=="y":
    start_guess()
