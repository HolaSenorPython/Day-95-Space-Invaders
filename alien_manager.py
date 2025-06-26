import turtle as t
import random # for randomized pellet shooting
STARTING_X = -380 # Starting X to start making aliens from
X_INCREMENT = 40 # Increment to increase by in X
Y_COORDS_PER_ROW = [280, 250, 220, 190, 160, 130]
COLORS = ["#FF0000", # Red
          "#FF7F00", # Orange
          "#FFFF00", # Yellow
          "#00FF00", # Green
          "#00FFFF", # Cyan / aqua blue
          "#8B00FF"  # Violet
          ] # colors of the rainbow

# This will handle the color for the alien's pellet
def color_check(alien, alien_list):
    if 0 <= alien_list.index(alien) <= 5: # If it's within the first 6 aliens its red
        return '#FF0000'
    elif 6 <= alien_list.index(alien) <= 11:
        return '#FF7F00'
    elif 12 <= alien_list.index(alien) <= 17:
        return '#FFFF00'
    elif 18 <= alien_list.index(alien) <= 23:
        return '#00FF00'
    elif 24 <= alien_list.index(alien) <= 29:
        return '#00FFFF'
    elif 30 <= alien_list.index(alien) < 36: # Doesn't include 36, should stop at 35 which i hope is all the colors/turtles
        return '#8B00FF'


class AlienManager:
    def __init__(self):
        self.all_aliens = []
        self.start_x = STARTING_X
        self.y_coords = Y_COORDS_PER_ROW
        self.colors = COLORS
        self.move_d = 5 # move distance for aliens
        self.direction = 1 # Start positive, negative means left pos is right
        self.pellets = [] # List to hold multiple pellets, idea from chatgpt to improve
        self.pellet_speed = 5 # Speed of pellet

    def spawn_aliens(self):
        designated_y_coord = 0
        for color in self.colors:
            for num in range(6): # Do this 6 times

                alien = t.Turtle()
                alien.penup()
                alien.color(color)
                alien.shape('triangle')
                alien.seth(270)
                alien.setpos(self.start_x, self.y_coords[designated_y_coord])
                self.all_aliens.append(alien)
                self.start_x += X_INCREMENT # Increase the x increment in nested loop so turtles are made along a row
            designated_y_coord += 1 # Increase designated y coord after one colored row is done
            self.start_x = STARTING_X # reset start X

    def move(self):
        hit_wall = False
        for alien in self.all_aliens:
            # Increase the x and multiply by direction. This is important later
            # Pemdas. Multiplication comes first, so that move d will change depending on if hit wall is true
            alien.setx(alien.xcor() + self.move_d * self.direction)

        # Check if a wall was hit
        for alien in self.all_aliens:
            if alien.xcor() > 380:
                hit_wall = True
            elif alien.xcor() < -380:
                hit_wall = True

        # IF any walls were hit, change the direction, making that move distance neg
        if hit_wall:
            self.direction *= -1

    def make_pellet(self):
        if not self.all_aliens: # If there are no more aliens
            return # Don't make pellets lol
        shooter = random.choice(self.all_aliens)
        color = color_check(shooter, self.all_aliens)
        p = t.Turtle('circle') # our mighty pellet
        p.penup()
        p.shapesize(stretch_wid=0.5, stretch_len=0.5) # 10 by 10 px
        p.color(color)
        p.goto(shooter.xcor(), shooter.ycor() - 10) # should spawn a little in front of alien/below
        self.pellets.append(p) # Append this pellet to the list

    # Once again, ChatGPT helped me clean this up, and im learning
    def move_pellets(self):
        """Call once per frame in the main loop.""" # 60 times 🤠
        for pellet in self.pellets[:]: # apparently iterating over a copy of a list when removing stuff is safer?
            pellet.sety(pellet.ycor() - self.pellet_speed) # Move that pellet downwars by decreasing y
            if pellet.ycor() <= -390: # If its off-screen...
                pellet.hideturtle() # Hide it
                self.pellets.remove(pellet) # Kill that pellet

    # removes the alien passed in from the list, effectively removing it from python's memory
    def kill_alien(self, alien):
        self.all_aliens.remove(alien)
