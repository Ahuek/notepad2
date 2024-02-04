from tkinter import *
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
root=Tk()
root.configure(background='light blue')
def save_file():
    file_save=filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_save,'w') as file:
        file.write(t.get('1.0',END))
def new_file():
    t.delete('1.0',END)
def exit():
    root.quit()
def cc():
    my_colour=ColorChooserDialog()
    my_colour.show()
    a=my_colour.result
    root.configure(background=a.hex)
def fg():
    b=ColorChooserDialog()
    b.show()
    d=b.result
    t.configure(fg=d.hex)
def open():
    file = filedialog.askopenfile(mode='r', title='Select a file', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if file is not None:
     content = file.read()
    # Do something with the content, for example insert it into a Text widget
     t.insert('1.0', content)


b1=Button(root,text='save file',bg='blue',command=save_file)
b2=Button(root,text='New file',bg='blue',command=new_file)
b3=Button(root,text='exit',bg='blue',command=exit)
b4=Button(root,text='colour picker',bg='blue',command=cc)
b5=Button(root,text='text colour picker',bg='blue',command=fg)
button = Button(root, text='open', command=open)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
button.pack()
t=Text(root,width=10000,height=1000)
t.pack()
root.mainloop()