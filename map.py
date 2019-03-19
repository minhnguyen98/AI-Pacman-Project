import turtle

N = 25
M = 25
width = N*24
height = M*24

if (N%2 == 0):
    mostRight = width/2
else:
    mostRight = (width - 24)/2

if (M%2 == 0):
    mostTop = height/2
else:
    mostTop = (height - 24)/2 

mostLeft = -mostRight
mostBottom = -mostTop
  
##################################################
wn = turtle.Screen() 
 
wn.bgcolor("black") 
wn.title("The Maze Game")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
 
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(1)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)        

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)        

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

levels = [""]  
 
level_1 = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1],
[1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1],
[1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1],
[1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1],
[1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1],
[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,0,0,0,0,0,0,0,5,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
 
levels.append(level_1)
 
def setup_maze(level):
        for y in range (len(level)):
            for x in range (len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x *24)
                screen_y = 288 -(y *24) 

                if character == 1:
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    # Add wall:
                    walls.append((screen_x, screen_y))
                
                if character == 5:
                    player.goto(screen_x, screen_y)

pen = Pen()
player = Player()
# wall = Wall()

walls = []

setup_maze(levels[1])

testA = [(10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13)]

def realCoordinare(testA):
    result = []
    for i in range (0, len(testA)):
        temp = testA[i]
        xT = mostLeft + temp[0]*24
        yT = mostTop - temp[1]*24
        pair = (xT, yT)
        result.append(pair) 
    return result

path = realCoordinare(testA)
# current = (player.xcor(), player.ycor())

for i in range (0, len(path)):
    current = (player.xcor(), player.ycor())
    temp = path[i]
    xT = temp[0] - current[0]
    yT = temp[1] - current[1]
    if (xT == 0 and yT == 24):
        player.go_up()
    elif (xT == 0 and yT == -24):
        player.go_down()
    elif (xT == 24 and yT == 0):
        player.go_right()
    elif (xT == -24 and yT == 0):
        player.go_left()  

wn.tracer(0)

while True:
    wn.update()
