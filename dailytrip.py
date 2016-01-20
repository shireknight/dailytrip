import os, sys
from Tkinter import *

class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()
        f2 = Frame(master, width=200, height=100)
        f2.grid(row=0, column=1)
        newTripBtn = Button(self.frame, text="New Trip", command=self.createNewTrip)
        quitBtn = Button(self.frame, text="Quit", command=self.quit)
        newTripBtn.pack(side=LEFT)
        quitBtn.pack(side=RIGHT)

    def createNewTrip(self):
        Trip()
        quit()

    def quit(self):
        sys.exit()


class Trip:

    def __init__(self):
        print 'new trip instance'


if __name__ == "__main__":
    top = Tk()
    app = App(top)
    top.mainloop()
