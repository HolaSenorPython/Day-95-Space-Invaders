from turtle import Screen, Turtle # Import turtle class for flashed msgs
from spaceship import SpaceShip
from alien_manager import AlienManager
from base_manager import BaseManager
from scoreboard import ScoreBoard
import time
import random

#-------SCREEN SETUP-------#
DARK_PURPLE = '#090040'
LIGHT_PURPLE = '#B13BFF'
YELLOW = '#FFCC00'
screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255) # Allow a wide range of colors
screen.bgcolor(DARK_PURPLE)
screen.title('Space Invaders')
screen.tracer(0) # Turn off auto screen update, ill do it myself
#------OBJECT INITIALIZATION AND SCREEN RESPONSE-----#
spaceship = SpaceShip()
alien_manager = AlienManager()
base_manager = BaseManager()
scoreboard = ScoreBoard()
screen.listen() # Screen should listen for key presses!
screen.onkeypress(spaceship.left, 'Left') # Do spaceship to left on left key press
screen.onkeypress(spaceship.right, 'Right') # Do spaceship to right on left key press
screen.onkeypress(spaceship.make_pellet, 'space') # Make a pellet (and shoot it) when space is pressed
#--------FLASHING MESSAGES FUNCTIONS-------#
def alien_hit():
    global flashed_messages
    # Will flash alien hit message
    alien_hit_msg = Turtle()
    alien_hit_msg.hideturtle()
    alien_hit_msg.penup()
    alien_hit_msg.color(LIGHT_PURPLE)
    alien_hit_msg.goto(0, -100) # Go to a lil lower than center
    alien_hit_msg.write(arg="Alien hit!\n"
                            "Your score has increased.", font=('Courier', 20, 'bold'), align='center')
    flashed_messages.append(alien_hit_msg)

    # Make the message disappear after a second. have to nest a function to use turtle on timer method.
    # Using on timer instead of sleep in this instance is wayy better. The whole game doesn't freeze for one message!
    def clear_msg():
        alien_hit_msg.clear() # Clear all text
        flashed_messages.remove(alien_hit_msg) # remove turtle from list, killing it from memory

    le_screen = alien_hit_msg.getscreen() # Find the screen this text is on
    le_screen.ontimer(clear_msg, 1000)
    # The screen should clear this alien hit message after 1000 seconds, and does this
    # whenever the outward function is called

def base_hit(score):
    global flashed_messages
    # Will make turtle and flash msg
    base_hit_msg = Turtle()
    base_hit_msg.hideturtle()
    base_hit_msg.penup()
    base_hit_msg.goto(0,-100)
    base_hit_msg.color(YELLOW)
    if score > 0:
        base_hit_msg.write(arg='Base hit!\n'
                           'You lost score!', font=('Courier', 20, 'bold'), align='center')
    else:
        base_hit_msg.write(arg="Base hit!\n"
                               "You didn't lose score\n"
                               "cause you'd be in\nthe negatives. Yikes.", font=('Courier', 20, 'bold'), align='center')
    flashed_messages.append(base_hit_msg)

    def clear_msg():
        base_hit_msg.clear()
        flashed_messages.remove(base_hit_msg)

    le_screen = base_hit_msg.getscreen()
    le_screen.ontimer(clear_msg, 1000)

def spaceship_hit(score):
    global flashed_messages
    ship_hit = Turtle()
    ship_hit.hideturtle()
    ship_hit.penup()
    ship_hit.color(LIGHT_PURPLE)
    ship_hit.goto(0, -100)
    if score > 0:
        ship_hit.write(arg='Ship hit!\nYou lost a life and score.', font=("Courier", 20, 'bold'), align='center')
    else:
        ship_hit.write(arg="Ship hit!\nYou lost a life. You didn't\n"
                           "lose score because you'd be\nin the negatives...", font=("Courier", 20, 'bold'), align='center')
    flashed_messages.append(ship_hit)

    def clear_msg():
        ship_hit.clear()
        flashed_messages.remove(ship_hit)

    le_screen = ship_hit.getscreen()
    le_screen.ontimer(clear_msg, 1000)
#-----GAME LOGIC----#
alien_manager.spawn_aliens() # Summon the aliens
flashed_messages = [] # List to remove turtle text objects i will flash for a bit later
game_on = True # Thingy to check against
while game_on:
    # Update the screen after that sleep right there
    time.sleep(0.0167) # About 60 fps according to ChatGPT
    screen.update()

    # Make aliens move back and forth
    alien_manager.move()
    # Automatically move pellets and stuff
    alien_manager.move_pellets()

    # Aliens randomly shoot a pellet
    random_num = random.randint(1,40) # Also, nerf aliens so there can't be more than 3 shots on screen
    if random_num == 1 and len(alien_manager.pellets) <= 3: # One in 40 chance of pellet being made by aliens and shot
        alien_manager.make_pellet()

    # Check if spaceship pellet (user pellet) hits aliens, and if it does, get rid of it
    if spaceship.pellet: # If a spaceship pellet exists
        for alien in alien_manager.all_aliens: # for every alien
            if spaceship.pellet.distance(alien) <= 15: # Distance between their centers, 10 by 10 pellet and 20 by 20 alien
                # Add score first
                scoreboard.add_score()
                # flash text
                alien_hit()
                # Get rid of the alien
                alien.hideturtle()
                alien_manager.kill_alien(alien)
                # Get rid of pellet
                spaceship.pellet.hideturtle() # Hide the pellet
                spaceship.pellet = None # Reset pellet to none
                break # Break the for loop once we hit an alien, we don't want to kill multiple!

    # Check if alien pellet hits bases, and if it does, break that part of the base
    for p in alien_manager.pellets[:]: # Iterate over a copy, it's safer since it never changes, and nothing can get skipped
        for base_p in base_manager.all_parts:
            if p.distance(base_p) <= 18:
                # Hide the base_part and kill it
                base_p.hideturtle()
                base_manager.all_parts.remove(base_p)
                # Hide pellet
                p.hideturtle()
                alien_manager.pellets.remove(p) # Kill pellet
                # Lose score, but only if score is greater than 0
                if scoreboard.score > 0:
                    scoreboard.lose_score()
                # Flash text
                base_hit(scoreboard.score)
                break # Break for loop for this pellet, don't check against a pellet that isn't there!

    # Check if alien pellet hits spaceship
    for p in alien_manager.pellets[:]:
        for spaceship_part in spaceship.FULL_SPACESHIP:
            if p.distance(spaceship_part) <= 18:
                # Hide alien pellet
                p.hideturtle()
                alien_manager.pellets.remove(p) # Kill pellet
                # Take away life from user
                scoreboard.lose_life()
                # Take score from user only if it's greater than 0
                if scoreboard.score > 0:
                    scoreboard.lose_score()
                # flash text
                spaceship_hit(scoreboard.score)
                break # Break the for loop for that pellet, don't keep checking

#----------HANDLE GAME OVER SCENARIOS-------------#

    # You win!
    if len(alien_manager.all_aliens) <= 0:
        scoreboard.you_win()
        game_on = False # breaks game loop
    # You lose
    if scoreboard.lives <= 0:
        scoreboard.you_lose()
        game_on = False
    elif len(base_manager.all_parts) <= 0:
        scoreboard.you_lose()
        game_on = False



screen.exitonclick() # Keep screen open