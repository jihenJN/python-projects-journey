playing = input("Do you want to play? ")
if playing.lower() =="yes":
    print("game starts :)")
score=0

answer=input("What CPU stands for? ")
if answer.lower() =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer=input("What GPU stands for? ")
if answer.lower() =="graphics processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer=input("What RAM stands for? ")
if answer.lower() =="random access memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer=input("What ROM stands for? ")
if answer.lower() =="read only memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print("total corrects answers is :" +str(score)+" questions")
print( "you answered "+ str((score/4)*100)+"% "+"correctly")