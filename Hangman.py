#Starting with the hangman project

#Import the random modules which will be used to randomly select a word from the list
import random
import hangman_art as ha
import hangman_words as hw

#importing the hangman art as (ha)
print(ha.logo)

#importing the hangman wordlist from the hangman wordlist class as (hw)
word_list = hw.word_list
#word_list = ["ardvak","baboon","camel"]

#Randomly Picking a word from the word_list
#Into a variable called choosen_word
choosen_word = random.choice(word_list)

#Testing Code
#print("The chosen word is {}".format(choosen_word))

#Creating an empty list called display
Display = []

i = 0

#Appending Underscore to the display list
#Using the length of the choosen word
while i < len(choosen_word):
    Display.append("_")
    i+=1

lives = 6

#Using the while loop to loop through the display list
# #if there are no more underscores in the display list 
while '_' in Display:
    #Asking the user to pick a letter
    guess = input("Guess a letter ").lower()

    #Checking if the user has already guessed a word in the choosen word
    if guess in Display:
        print("You have already guessed {} so please try a different letter".format(guess))

    #Using the range function to loop through the index of the choosen_word
    #And replacing the guess letter to the display list 
    for i in range(0, len(choosen_word)):
        if guess == choosen_word[i]:
            Display[i] = guess
    print(' '.join(Display))
        
    
    #Checking if the wrong gussed word is in the updated Display list
    #If not it should decrease the live 
    #and print the hang man
    if not guess in Display:
        print("The letter {} is not in the word you have loss a life".format(guess))
        lives-=1
        print(ha.stages[lives])
    #If the the number lives is = 0 the loop should break
    #This is used to check the number of lives and break out of the loops
    if lives == 0:
        break
display = ''.join(Display)
if display == choosen_word:
    print(display)
    print("You Won!!!")
else:
    print("You loose!!!")
    #Using the for loop to loop through the choosen word 
    #To check if a selected word from the user is in the list or string
    #for letter in choosen_word:
    #    if guess == letter:
    #       Display[letter] = guess
    #print(Display)