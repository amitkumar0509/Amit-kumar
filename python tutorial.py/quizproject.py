print('WELCOME TO MY COMPUTER QUIZ!')
playing=input('Do you want to play?')
if playing != "yes":
   quit()
   
print("okay!,let's play:)")
score=0
answer=input("what is short form of central processing unit")
if answer=="cpu":
    print("CORRECT! ")
    score==1

else:
    print("INCORRECT!")
    
answer=input("WHAT IS THE SIGN OF MAGNESIUM METAL?")
if answer.lower()=="MG":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")
    

