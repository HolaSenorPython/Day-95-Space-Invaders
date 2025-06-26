import turtle as t
import time
MOVE_D = 20
LIGHT_PURPLE = '#B13BFF' # define light purple here to, cant import from main then import this to main lol
FULL_SPACESHIP_POS = [(-20, -310), (0, -310), (20, -310), (0, -290)] # Define the positions for all the turtles that make up the ship
PELLET_D = 30

class SpaceShip:
    # When a spaceship obj is initialized...
    def __init__(self):
        self.FULL_SPACESHIP = []
        self.make_spaceship() # Do this method on init
        self.ship_edge = self.FULL_SPACESHIP[0] # Define edge of spaceship for movement
        self.move_d = MOVE_D # Save as attribute that we can adjust later
        self.pellet_holder = [] # List to hold our pellet object, so we can delete it and save memory when off-screen
        self.pellet_d = PELLET_D # pellet move distance for later
        self.pellet = None

    def make_spaceship(self):
        for pos in FULL_SPACESHIP_POS:
            self.add_spaceship_part(pos)

    def add_spaceship_part(self, position):
        # this is done for all the starting pos in that list, essentially filling up our desired shape :D
        spaceship_part = t.Turtle()
        spaceship_part.penup()
        spaceship_part.shape('square')
        spaceship_part.seth(180) # face west
        spaceship_part.color(LIGHT_PURPLE) # Light purp color :D
        spaceship_part.setpos(position)
        self.FULL_SPACESHIP.append(spaceship_part) # add this turtle to the full spaceship

    def left(self):
        if self.ship_edge.xcor() > -380: # If the left edge is at least at x = -379, move left
            for part in self.FULL_SPACESHIP:
                part.goto(part.xcor() - self.move_d, part.ycor()) # Stay same y, decrease in x

    def right(self):
        if self.FULL_SPACESHIP[2].xcor() < 380:
        # If the right edge of the spaceship (turtle at index 2 in the list) is at a xcor less than 380:
            for part in self.FULL_SPACESHIP:
                part.goto(part.xcor() + self.move_d, part.ycor()) # Stay same y, increase in x

    def make_pellet(self):
        if self.pellet is not None: # if there is already a pellet on screen, don't make another one
            return
        self.pellet = t.Turtle()
        self.pellet.penup()
        self.pellet.color('white')
        self.pellet.shape('circle')
        self.pellet.seth(90) # set it facing north
        self.pellet.shapesize(stretch_wid=0.5, stretch_len=0.5) # Set these vals to less than 1, to have a smaller turtle
        # Get the pos of the tip of the spaceship, to know where to shoot pellet from
        position = self.FULL_SPACESHIP[3].pos()
        self.pellet.goto(position[0], position[1] + 10) # Go to the x of the tip, and its y plus 10
        self.pellet_holder.append(self.pellet)
        self.shoot_pellet(p=self.pellet)

    def shoot_pellet(self, p): # Passed in specific pellet so computer remembers it?
        def move(): # Nest in function to use turtle's ontimer method
            if p.ycor() > 390: # If the pellet is now off-screen, delete it and make a new pellet
                p.hideturtle() # Hide before delete
                if p in self.pellet_holder: # Delete only if in list
                    self.pellet_holder.remove(p) # Remove it from the list
                self.pellet = None # Reset the self.pellet value
                return
                # STOP the loop that move calls on itself using the ontimer method using a return statement, therefore
                # ensuring that self.pellet doesn't remain as none (since we did just hide and delete that pellet)
            p.sety(p.ycor() + self.pellet_d)
            t.Screen().ontimer(move, 32) # every 32 milliseconds this function move should be done, so about 30 fps

        move() # Do move when pellet is made lol