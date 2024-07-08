print("Welcome to the Quiz!!")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()

print("Okay! Let's play :) ")
score = 0

#Q1
answer = input("What does CPU stand for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct! Answer")
    score += 1
else:
    print("Incorrect!")

#Q2
answer = input("What does GPU stand for? ")
if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print("Correct! Answer")
    score += 1
else:
    print("Incorrect!")

#Q3
answer = input("What are 3 components of the Blockchain trilemma? (Answer in the alphabatical order) ")
if answer.upper() == "DECENTRALIZATION SCALABILITY SECURITY":
    print("Correct! Answer")
    score += 1
else:
    print("Incorrect!")

#Q4
answer = input("What does RAM stand for? ")
if answer.upper() == "RANDOM ACCESS MEMORY":
    print("Correct! Answer")
    score += 1
else:
    print("Incorrect!")

print(f'Your Score is {score} out of 4')
print(f'You secured {(score/4) * 100}%')
