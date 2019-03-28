import turtle
import math
from bfs import *

f = open("map31.txt", 'r')
firstline = f.readline()
matrix = f.readlines()
info = firstline.split()

#######################################
N = int(info[0])
M = int(info[1])
area_1_block = 24
width = N*area_1_block
height = M*area_1_block

if (N%2 == 0):
    mostRight = width/2
else:
    mostRight = (width - area_1_block)/2

if (M%2 == 0):
    mostTop = height/2
else:
    mostTop = (height - area_1_block)/2 

mostLeft = -mostRight
mostBottom = -mostTop
#######################################
graph = []
for line in matrix:
    y = [int(value) for value in line.split()]
    graph.append(y)
#######################################
f.close()

wn = turtle.Screen() 

wn.bgcolor("black") 
wn.title("The Maze Game")
wn.setup(700, 700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Food(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.reward = 9
        self.goto(x, y)

    def destroy(self):
        self.goto(5000, 5000)
        self.hideturtle()    

class Monster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)   

class Pacman(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(1)
        self.point = 0

    def go_up(self):
        move_to_x = pacman.xcor()
        move_to_y = pacman.ycor() + area_1_block

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = pacman.xcor()
        move_to_y = pacman.ycor() - area_1_block

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)        

    def go_left(self):
        move_to_x = pacman.xcor() - area_1_block
        move_to_y = pacman.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)        

    def go_right(self):
        move_to_x = pacman.xcor() + area_1_block
        move_to_y = pacman.ycor() 

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        if self.xcor() == other.xcor() and self.ycor() == other.ycor():
            return True
        else:
            return False

    def destroy(self):
        self.goto(5000, 5000)
        self.hideturtle()  

levels = [""]
walls = []
foodList = []
monsterList = []  
level_1 = graph
levels.append(level_1)


def setup_maze(level):
        for x in range (len(level)):
            for y in range (len(level[x])):
                character = level[x][y]
                screen_x = mostLeft + (y *area_1_block)
                screen_y = mostTop -(x *area_1_block) 

                if character == 1:
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x, screen_y))
                
                if character == 5:
                    pacman.goto(screen_x, screen_y)
                    x_pacman = x
                    y_pacman = y

                if character == 2:
                    foodList.append(Food(screen_x, screen_y))
                    x_food = x
                    y_food = y 
                if character == 3:
                    monsterList.append(Monster(screen_x, screen_y))
                    x_food = x
                    y_food = y 

pen = Pen()
pacman = Pacman()

x_pacman = 0
y_pacman = 0
x_food = 0
y_food = 0
for x in range (len(graph)):
    for y in range (len(graph[x])):
        character = graph[x][y]
        if character == 5:
            x_pacman = x
            y_pacman = y

        if character == 2:
            x_food = x
            y_food = y 

print(x_pacman, y_pacman, x_food, y_food)

##########        LEVEL 1         ############
setup_maze(graph)

visited = initvisited(graph)
before = initbefore(graph)
final = (x_pacman, y_pacman)
final = []
DFSforLevel3(graph, visited, before, x_pacman, y_pacman, final)
finalPoint = final[0]
solution = pathLevel3(before, x_pacman, y_pacman, finalPoint)

print(solution)

def realCoordinare(t):
    result = []
    for i in range (0, len(t)):
        temp = t[i]
        xT = mostLeft + temp[1]*area_1_block
        yT = mostTop - temp[0]*area_1_block
        pair = (xT, yT)
        result.append(pair) 
    return result

path = realCoordinare(solution)

def eatFood():
    for f in foodList:
        if pacman.is_collision(f):
            pacman.point += f.reward
            print("Player Point: ", pacman.point)
            f.destroy()
            foodList.remove(f)

while True:
    if(len(path) > 0):
        for i in range (0, len(path)):
            current = (pacman.xcor(), pacman.ycor())
            temp = path[i]
            xT = temp[0] - current[0]
            yT = temp[1] - current[1]
            if (xT == 0 and yT == area_1_block):
                pacman.go_up()
                pacman.point -= 1
                eatFood()
            elif (xT == 0 and yT == -area_1_block):
                pacman.go_down()
                pacman.point -= 1
                eatFood()
            elif (xT == area_1_block and yT == 0):
                pacman.go_right()
                pacman.point -= 1
                eatFood()
            elif (xT == -area_1_block and yT == 0):
                pacman.go_left()
                pacman.point -= 1  
                eatFood()
    else:
        print("Player Point: ", pacman.point)
        print("Pacman Don't Want To Move!!!")
        break

    wn.tracer(0)
    wn.update()
