# -*- coding: UTF-8 -*-
'''
Created on 2017年8月15日

@author: hasee
'''
from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

#设置GUI
root = Tk()
w = Label(root, text = "Label Title")
w.pack()

# 欢迎信息
# mb.showinfo("title,这是标题", "message")
# guess =dl.askinteger("title", "Enter a number")
# 
# output = "This is a output message "
# mb.showinfo("OutPut: ",output)


# #欢迎消息
mb.showinfo("Welcome", "Welcome to Guess Number Game")
#  
#  
# #处理信息
number = 59
#  
while True:
#让用户输入信息
    guess = dl.askinteger("Number", "What's your guess?")
        
    if guess == number:
        # New block starts here
        output = 'Bingo! you guessed it right, but you do not win any prizes!'
        mb.showinfo("Hint: ", output)
        break
        # New block ends here
    elif guess < number:
        output = 'No, the number is a  higer than that'
        mb.showinfo("Hint: ", output)
    else:
        output = 'No, the number is a  lower than that'
        mb.showinfo("Hint: ", output)
     
print('Done')






