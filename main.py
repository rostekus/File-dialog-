from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog



root = Tk()
root.title('Paint')


#=========================
def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

def new_file():
    pass

def save_file():
    pass
#=========================

# Menu
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu =Menu(my_menu)

my_menu.add_cascade(label='File',menu=file_menu)
#=========================
file_menu.add_command(label='New',command = new_file)
file_menu.add_command(label= 'Open...', command = open_file)
file_menu.add_command(label= 'Save', command = save_file)
file_menu.add_command(label= 'Exit', command = root.quit)

#=========================


root.mainloop()




