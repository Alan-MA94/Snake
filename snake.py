from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Walls(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -340)
        self.pendown()
        self.goto(0, -340)
        self.goto(450, -340)
        self.goto(450, 340)
        self.goto(-450, 340)
        self.goto(-450, -340)
        self.goto(0, -340)

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(2300,2300)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    

