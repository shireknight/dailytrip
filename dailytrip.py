import os, sys
from Tkinter import *
# from quitter import Quitter

class App(Frame):

    API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    API_KEY = 'AIzaSyCbdRN1-Cn8mo5TZ_-S_diukU3Qh6cdf9E'

    def __init__(self, master=None):
        Frame.__init__(self, master)

        origLbl = Label(self, text='Origin:')
        origLbl.pack()
        origPut = Entry(self, textvariable=orig)
        origPut.pack()

        destLbl = Label(self, text='Destination:')
        destLbl.pack()
        destPut = Entry(self, textvariable=dest)
        destPut.pack()

        qBtn = Button(self, text="Quit", command=self.quit)
        #qBtn.grid(row=2, column=2)
        qBtn.pack()

    def getTripTime(self, start, end):
        print start + " " + end



    def quit(self):
        sys.exit()





if __name__ == "__main__":
    top = Tk()
    app = App(top)
    top.mainloop()
