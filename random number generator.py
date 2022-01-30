# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 11:43:41 2022

@author: ramak
"""

import random
from tkinter import *
root=Tk()
root.title("Sorting List")
root.geometry("500x400")
root.configure(bg="pink")

list=["bottle", "glass", "desk", "lamp", "book", "jacket", "laptop", "binder", "box", "pencil"]
label_1 = Label(root)
label_2= Label(root)
label_1["text"]= "Listed Items: "+ str(list)

def randomno():
    randomnumber = random.randint(1, 10)
    label_2["text"]= "Put item no. " + str(randomnumber) + " in the bag"
   
btn=Button(root, text="Generate Random List", command=randomno, bg="purple", fg="white")

btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label_1.place(relx=0.5, rely=0.4, anchor=CENTER)
label_2.place(relx=0.5, rely=0.6, anchor=CENTER)

    



root.mainloop()