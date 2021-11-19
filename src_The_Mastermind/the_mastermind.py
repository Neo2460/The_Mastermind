'''
date: 15.11.2021
author: Katharina Melchart
The Mastermind
'''

#Imports:
import tkinter as tk


#Classes
class Homescreen():
    def __init__(self, fenster, container):
        self.container = container
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='Enter your password:')
        label.place(x=617, y=220)
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        ohne = Intruder_Library(fenster, container)

        self.e1 = tk.Entry(self.s1_rahmen)
        b1 = tk.Button(self.s1_rahmen, text="Enter", command=self.password_correct)
        b2 = tk.Button(self.s1_rahmen, text="Continue without password", command=ohne.show)

        b1.place(x=655,y =270)
        b2.place(x=597,y= 300)
        self.e1.place(x=613, y=245)

    def show(self):
        self.s1_rahmen.lift()

    def password_correct(self):
        e = self.e1.get()
        if e == 'Test':
            geheim = Library(fenster, self.container)
            geheim.show()
        else:
            pass
class Library():
    def __init__(self, fenster, container):
        self.s2_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s2_rahmen, text='Welcome to your library, Neo2460.\nWhich entry do you want to edit?')
        label.place(x=600, y=10)
        self.s2_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s2_rahmen.lift

class Intruder_Library():
    def __init__(self, fenster, container):
        self.s3_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s3_rahmen, text='Welcome to the library. \nGo on, have a look around, I dare you!')
        label.place(x=585, y=2)
        self.s3_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s3_rahmen.lift()

#defs:
def haupt_ansicht(fenster):
    buttonframe = tk.Frame(fenster)
    container = tk.Frame(fenster)
    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)

    h = Homescreen(fenster, container)
    b1 = tk.Button(buttonframe, text = 'Homescreen', command=h.show)
    b1.pack(side='left')
    h.show()


fenster = tk.Tk()
fenster.title('The Mastermind')
haupt_ansicht(fenster)
fenster.geometry("1350x800")


fenster.mainloop()
