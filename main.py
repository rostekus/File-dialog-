from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog




root = Tk()
root.title('Paint')
root.geometry('1000x400')
root.resizable(0,0)
root.configure(background = 'white')



#=========================
def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

def new_file():
    pass

def save_file():
    pass

def open_file():
    pass

def rotate_left():
    pass

def rotate_right():
    pass


# Menu
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu =Menu(my_menu)
edit_menu = Menu(my_menu)

my_menu.add_cascade(label='File', menu = file_menu)
my_menu.add_cascade(label='Edit',menu = edit_menu)
#=========================
file_menu.add_command(label='New',command = new_file)
file_menu.add_command(label= 'Open...', command = open_file)
file_menu.add_command(label= 'Save', command = save_file)
file_menu.add_command(label= 'Exit', command = root.quit)

edit_menu.add_cascade(label = 'Rotate right', command= rotate_left)
edit_menu.add_cascade(label = 'Rotate left', command = rotate_left)
#=========================
main_frame = LabelFrame(root,bg = 'grey')
main_frame. grid(row =0, column =0)

frame_colors = LabelFrame(main_frame,text = 'Color', bg='grey',relief = RIDGE)
frame_colors.grid(row=1, columnspan=2, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

frame_tool = LabelFrame(main_frame,text = 'Tools', bg='grey',relief = RIDGE)
frame_tool.grid(row=6, columnspan=2, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
#=========================
colors = {'red': '#FF0000', 'yellow' : '#FFFF00','orange' : '#FFA500', 'purple' : '#800080', 'white' : '#FFFFFF', 'black': '#000000', 'blue':'#0000FF'}

i,j=0,0
for color in colors:
    Button(frame_colors,bg=color, text = color,width = 5).grid(row = i, column= j)
    if i < 3:
        i += 1
    else:
        j +=1
        i=0
#=========================

Button(frame_tool,bg=color, text = "ERASER",width = 5).grid(row = 0, columnspan = 2)
Button(frame_tool,bg=color, text = "CLEAR",width = 5).grid(row = 1, columnspan = 2)

#=========================






root.mainloop()




