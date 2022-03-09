#python 3.7.1
 
user_input=input("Do you want to play? ")
if user_input.lower() != "yes":
  quit()
  
print("Okay! Lets play :)")
score=0

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score +=1
else:
  print("incorrect!")  
  user_input=input("Do you want to continue? ")
  if user_input.lower()!= "yes":
    quit()
    
print("Here is second question for you : ")

answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
  print("Correct answer!")
  score +=1
else:
  print("incorrect!")  
  user_input=input("Do you want to continue? ")
  if user_input.lower()!= "yes":
    quit()

print("Here is third question for you : ") 

answer = input("What is GPU stands for? ")
if answer.lower() == "graphics processing unit":
  print("Correct answer!")
  score +=1
else:
  print("incorrect!")  
  user_input=input("Do you want to continue? ")
  if user_input.lower()!= "yes":
    quit()

print(f"Your score is {score} :)\nKeep smiling")













