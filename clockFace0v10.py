"""
Project - Clock Face
make a quick painted clock face for tasks

Author : Simon Bird

Aim
    Make a quick painted clock face for tasks.


TS 300 min opening setting turtle
"""

from turtle import TurtleScreen, RawTurtle, TK
from turtle import *
import turtle

import math
import time
import random
import numpy as np


# set speed, however final uses the update function for quick draw

loadWindow = turtle.Screen()

# using one turtle
t=turtle.Turtle()

#speed - 0 is fastest
g_speed=10
turtle.speed(g_speed)
t.speed(g_speed)

def iniz_system():
    return 7;

def void_function():
    ret = 0
    return ret

def makeCircleMain():
    ret = 0
    return ret
    
def moveToOutsidePos( sizeOfDot , dotPlacement ):
    var1=0

def makeNumbers( fontSize , sizeOfDot , dotPlacement ):
    var1=0

def makeNumbers():
    ret = 0
    return ret

def makeHands():
    ret = 0
    return ret

def makeSegment():
    ret = 0
    return ret

def makeMinDots():
    ret = 0
    return ret

def makeHourDots():
    ret = 0
    return ret

def makeFace():

    turtle.ht();    t.ht();
    turtle.tracer(0,0)

    # array starting right at 3 clock then anti clockwise
    stringArray = [ '  3','  2','  1',' 12',' 11',' 10','  9','  8','  7','  6','  5','  4']

    
    dotPlacement = 130
    sizeOfDot = 5
    outsideSpace = 15
    fontSize = 14
    radiusIn = dotPlacement + sizeOfDot + outsideSpace

    posx=( 0 )
    posy=( 0 - ( dotPlacement + sizeOfDot + outsideSpace ) )
#=== main circle
    makeBasicCircle ( ( dotPlacement + sizeOfDot + outsideSpace ) , posx , posy , False )
    t.up()
    
#=== move to center
    t.setx(0)
    t.sety(0)
    
#=== small dots
    dotId = 0
    
    while dotId < 12:

        t.up()
        
        #t.left(90)
        #delay(3000)

        #move to inner
        t.left( dotId * 30 )
        t.forward( dotPlacement )

        #line to horizontal
        t.right( dotId * 30 )

        #draw circle
        t.down()
        t.circle( sizeOfDot )
        t.up()
        #delay(300)

        #move down
        t.right( 90 )
        t.forward( fontSize )

        #center text
        t.right( 90 )
        t.forward( fontSize/2 )
        #write text
        t.write( stringArray[ ( dotId ) ], font=('Areil',8,'bold') )####
        t.left( 180 )
        t.forward( fontSize/2 )
        t.right( 90 )

        #move up
        t.left( 180 )
        t.forward( fontSize )

        t.left( 90 + ( dotId *30 ) )

        #move center
        t.forward( dotPlacement )

        #realighn
        
        t.left( 180 - ( dotId *30 ) )
        dotId+=1
        
    turtle.update()
    
def makeBasicCircle ( radiusIn , posx , posy , fill ):
    t.up()
    t.setx(posx)
    t.sety(posy)
    t.down()
    if fill is True:
        color ( 'black' , 'black' )
    if fill is not True:
        color ( 'black', 'white' )
    begin_fill()
    t.circle(radiusIn,360)
    end_fill()
        
def main_core( s_size , colour ):
    var1=0

def test_bed ():

    var1=0



#==================== BASIC UI =================================#
       
def du ():makeFace();
def dl ():makeFace();
def dr ():print( "Right");
def dd ():print( "Down");
def ax ():  void_function(); 
def ay ():  void_function();
def az ():  void_function();
def n1():   void_function();
def n2():   void_function();
def n3():   void_function();
def kr():   void_function();
def kq():   void_function();
def cc():   void_function();
def cb():   void_function();


def main_core():

    iniz_system()
    
    loadWindow.onkey(du, "Up")
    loadWindow.onkey(dl , "Left")
    loadWindow.onkey(dr , "Right")
    loadWindow.onkey(dd , "Down")

    loadWindow.onkey(ax , "x")
    loadWindow.onkey(ay , "y")
    loadWindow.onkey(az , "z")

    loadWindow.onkey(n1 , "1")
    loadWindow.onkey(n2 , "2")
    loadWindow.onkey(n3 , "3")

    loadWindow.onkey(kr , "r")

    loadWindow.onkey(kq , "q")
    
    loadWindow.onkey(cc, "c")
    loadWindow.onkey(cb, "b")
    loadWindow.listen()
    loadWindow.mainloop()
    void_function()
    test_bed()
  
makeFace()

#========== TURTLE STUFF NEW ENTRANCE ==============#

#if __name__ == "__main__":
 #   makeFace()


