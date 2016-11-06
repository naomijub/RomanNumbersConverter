#!/usr/bin/python
'''
Created on 06/11/2016

@author: JAT
'''
import tkinter as tki


#root = tki.Tk()
#===============================================================================
# varLabel = tki.StringVar()
# label = tki.Label(root, textvariable=varLabel, bg="#fff", width=20, anchor="e")
# varLabel.set(" ")
# label.grid(row=0, column=0, columnspan=6)
# 
# varRadio = tki.IntVar()
# tki.Radiobutton(root, text="Roman", variable=varRadio, value=1).grid(row=1, column=0, columnspan=3, command=sel)
# tki.Radiobutton(root, text="Arabic", variable=varRadio, value=2).grid(row=1, column=3, columnspan=3, command=sel)
#===============================================================================


class view(tki.Tk):
    def __init__(self, parent):
        tki.Tk.__init__(self, parent)
        self.parent = parent
        self.title("RomanArabicCalculator")
        self.run()
        
    def sel(self):
        selection = str(self.varRadio.get())
        self.varLabel.set(selection)
    
    def run(self):
        self.varLabel = tki.StringVar()
        self.label = tki.Label(self, textvariable=self.varLabel, bg="#fff", width=20, anchor="e")
        self.varLabel.set(" ")
        self.label.grid(row=0, column=0, columnspan=6)

        self.varRadio = tki.IntVar()
        self.varRadio.set(1)
        Roman = tki.Radiobutton(self, text="Roman", variable=self.varRadio, value=1, command=self.sel)
        Roman.grid(row=1, column=0, columnspan=3)
        Arabic = tki.Radiobutton(self, text="Arabic", variable=self.varRadio, value=2, command=self.sel)
        Arabic.grid(row=1, column=3, columnspan=3)
    
if __name__ == "__main__":    
    app = view(None)
    app.mainloop()