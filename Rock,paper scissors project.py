game=["Rock","Paper"]
player=["Ram","Joseph"]
choice=input("Enter R for Rock \n Enter P for Paper :-")
player=input("Enter A for Ram \n Enter J for Joseph:-")
if(choice=="R" and player =="A"):
  print("Rock choosen by Player 1,HE LOSES")
elif(choice=="P" and player=="J"):
  print("Paper choosen by Player 2 and HE WINS!!!")
elif(choice=="R" and player=="A" and player=="J"):
  print("Its a tie and no one wins!")
else:
  print("Invalid!")
print("The program is about the game Rock,Paper and Scissors played by 2 friends Ram and Joseph,with player 1 being Ram and player 2 being Joseph and here JOSEPH wins it")
