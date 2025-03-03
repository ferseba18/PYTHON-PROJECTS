print("Quiz Time")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Play time! Let's go!")
score = 0
answer = input("How many days are in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USA stands for? ")
if answer.lower() == "united states of america":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")