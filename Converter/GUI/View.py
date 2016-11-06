#!/usr/bin/python
'''
Created on 06/11/2016

@author: JAT
'''
import tkinter as tki

root = tki.Tk()
var = tki.StringVar()
label = tki.Label(root, textvariable=var, bg="#fff", width=20, anchor="e")
var.set("Hello World")

label.pack()
root.mainloop()