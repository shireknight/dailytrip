'''
    Title: DailyTrip
    Author: Ben Valentine
    Copyright: 2016, Ben Valentine
    Version 1.0

    - Completed basic functionality and ugly UI.
    - Next steps including saving and retrieving trips
    from json file + fixing button alignment.
'''


import os, sys
import urllib, urllib2
import json
from Tkinter import *

class App(Frame):

    # Distance Matrix URL
    API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    # this has to go somewhere else, its not safe
    API_KEY = 'AIzaSyCbdRN1-Cn8mo5TZ_-S_diukU3Qh6cdf9E'

    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=500)
        self.grid(row=2, column=4)

        # origin widgets
        orig_lbl = Label(self, text="Origin:").grid(row=0, sticky=W)
        self.orig_val = Entry(self, width=50)
        self.orig_val.grid(row=0, column=1)
        # insert most recent from json file
        # self.orig_val.insert(0, address1)

        #destination widgets
        dest_lbl = Label(self, text="Destination:").grid(row=1, sticky=W)
        self.dest_val = Entry(self, width=50)
        self.dest_val.grid(row=1, column=1)
        # insert most recent from json file
        # self.dest_val.insert(0, address2)

        self.results = Text(self, height=5)
        self.results.grid(row=0, column=2, columnspan=2, rowspan=2)

        # go button calls get getTripTime
        resetBtn = Button(self, text="Reset", command=self.resetVals).grid(row=2, sticky=W)
        goBtn = Button(self, text="Go", command=self.getTripTime).grid(row=2, column=2, sticky=E)


    def getTripTime(self):
        # grab addresses from inputs
        addresses = {
            'origins' : self.orig_val.get(),
            'destinations' : self.dest_val.get()
        }
        # append addresses to url
        url = self.API_URL
        url += '&' + urllib.urlencode(addresses)
        url += '&key=' + self.API_KEY

        try: # calling Google Distance Matrix API
            response = urllib2.urlopen(url)
            contents = response.read()
            decoded = json.loads(contents)

            # dig deep for data
            dist = decoded['rows'][0]['elements'][0]['distance']['text']
            dur = decoded['rows'][0]['elements'][0]['duration']['text']

            self.results.insert(END, 'Distance: ' + dur + '\r\n')
            self.results.insert(END, 'Duration: ' + dist + '\r\n')
        except IOError as e: # error on the command line for now
            # eventually we'll print this for the user in the textbox
            print e.strerror

    # clears text boxes
    def resetVals(self):
        self.orig_val.delete(0, END)
        self.dest_val.delete(0, END)

if __name__ == "__main__":
    App().mainloop()
