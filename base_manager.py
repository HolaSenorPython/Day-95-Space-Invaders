import turtle as t

YELLOW = '#FFCC00'
X_INCREMENT = 310

def position_check(loop_num):
    # This function will check for every possible number and where to place the block. Its very tedious but yeah.
    if loop_num == 0:
        return -320, -180
    elif loop_num == 1:
        return -300, -180
    elif loop_num == 2:
        return -340, -160
    elif loop_num == 3:
        return -320, -160
    elif loop_num == 4:
        return -300, -160
    elif loop_num == 5:
        return -280, -160
    elif loop_num == 6:
        return -280, -140
    elif loop_num == 7:
        return -300, -140
    elif loop_num == 8:
        return -320, -140
    elif loop_num == 9:
        return -340, -140
    elif loop_num == 10:
        return -320, -120
    elif loop_num == 11:
        return -300, -120

class BaseManager:

    def __init__(self):
        self.all_parts = []
        self.make_bases() # do method on init

    def make_bases(self):
        for i2 in range(3):
            for i in range(12): # do this 12 times, basically making a turtle and placing it where we need:
                base_part = t.Turtle()
                base_part.penup()
                base_part.color(YELLOW)
                base_part.shape('square')
                # Now make the position dynamic based on which base we're on in loop
                if i2 == 0:
                    position = position_check(i)
                    base_part.setpos(position)
                elif i2 == 1:
                    position = position_check(i)
                    new_pos = (position[0] + X_INCREMENT, position[1]) # maintain same y, but increase the X to spread out bases
                    base_part.setpos(new_pos)
                elif i2 == 2:
                    position = position_check(i)
                    new_pos = (position[0] + (X_INCREMENT * 2), position[1]) # Maintain same y, move x by double to signify it's farther than base 1
                    base_part.setpos(new_pos)
                self.all_parts.append(base_part) # Add all the parts to the list

    # Kill that base part from memory!
    def kill_base_part(self, part):
        self.all_parts.remove(part)
