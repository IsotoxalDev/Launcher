import os
from tkinter import filedialog
import tkinter


def Label(text, tk, row = 0, col = 0):
    tkinter.Label(tk, text = text, padx = 10).grid(row = row, column = col)

def Entry(tk, width, row = 0, col = 0):
    t = tkinter.Entry(tk, width = width)
    t.grid(row = row, column = col)
    return t

class Launcher:

    tk = tkinter.Tk()
    name = None
    exec = None
    e_path = None
    icon = None
    i_path = None

    def __init__(self):
        self.tk.title('Add Launcher - Abhinav')
        self.tk.geometry('555x120')
        Label('Name: ', self.tk)
        self.name = Entry(self.tk, 50, 0, 1)
        Label('Exec: ', self.tk, 1)
        self.exec = Entry(self.tk, 50, 1, 1)
        tkinter.Button(text = 'Browse', command = self.exec_path).grid(row = 1, column = 2)
        Label('Icon ', self.tk, 2)
        self.icon = Entry(self.tk, 50, 2, 1)
        tkinter.Button(text = 'Browse', command = self.icon_path).grid(row = 2, column = 2)
        tkinter.Button(text = 'Continue', command = self.next, padx = 100).grid(row = 3, column = 1)
        self.tk.mainloop()
    def set_location(self, file, entry):
        entry.insert(0, file)

    def exec_path(self):
        file = filedialog.askopenfilename(initialdir = "~",title = "Select Executable")
        self.e_path = file
        self.set_location(file, self.exec)

    def icon_path(self):
        file = filedialog.askopenfilename(initialdir = "~",title = "Select Icon")
        self.i_path = file
        self.set_location(file, self.icon)

    def next(self):
        self.name = self.name.get()
        text = '[Desktop Entry]\nName='+self.name+'\nExec='+self.exec.get()+'\nTerminal=false\nType=Application\nIcon='+self.icon.get()
        #os.system('touch ~/.local/share/applications/'+self.name+'.desktop')
        f = open('../../.local/share/applications/'+self.name+'.desktop', 'w')
        f.write(text)
        f.close()
        #os.system('chmod +x '+self.name+'.desktop')
        #f = open('../../.local/share/applications/'+self.name+'.desktop', 'r')
        #print(f.read())
        exit()
        #print(text)

launcher = Launcher()
