##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
# create_oval(x,y,width,height,fill color)
oval = drawpad.create_oval(10, 50, 100, 100, fill='green')

#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
#this is the base of the house

square = drawpad.create_rectangle(300,300,600,700, fill='red')
#this square is the upper left window currently
sq2 = drawpad.create_rectangle(325,325,375,350, fill='black')


#create_line(top left x,top left y, bottom right x, bottom right y, fill color)

#this is the line that connects the left part of the house to the top of the roof
line = drawpad.create_line(300, 300, 450, 100)
#this is the line that connects the right part of the house to the top of the roof
line2 = drawpad.create_line(600, 300, 450, 100)

root.mainloop()

