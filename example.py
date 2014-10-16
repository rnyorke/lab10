##########################################
#                                        #
#    Example of drawing with Canvas      #
#                                        #
##########################################

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='brown')
drawpad.grid(row=0, column=1)
# create_oval(x,y,width,height,fill color)
oval = drawpad.create_oval(10, 50, 100, 100, fill='green')
#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
square = drawpad.create_rectangle(300,300,600,700, fill='red')
#create_line(top left x,top left y, bottom right x, bottom right y, fill color)
line = drawpad.create_line(0, 0, 200, 100)
root.mainloop()