import turtle as t
import time
import random as r
import math
import Vertex

numPoints = 7
minConnections = 2
t.speed(0)
t.pensize(2)
maxVertices = (numPoints * (numPoints - 1)) / 2

t.hideturtle()
pointCords = []
lineDists = []
alphaDict = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

def randInRange(start, end):
    i = 0
    while i <= start or i >= end:
        i = int(r.random() * 360)
    return i

def angRange():
    i = 0
    while ((i > 50 and i < 130) or (i > 230 and i < 310)) == False:
        i = int(r.random() * 360)
    return i

def randInArr(arr):
    x = len(arr)
    return arr[randInRange(0, x)]

def findAdjacencies(point):
    final = []
    for dot in pointCords:
        if dot != point:
            x = int("{:.0f}".format(Vertex.findDist(point, dot)))
            if x in lineDists:
                final.append(dot)
    return final

for i in range(0, numPoints - 1):
    fwNum = randInRange(50, 200)
    lineDists.append(fwNum)
    Vertex.makePoint(i)
    t.pendown()
    t.forward(fwNum)

Vertex.makePoint(numPoints - 1)
notConnected = pointCords
tree = []

for i in range(0, randInRange(0, int(maxVertices) - len(pointCords))):
    a = pointCords[randInRange(0, len(pointCords))]
    b = pointCords[randInRange(0, len(pointCords))]
    dist = 0
    actualDist = 0
    while (dist in lineDists) == True or a == b:
        a = pointCords[randInRange(0, len(pointCords))]
        b = pointCords[randInRange(0, len(pointCords))]
        dist = int("{:.0f}".format(findDist(a, b)))
        actualDist = findDist(a, b)

    t.penup()
    t.setpos(a[0], a[1])
    t.pendown()
    t.setpos(b[0], b[1])
    lineDists.append(dist)

if 0 in lineDists:
    lineDists.remove(0)

def getPointForDist(point, dist):
    for dot in pointCords:
        if findDist(point, dot) == dist:
            return dot

def findMST():
    t.pensize(3)
    t.hideturtle()
    t.pencolor("red")
    rand = randInArr(pointCords)
    tree.append(rand)
    notConnected.remove(rand)
    print("Starting vertex is: ", tree)
    adjs = {}
    while len(notConnected) != 0:
        t.speed(0)
        for point in tree:
            # print(findAdjacencies(point))
            for dot in findAdjacencies(point):
                adjs[findDist(point, dot)] = point

        minAdj = min(adjs, key=int)
        minDot = adjs[minAdj]
        nextDot = getPointForDist(minDot, minAdj)
        t.penup()
        t.setpos(minDot[0], minDot[1])
        t.pendown()
        t.setpos(nextDot[0], nextDot[1])
        adjs = {}
        tree.append(nextDot)
        notConnected.remove(nextDot)
        wait = input("Press any button")
    print("All adjacencies: ", adjs)

findMST()

# print(lineDists)
t.hideturtle()
t.exitonclick()
