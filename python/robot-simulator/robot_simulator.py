# Globals for the bearings
# Change the values as you see fit
NORTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
SOUTH = (0, -1)

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def simulate(self, string):
        for char in string:
            if char == "A":
                self.advance()
            elif char == "L":
                self.turn_left()
            elif char == "R":
                self.turn_right()
            else:
                raise ValueError("Invalid input '{char}'")

    def advance(self):
        x, y = self.bearing
        a, b = self.coordinates
        self.coordinates = (a + x, b + y)

    def turn_left(self):
        x, y = self.bearing
        self.bearing = (-y, x)

    def turn_right(self):
        x, y = self.bearing
        self.bearing = (y, -x)
