import random 

roller = random.randint(1,10)
attempt=0
maxAttempts = 5

while True:
    play = int(input("Guess a number between 1-10 : "))
    attempt +=1

    if play < roller :
        print("Hmm too low 📈")

    elif play > roller:
        print("Hmm too high 📉")
    
    elif play == roller:
        print("Congratulations😍 you got it ")
        print(f"Total attempts : {attempt}")
        break
    
    if attempt >= maxAttempts:
        print(f"Game Over sorry you LOSE😭 The Number is {roller}")
        break 