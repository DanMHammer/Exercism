import string
import random

class Robot(object):
    def __init__(self):
        self.database = set()
        self.name = ""
        self.new_name()

    def new_name(self):
        new = ""
        for x in range(0, 2):
            new += random.choice(string.ascii_uppercase)

        for x in range(0, 3):
            new += str(random.randint(0, 9))

        if new not in self.database:
            self.database.add(new)
            self.name = new
        else:
            self.new_name()

    def reset(self):
        self.new_name()