import os
try:
    import tkinter
    from tkinter import filedialog
except:
    print("It looks like you don't have tkinter.\n If you are on a Debian based distro(ubuntu. pop OS, Linux Mint) type: DEB\nIf you are on a Arch based distro(Manjaro, Arco Linux) type: ARCH\n If you are on redhat basd distro(Fedoro, RHEL) type: RH\n If you are on another distro please install tkinter with your distro's package manager (<ctrl + c> to exit). Thank You! ")
    DISTRO = input("Your Input: ")
    if DISTRO == "DEB":
            os.system("sudo apt install python3-tk")
            from tkinter import filedialog
            import tkinter
    elif DISTRO == "ARCH":
            os.system("sudo pacman -S tk")
            from tkinter import filedialog
            import tkinter
    elif DISTRO == "RF":
            os.system("sudo dnf install python3-tkinter")
            from tkinter import filedialog
            import tkinter
    else:
            print("Wrong Input")
            import sys
            sys.exit()

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
        self.tk.geometry('555x130')
        Label('Name: ', self.tk)
        self.name = Entry(self.tk, 50, 0, 1)
        Label('Exec: ', self.tk, 1)
        self.exec = Entry(self.tk, 50, 1, 1)
        self.WEB = 0
        self.checkWeb = tkinter.Checkbutton(self.tk, text='Web', onvalue=1, offvalue=0, command=self.web)
        self.checkWeb.grid(row = 3, column = 1)
        tkinter.Button(text = 'Browse', command = self.exec_path).grid(row = 1, column = 2)
        Label('Icon ', self.tk, 2)
        self.icon = Entry(self.tk, 50, 2, 1)
        tkinter.Button(text = 'Browse', command = self.icon_path).grid(row = 2, column = 2)
        tkinter.Button(text = 'Continue', command = self.next, padx = 100).grid(row = 4, column = 1)
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

    def web(self):
        self.WEB = 1 if self.WEB == 0 else 0

    def next(self):
        self.name = self.name.get()
        if self.WEB == 1:
            text = '[Desktop Entry]\nName='+self.name+'\nExec=xdg-open '+self.exec.get()+'\nTerminal=false\nType=Application\nIcon='+self.icon.get()
        else:
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
