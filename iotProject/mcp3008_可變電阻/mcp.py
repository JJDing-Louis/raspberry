#!/usr/bin/python3.7
'''
MCP3008 ,可變電阻
'''

from gpiozero import MCP3008
from tkinter import *

channel0 = MCP3008(0)

class App():
    def __init__(self,win):
        mainFrame = Frame(win,borderwidth=2,relief=GROOVE)


if __name__ == '__main__':
    window = Tk()
    window.title("MCP3008_可變電阻")
    window.option_add("*font",('verdana',18,'bold'))
    window.option_add('*background','#333333')
    window.option_add('*foreground','#ffffff')
    app = App(window)
    window.mainloop()
