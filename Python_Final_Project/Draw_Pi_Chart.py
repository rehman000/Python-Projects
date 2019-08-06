import tkinter       					# import tkinter module ... 
from Read_File_Contents import Read_File    	 	# import module to find the probability of letters ... 
from decimal import Decimal
import math
import random


# Save the numberofletters from file
(Number_of_Characters, Frequency_Sum_Total, Unique_Letter_List, Sum_of_Probability) = Read_File()


Unique_Letter_List = list(Unique_Letter_List)
All_Other_Probability = Sum_of_Probability - (Unique_Letter_List[0] + Unique_Letter_List[1] + Unique_Letter_List[2])


print("\nReturn Number of Letters: ", Frequency_Sum_Total, "\n")
print("\nFile Terminated Reading at character:  \n", Number_of_Characters)  # So the Python reads files line by line, or character by character
# If you go character by character you need to specify n, otherwise it will just read the whole file. This way the user can determine where he/she can stop reading the file! 

# Draw_Pie_Chart function: 
def Draw_Pie_Chart(n):

    return 360. * n / 500


# Set the tkinter window height and width: 
Window = tkinter.Canvas(width = 350, height = 350);

Window.pack()

# Create arc in the pie chart through canvas


#============================================================================================================

Window.create_arc((30,30,280,280), fill="red", start=Draw_Pie_Chart(0), extent = Draw_Pie_Chart(100))
Window.create_text((310,75),text = "i : " + str(round(Unique_Letter_List[0],4)))


Window.create_arc((30,30,280,280), fill="blue", start=Draw_Pie_Chart(100), extent = Draw_Pie_Chart(400))
Window.create_text((300,250),text = "s : "+ str(round(Unique_Letter_List[1],4)))


Window.create_arc((30,30,280,280), fill="green", start=Draw_Pie_Chart(400), extent = Draw_Pie_Chart(100))
Window.create_text((110,300),text = "e : " + str(round(Unique_Letter_List[2],4)))


Window.create_arc((30,30,280,280), fill="yellow", start=Draw_Pie_Chart(600), extent = Draw_Pie_Chart(200))
Window.create_text((80,90),text = "\n Other Letters, " + str(round(All_Other_Probability,4)))

#============================================================================================================


print("********************[ Press the red X button to escape back to the terminal ]************************\n")

Window.mainloop()
