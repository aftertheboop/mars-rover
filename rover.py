maxx = 5
maxy = 5
startx = 0
starty = 0


class Rover:
    # Rover Constructor
    def __init__ (self, x, y, heading):
        # A rover has a starting x, y and heading, as well as 4 cardinal directions it can travel
        self.x = x
        self.y = y
        self.heading = heading
        # Define the heading constraints; realistically this could be expanded to include NE, SW etc.
        self.headings = ['N', 'E', 'S', 'W']

    def turn(self, direction):
        # Assume the direction is (R)ight
        delta = 1
        # If L is input, reverse the delta
        if direction == 'L':
            delta = -1
        # Get the current heading index
        headingindex = self.headings.index(self.heading)
        # Add the delta to the index
        newheading = headingindex + delta
        # If the newheading is outside the limit of coordinates, reset to 0
        if newheading >= len(self.headings):
            newheading = 0
        # If the newheading index is less than zero, reset to the index limit
        if newheading < 0:
            newheading = len(self.headings) - 1
        # Set the new heading
        self.heading = self.headings[newheading]

    def move(self):
        # Create a dictionary with x,y movement coordinates
        rules = {
            'N': [0, 1],
            'E': [1, 0],
            'S': [0, -1],
            'W': [-1, 0]
        }
        # Get the current heading's x,y coord change rules
        coords = rules[self.heading]
        # Modify the coordinates
        self.x = self.x + coords[0]
        self.y = self.y + coords[1]

    def operate(self, instructions):
        for action in instructions:
            # TODO: Error trap for non-LRM actions
            if action == 'M':
                self.move()
            else:
                self.turn(action)

    def getposition(self):
        print(str(self.x) + ' ' + str(self.y) + ' ' + str(self.heading))


oneRover = Rover(1, 2, 'N')
oneRover.operate('LMLMLMLMM')
oneRover.getposition()

twoRover = Rover(3, 3, 'E')
twoRover.operate('MMRMMRMRRM')
twoRover.getposition()
