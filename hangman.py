'''
author : David Gilbert
problem : hangman game python
'''
import random as r 

def setup():
    global word 
    global tries
    words = ["exposure","strikebreaker","deck","sandwich","make","commemorate","wedding","staircase","allow","urgency"]
    word = words[r.randint(0,len(words)-1)]
    print(word)
    tries = len(word)+2
    print("you have " + str(tries) +" tries to guess the word" )
    for x in range (0,len(word)):
        found.append(0) 
    
    
def guess():
    global found,tries,word,won
    
    letter = input("enter a letter you think is in the word or guess the whole word\n")
    
    if(len(letter) == 1): #letter input
        count = 0 
        boo = False
        for wordLetter in word:
            if(letter == wordLetter):
                found[count] = 1 
                boo =True
            count += 1
        if(boo == False):
            tries -= 1
    else: #word guess input
        if(letter == word):
            print("Congradulation you won !!!\nyour word was "+ word)  
            won = True
        else:
            tries -= 1
            
            
        
        
def printCurrent():
    global word
    print("current guess : ")
    for x in range(0,len(word)):
        if(found[x] == 1 ):
            print(word[x]+ " ",end='')
        else:
            print("_ ",end='')
    #print("\n")

def checkWin():
    global word
    global won
    global found
    for x in range (0,len(word)):
        if(found[x] == 0):
            return 
    print("Congradulation you won !!!\nyour word was "+ word)    
    won = True
     
    
def main():
    global tries
    print("welcome to my hangman game \nyou will be ask to enter every letter in an hidden word in order to win\nGood Luck ! ")
    setup()
    while(True):
        printCurrent()
        guess()
        checkWin()
        if(won == True):
            return
        if(tries == 0 ):
            print("you lost :(" )
            break 
        print (tries," tries left")
    
won = False 
found = []
word = ""
current = ""
tries = 0 
main()
