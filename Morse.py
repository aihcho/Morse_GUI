from tkinter import *
import tkinter.font

import time

from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## DEF ##
red = LED(26)
UNIT = 0.15

## GUI ##
win = Tk()
win.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12)

## FUNCTIONS ##
def dot():
    red.on()
    time.sleep(UNIT)
    red.off()
    
def dash():
    red.on()
    time.sleep(UNIT * 3)
    red.off()

def space_sl():
    time.sleep(UNIT)

def space_l():
    time.sleep(UNIT * 3)
    
def space_w():
    time.sleep(UNIT * 7)

def close():
    RPi.GPIO.cleanup()
    win.destroy()

def a():
    dot()
    space_sl()
    dash()

def b():
    dash()
    space_sl()
    dot()
    space_sl()
    dot()
    space_sl()
    dot()

def c():
    dash()
    space_sl()
    dot()
    space_sl()
    dash()
    space_sl()
    dot()

def d():
    dash()
    space_sl()
    dot()
    space_sl()
    dot()

def e():
    dot()

def f():
    dot()
    space_sl()
    dot()
    space_sl()
    dash()
    space_sl()
    dot()

def g():
    dash()
    space_sl()
    dash()
    space_sl()
    dot()

def h():
    dot()
    space_sl()
    dot()
    space_sl()
    dot()
    space_sl()
    dot()

def i():
    dot()
    space_sl()
    dot()

def j():
    dot()
    space_sl()
    dash()
    space_sl()
    dash()
    space_sl()
    dash()

def k():
    dash()
    space_sl()
    dot()
    space_sl()
    dash()

def l():
    dot()
    space_sl()
    dash()
    space_sl()
    dot()
    space_sl()
    dot()

def m():
    dash()
    space_sl()
    dash()

def n():
    dash()
    space_sl()
    dot()

def o():
    dash()
    space_sl()
    dash()
    space_sl()
    dash()

def p():
    dot()
    space_sl()
    dash()
    space_sl()
    dash()
    space_sl()
    dot()

def q():
    dash()
    space_sl()
    dash()
    space_sl()
    dot()
    space_sl()
    dash()

def r():
    dot()
    space_sl()
    dash()
    space_sl()
    dot()

def s():
    dot()
    space_sl()
    dot()
    space_sl()
    dot()

def t():
    dash()

def u():
    dot()
    space_sl()
    dot()
    space_sl()
    dash()

def v():
    dot()
    space_sl()
    dot()
    space_sl()
    dot()
    space_sl()
    dash()

def w():
    dot()
    space_sl()
    dash()
    space_sl()
    dash()

def x():
    dash()
    space_sl()
    dot()
    space_sl()
    dot()
    space_sl()
    dash()
    
def y():
    dash()
    space_sl()
    dot()
    space_sl()
    dash()
    space_sl()
    dash()

def z():
    dash()
    space_sl()
    dash()
    space_sl()
    dot()
    space_sl()
    dot()

def convert(input):
    for letter in input:
        if letter == ' ':
            space_w()
        elif letter == 'a':
            a()
            space_l()
        elif letter == 'b':
            b()
            space_l()
        elif letter == 'c':
            c()
            space_l()
        elif letter == 'd':
            d()
            space_l()
        elif letter =='e':
            e()
            space_l()
        elif letter == 'f':
            f()
            space_l()
        elif letter == 'g':
            g()
            space_l()
        elif letter == 'h':
            h()
            space_l()
        elif letter == 'i':
            i()
            space_l()
        elif letter == 'j':
            j()
            space_l()
        elif letter == 'k':
            k()
            space_l()
        elif letter == 'l':
            l()
            space_l()
        elif letter == 'm':
            m()
            space_l()
        elif letter == 'n':
            o()
            space_l()
        elif letter == 'p':
            p()
            space_l()
        elif letter == 'q':
            q()
            space_l()
        elif letter == 'r':
            r()
            space_l()
        elif letter == 's':
            s()
            space_l()
        elif letter == 't':
            t()
            space_l()
        elif letter == 'u':
            u()
            space_l()
        elif letter == 'v':
            v()
            space_l()
        elif letter == 'w':
            w()
            space_l()
        elif letter == 'x':
            x()
            space_l()
        elif letter == 'y':
            y()
            space_l()
        elif letter == 'z':
            z()
            space_l()
        else:
            space_w()
            
def input():
    INPUT = inputtxt.get("1.0", "end-1c")
    if len(INPUT) <= 12:
        convert(INPUT)


## WIDGET ##
playButton = Button(win, text = 'Convert to Morse Code', font = myFont, command = input, bg = 'bisque2', height = 1, width = 24)
inputtxt = Text(win, height = 2, width = 25, bg = "white")

inputtxt.grid(row=0, column = 1)
playButton.grid(row=1, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
