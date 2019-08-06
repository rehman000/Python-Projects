import math
import random
from tkinter import *

# TODO: I need to pass the Strings from the Front End into this!!!!! 


#=========================================================================================================================================
# Front End: 
#=========================================================================================================================================
window = Tk() 
window.title("CSC 113: Final Project")
window.geometry("840x340+0+0")

label = Label(window, text = " Make sure the File is in the Right Directory! ", font=("arial",20,"bold"), fg="steelblue").pack()

label2 = Label(window, text = " Enter the File Name: ", font=("arial",18,"bold"), fg="black")
label2.place(x=10, y=30)

label2 = Label(window, text = " Enter the Number of Characters: ", font=("arial",18,"bold"), fg="black")
label2.place(x=10, y=65)

label3 = Label(window, text = "The File Name is:   Words.txt   ", font=("arial",20,"italic"), fg="red")
label3.place(x=10, y=270)



User_Input = StringVar()
e1 = Entry(window, fg = "Green", bd = 5, bg = "black", textvariable = User_Input) 
e1.pack()


def Button_1_Click():
	Return_Value = str(User_Input.get())
	return Return_Value 

btn1 = Button(window, bd = 10, bg = "Green", fg = "Black", text="Submit", padx=30, pady=5, command = Button_1_Click )
btn1.place(x=580, y=30)


n = IntVar()
e2 = Entry(window, fg = "Green", bd = 5, bg = "black", textvariable = n) 
e2.pack()

def Button_2_Click():
	Return_Value = int(n.get())
	return Return_Value

btn2 = Button(window, bd = 10, bg = "Green", fg = "Black", text="Submit", padx=30, pady=5, command=Button_2_Click )
btn2.place(x=580, y=70)


Kill = Button(window, text="Please Submit BOTH values First! Click on me last To See The Pie Chart! ", padx=80, pady=5, command=window.destroy)
Kill.place(x=120, y=160)

window.mainloop()

#=========================================================================================================================================
#=========================================================================================================================================







#=========================================================================================================================================
# Read File Function: 
#=========================================================================================================================================


def Read_File():

    # Get the file name:
    filename = Button_1_Click()
    
    # Get the Number of Characters: 
    Number_of_Characters = Button_2_Click()

    # open the file in read mode: 
    fileContent = open(filename,'r')             #  fileContent goes through the entire file!

    readContents_str = fileContent.readlines()

    letterdictionary={}

    print("\n*********** Printing the text file **********\n ")

    #iterate the file contents

    for char in readContents_str:
        print(char, type(char))

        for letter in char:
            letterCount = char.count(letter)
            letterdictionary[letter] = letterCount

    with open(filename) as fileContent:
        lines = 0
        words = 0
        characters = 0
        for line in fileContent:
            wordslist=line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)     # This way we exclude whitespaces! "\n", and "\t". 
            

    # Sum of the Frequency of All the letters! Initialize it to zero by Default!  
    Frequency_Sum_Total = 0

    # find the Frequency_Sum_Total: 
    
    if(Number_of_Characters > 0 and Number_of_Characters < characters):
        characters = Number_of_Characters            # This way the user input is used in determining probabilty.  

    Frequency_Sum_Total = characters

    # Display statement: 

    print("\n********** Frequencies of all Letters from file ************\n")
    print("Frequencies of all Letters " ,Frequency_Sum_Total)
    print("\n*********** Probability of each letter from file ************\n")

    # Find the probability of Letter: 

    Letter_Array = []

    Sum_of_Probability = 0

    for letter,letterCount in letterdictionary.items():

        probabilityofLetter = letterCount/int(Frequency_Sum_Total)

        print("\n")

        print("probability of Letter: ", letter, ": \t", probabilityofLetter)
	# Prints out the letter followed by it's probabilty 
        
        Sum_of_Probability = Sum_of_Probability + probabilityofLetter

        print("\n")
        Letter_Array.append(probabilityofLetter)                                 # Store that letter in the array of special characters!

    print("Probability of: i\tProbability of: s\tProbability of: e")
    print(set(Letter_Array))

    # Return the sum of frequency of all letters in the other file: 

    return (Number_of_Characters, Frequency_Sum_Total, set(Letter_Array), Sum_of_Probability)


#=========================================================================================================================================
#=========================================================================================================================================
