# snake game
#step up the screen

#turtle is pre installed and virtual canvas
import turtle
import time
import random
delay = 0.2
# create  a variable

score = 0
high_score = 0


# in the beginnning create screen
#turtle.Screen - make screen object

wn = turtle.Screen()
wn.title("snake game:")
wn.bgcolor("blue")
wn.setup(width=600,height=600)
wn.tracer(0) #turns off the screen updates

# step 1:with turtle in built function we create head 
#snake head
head =turtle.Turtle() #Turtle is assgin to head(object) to use turtle feature like moving 
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0) #x and y -coordinate asgin 0 at inital for movement
head.direction = "stop"

# step 4 :snake food 

food =turtle.Turtle() #Turtle is assgin to head(object) to use turtle feature like moving 
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) #x and y -coordinate asgin 0 at inital for movement
# creating segment list
segment =[]
# step 8: pen
pen=turtle.Turtle() #Turtle is assgin to pen(object) to use turtle feature like moving 
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0,0)
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0 high Score : 0 \n Use Arrow key to Move",align ="center",font = ("Courier",24,"normal"))
#step 3: creating functions to assign keyboard to move head
def go_up():
    if head.direction != "down": # step 7: now if will stop going in opposite direction 
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

#step 2:move function to assign direction to head

def move():
    if head.direction == "up":
        y = head.ycor()  #ycor is y co-ordinate
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()  #ycor is y co-ordinate
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()  #xcor is x co-ordinate
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()  #xcor is x co-ordinate
        head.setx(x + 20)

        
# keyborad bindings - connect keyboard to function

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")

# wn.onkeypress(go_up,"w")
# wn.onkeypress(go_right,"d")
# wn.onkeypress(go_down,"x")
# wn.onkeypress(go_left,"a")
        


while True:
    wn.update()
    # check for collision of head with border
    if head.xcor()>290 or  head.xcor()< -290 or  head.ycor()>290 or  head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
        # as we cannot delete the segment in turtle we just place it outside the screen
        for j in segment:
            j.goto(1000,1000)
        # clear the segment 
        segment.clear()


        # after collision we are resetting the score
        score = 0
        delay = 0.2
        
        pen.clear()
        pen.write("Score : {} high Score : {} ".format(score,high_score), align = "center",font = ("Courier",24,"normal"))
        
        
        
    # now we use if to move our food at random  position when snake touches it for that import random
    if head.distance(food) < 20:
        x = random.randrange(-280,280)
        y = random.randrange(-280,280)
        food.goto(x,y) # goto will move food
        #as now head is touching food we have to increment snake size by adding segment to it
        # segment created in if reason : as 1st snake should touch the food
        new_segment=turtle.Turtle() #Turtle is assgin to head(object) to use turtle feature like moving 
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
        # increase
        delay -= 0.001

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} high Score : {} ".format(score,high_score), align = "center",font = ("Courier",24,"normal"))
        
    # move the sigment in the reverse order first
    for i in range(len(segment)-1,0,-1): # i is index (10,9,8,7,6....)
        x=segment[i - 1].xcor()
        y=segment[i - 1].ycor()
        segment[i].goto(x,y)
    #move segment[0] to where the head is 
    if len(segment) >0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
    


        



#main game loop
#we use while to run loop until condition is true 


        
    move()
    # STEP 6 : CHECK FOR HEAD COLLISION WITH THE BODY SEGMENTS
    for j in segment:
        if j.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segment
            for j in segment:
                j.goto(1000,1000)
            segment.clear()
            score = 0
            delay = 0.2
            pen.clear()
            pen.write("Score : {} high Score :{}".format(score,high_score),align ="center",font=("Courier",24,"normal"))
            
                
    time.sleep(delay)
    






wn.mainloop()

