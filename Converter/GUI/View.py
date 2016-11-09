#!/usr/bin/python
'''
Created on 06/11/2016

@author: JAT
'''
import tkinter as tki

class view(tki.Tk):
    def __init__(self, parent):
        tki.Tk.__init__(self, parent)
        self.parent = parent
        self.selection = ""
        self.arg1 = ""
        self.arg2 = ""
        self.operatorSymbol = ""
        self.title("RomanArabicCalculator")
        self.run()

    def sel(self, arg):
        self.selection = self.varLabel.get() + arg
        sel = self.selection
        self.varLabel.set(sel)

    def typeSel(self):
        selection = self.varRadio.get()
        print(selection)
        if(selection == 1): #Roman
            self.changeButtonStates('normal','disable')
        elif (selection == 2): #Arabic
            self.changeButtonStates('disable', 'normal')
        else:
            self.changeButtonStates('disable','disable')
            
    def changeButtonStates(self, roman, arabic):
        self.B0['state'] = arabic
        self.B1['state'] = arabic
        self.B2['state'] = arabic
        self.B3['state'] = arabic
        self.B4['state'] = arabic
        self.B5['state'] = arabic
        self.B6['state'] = arabic
        self.B7['state'] = arabic
        self.B8['state'] = arabic
        self.B9['state'] = arabic
        self.BI['state'] = roman
        self.BV['state'] = roman
        self.BX['state'] = roman
        self.BL['state'] = roman
        self.BC['state'] = roman
        self.BD['state'] = roman
        self.BM['state'] = roman

    def run(self):
        self.runLabel()
        self.runRadio()
        self.runButton()


    def runLabel(self):
        #label 1st row
        self.varLabel = tki.StringVar()
        self.label = tki.Label(self, textvariable=self.varLabel, bg="#fff", width=20, anchor="e")
        self.label.grid(row=0, column=0, columnspan=6)

    def runRadio(self):
        #radio buttons 2nd row
        self.varRadio = tki.IntVar()
        self.varRadio.set(1)
        Roman = tki.Radiobutton(self, text="Roman", variable=self.varRadio, value=1, command=lambda : self.typeSel())
        Roman.grid(row=1, column=0, columnspan=3)
        Arabic = tki.Radiobutton(self, text="Arabic", variable=self.varRadio, value=2, command=lambda : self.typeSel())
        Arabic.grid(row=1, column=3, columnspan=3)

    def runButton(self):
        #Buttons
        #3rd row
        self.B0 = tki.Button(self, text="0", command= lambda: self.sel('0'))
        self.B0.grid(row=2, column=0)
        self.B1 = tki.Button(self, text="1", command= lambda: self.sel('1'))
        self.B1.grid(row=2, column=1)
        self.B2 = tki.Button(self, text="2", command= lambda: self.sel('2'))
        self.B2.grid(row=2, column=2)
        self.B3 = tki.Button(self, text="3", command= lambda: self.sel('3'))
        self.B3.grid(row=2, column=3)
        self.B4 = tki.Button(self, text="4", command= lambda: self.sel('4'))
        self.B4.grid(row=2, column=4)
        self.B5 = tki.Button(self, text="5", command= lambda: self.sel('5'))
        self.B5.grid(row=2, column=5)
        #4th row
        self.B6 = tki.Button(self, text="6", command= lambda: self.sel('6'))
        self.B6.grid(row=3, column=0)
        self.B7 = tki.Button(self, text="7", command= lambda: self.sel('7'))
        self.B7.grid(row=3, column=1)
        self.B8 = tki.Button(self, text="8", command= lambda: self.sel('8'))
        self.B8.grid(row=3, column=2)
        self.B9 = tki.Button(self, text="9", command= lambda: self.sel('9'))
        self.B9.grid(row=3, column=3)
        self.BI = tki.Button(self, text="I", command= lambda: self.sel('I'))
        self.BI.grid(row=3, column=4)
        self.BV = tki.Button(self, text="V", command= lambda: self.sel('V'))
        self.BV.grid(row=3, column=5)
        #5th row
        self.BX = tki.Button(self, text="X", command= lambda: self.sel('X'))
        self.BX.grid(row=4, column=0)
        self.BL = tki.Button(self, text="L", command= lambda: self.sel('L'))
        self.BL.grid(row=4, column=1)
        self.BC = tki.Button(self, text="C", command= lambda: self.sel('C'))
        self.BC.grid(row=4, column=2)
        self.BD = tki.Button(self, text="D", command= lambda: self.sel('D'))
        self.BD.grid(row=4, column=3)
        self.BM = tki.Button(self, text="M", command= lambda: self.sel('M'))
        self.BM.grid(row=4, column=4)

if __name__ == "__main__":
    app = view(None)
    app.mainloop()
