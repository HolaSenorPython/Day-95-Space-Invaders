from turtle import Turtle
FONT = ("Courier", 36, "bold")
WHITE = '#FFFFFF'
YELLOW = '#FFCC00'
RED = '#FF0000'
LIME_GREEN = '#32CD32'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Set scoreboard properties on init
        self.score = 0
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color(WHITE)
        # Write the title first
        self.goto(0, 345)
        self.write(arg="Space Invaders!", font=FONT, align="center")
        # Write the score
        self.goto(250, 300)
        self.color(YELLOW)
        self.write(arg=f'Score: {self.score}', font=('Courier', 26, 'bold'), align='center')
        # Write lives count
        self.goto(-250, 300)
        self.color(RED)
        self.write(arg=f'Lives: {self.lives}', font=('Courier', 26, 'bold'), align='center')

    # After an alien is hit, add 100 to score
    def add_score(self):
        self.score += 100
        self.clear() # Clears all text
        # Now rewrite all text
        # Write the title first
        self.goto(0, 345)
        self.color(WHITE) # make sure title card is white
        self.write(arg="Space Invaders!", font=FONT, align="center")
        # Write the score
        self.goto(250, 300)
        self.color(YELLOW)
        self.write(arg=f'Score: {self.score}', font=('Courier', 26, 'bold'), align='center')
        # Write lives count
        self.goto(-250, 300)
        self.color(RED)
        self.write(arg=f'Lives: {self.lives}', font=('Courier', 26, 'bold'), align='center')

    # If base is hit, lower score
    def lose_score(self):
        self.score -= 50
        self.clear()
        # Now rewrite all text
        # Write the title first
        self.goto(0, 345)
        self.color(WHITE)  # make sure title card is white
        self.write(arg="Space Invaders!", font=FONT, align="center")
        # Write the score
        self.goto(250, 300)
        self.color(YELLOW)
        self.write(arg=f'Score: {self.score}', font=('Courier', 26, 'bold'), align='center')
        # Write lives count
        self.goto(-250, 300)
        self.color(RED)
        self.write(arg=f'Lives: {self.lives}', font=('Courier', 26, 'bold'), align='center')

    # Win screen
    def you_win(self):
        self.clear() # clear all text
        self.goto(0, 0)
        self.color(LIME_GREEN)
        self.write(arg=f'You win!\nFinal score: {self.score}', font=FONT, align='center')

    # Lose screen
    def you_lose(self):
        self.clear()
        self.goto(0, 0)
        self.color(RED)
        self.write(arg=f"You lose!\nFinal score: {self.score}", font=FONT, align='center')

    # When user loses a life
    def lose_life(self):
        self.lives -= 1
        self.clear()
        # Now rewrite all text
        # Write the title first
        self.goto(0, 345)
        self.color(WHITE)  # make sure title card is white
        self.write(arg="Space Invaders!", font=FONT, align="center")
        # Write the score
        self.goto(250, 300)
        self.color(YELLOW)
        self.write(arg=f'Score: {self.score}', font=('Courier', 26, 'bold'), align='center')
        # Write lives count
        self.goto(-250, 300)
        self.color(RED)
        self.write(arg=f'Lives: {self.lives}', font=('Courier', 26, 'bold'), align='center')