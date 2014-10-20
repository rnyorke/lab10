# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# base
square = drawpad.create_rectangle(100,500,500,300, fill='red')

# windows
sq1 = drawpad.create_rectangle(125,400,200,450, fill='white')
sq2 = drawpad.create_rectangle(400,400,475,450, fill='white')
sq3 = drawpad.create_rectangle(125,325,200,375, fill='white')
sq4 = drawpad.create_rectangle(400,325,475,375, fill='white')
ln1 = drawpad.create_line(162.5,400, 162.5, 450)
ln2 = drawpad.create_line(162.5,325, 162.5, 375)
ln3 = drawpad.create_line(437.5,400, 437.5, 450)
ln4 = drawpad.create_line(437.5,325, 437.5, 375)
ln5 = drawpad.create_line(125,425, 200, 425)
ln6 = drawpad.create_line(400,425, 475, 425)
ln7 = drawpad.create_line(125,350, 200, 350)
ln8 = drawpad.create_line(400,350, 475, 350)


# roof
line = drawpad.create_line(100, 300, 300, 100)
line2 = drawpad.create_line(300, 100, 500, 300)

# chimney
l1 = drawpad.create_line(150, 250, 150, 150)
l2 = drawpad.create_line(150, 150, 220, 150)
l3 = drawpad.create_line(220, 150, 220, 180)

# door
door = drawpad.create_rectangle(275,500,325,400, fill='brown')


#doorhandle 
hndl = drawpad.create_oval(310,440,320,450,fill = 'orange')

# Grass

sq4 = drawpad.create_rectangle(0,500,800,600, fill='green')


root.mainloop()