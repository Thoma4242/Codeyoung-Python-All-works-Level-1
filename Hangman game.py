def getWord():
  from wordfile import words
  import random
  return random.choice(words) 

word=getWord()
word=list(word)
print("You have to guess this word: \n","_ "*len(word))

answer="_"*len(word)
answer=list(answer)
while True:
  if answer==word:
    print("You completed the word","Hurray!!")
    break 
  guess=input("Enter your guess: ")
  if guess in word:
    for i in range(len(word)):
      if word[i]==guess:
        answer[i]=guess
        print("Correct guess!")
        print(" ".join(answer))
  else:
    print("Wrong guess!!")
