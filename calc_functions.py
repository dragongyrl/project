#calculator functions
#Author: Amelia Krouse

def inside(clicked, button, valX1,valY1,valX2,valY2):
    if clicked.getX() > valX1 and clicked.getX() < valX2:
        if clicked.getY() > valY1 and clicked.getY() < valY2:
            return True

def buttonMaker(valX1,valY1,valX2,valY2,color,num,win):
    num1 = Point(valX1,valY1)
    num2 = Point(valX2,valY2)
    buttonNum = Rectangle(num1, num2)
    buttonNum.setFill(color)
    text = Text(Point(valX1+30,valY1+30),num)
    buttonNum.draw(win)
    text.draw(win)

def screenClean(win):
    scr1 = Point(60, 60)
    scr2 = Point(380, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

def addy(x,y):
    return float(x) + float(y)

def subby(x,y):
    return float(x) - float(y)

def multy(x,y):
    return float(x) * float(y)

def divy(x,y):
    return float(x) / float(y)

def percy(x,y):
    return float(x) * float(y)/100.0

def sqrty(x):
    return float(x) **(1/2)

def squy(x):
    return float(x) **2

def denomy(x):
    return 1/float(x)

def memcleary():
    return ''

def memaddy(mem,dis):
    return str(float(mem)+float(dis))

def memsubby(mem,dis):
    return str(float(mem)-float(dis))

def memrecy(mem,win):
    text = Text(Point(360-len(mem) * 10, 90), mem)
    text.draw(win)
    return ''

def memsubsty(dis,win):
    text = Text(Point(360-len(dis) * 10, 90), dis)
    text.draw(win)
    return dis
