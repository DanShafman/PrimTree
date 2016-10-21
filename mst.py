import turtle
import time
import random
import math

t = turtle
r = random

numPoints = 5
minConnections = 2
t.speed(0)
t.pensize(2)
maxVertices = (numPoints * (numPoints - 1))/2

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

def makePoint(num):
	t.penup()
	t.left(270)	
	t.forward(6.39245)
	t.left(90)
	t.pendown()
	t.circle(6.39245)
	t.left(90)
	t.penup()
	t.forward(6.39245)
	t.left(270)
	print("Point position: ", alphaDict[num], t.pos())
	pointCords.append(t.pos())
	t.left(135)
	t.forward(20)
	t.write(alphaDict[num], font=("Arial", 10, "normal"))
	t.forward(-20)
	t.left(225)
	t.left(angRange())

def findDist(a, b):
	x = 0
	y = 1
	return math.sqrt( (b[x]-a[x])**2 + (b[y]-a[y])**2 )

def findAdjacencies(point):
	final = []
	for dot in pointCords:
		if dot != point:
			x = int("{:.0f}".format(findDist(point, dot)))
			if x in lineDists:
				final.append(dot)
	return final	

for i in range(0, numPoints-1):
	fwNum = randInRange(50, 200)
	lineDists.append(fwNum)
	makePoint(i)
	t.pendown()
	t.forward(fwNum)

makePoint(numPoints-1)
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
			#print(findAdjacencies(point))
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
		t.speed(4)
		t.showturtle()
		t.left(1080)
	print("All adjacencies: ", adjs)

findMST()	

#print(lineDists)
t.hideturtle()
t.exitonclick()
