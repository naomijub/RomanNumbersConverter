#!/usr/bin/python
'''
Created on 06/11/2016

@author: JAT
'''
import tkinter as tki

root = tki.Tk()
varLabel = tki.StringVar()
label = tki.Label(root, textvariable=varLabel, bg="#fff", width=20, anchor="e")
varLabel.set(" ")
label.grid(row=0, column=0, columnspan=6)

varRadio = tki.IntVar()
tki.Radiobutton(root, text="Roman", variable=varRadio, value=1).grid(row=1, column=0, columnspan=3)
tki.Radiobutton(root, text="Arabic", variable=varRadio, value=2).grid(row=1, column=3, columnspan=3)

root.mainloop()  