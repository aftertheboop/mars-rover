import unittest

maxx = 5
maxy = 5
startx = 0
starty = 0


class Rover:
    # Rover Constructor
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 'N'
        # Define the heading constraints; realistically this could be expanded to include NE, SW etc.
        self.headings = ['N', 'E', 'S', 'W']

    def setstart(self, userinput):
        # TODO: Handle inputs of more or less than 3 vars
        inputarray = userinput.split(' ')

        self.x = int(inputarray[0])
        self.y = int(inputarray[1])
        self.heading = inputarray[2]

    def setoperations(self, operations):
        self.operations = operations

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

    def operate(self):
        for action in self.operations:
            # TODO: Error trap for non-LRM actions
            if action == 'M':
                self.move()
            else:
                self.turn(action)

    def getposition(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.heading)


class RoversUnitTest(unittest.TestCase):
    def test_1(self):
        # Prepare and run Rover One
        oneRover = Rover()
        oneRover.setstart('1 2 N')
        oneRover.setoperations('LMLMLMLMM')
        oneRover.operate()
        # Prepare and run Rover Two
        twoRover = Rover()
        twoRover.setstart('3 3 E')
        twoRover.setoperations('MMRMMRMRRM')
        twoRover.operate()
        # Get rover outputs
        output1 = oneRover.getposition()
        output2 = twoRover.getposition()
        # Expected results
        expected1 = "1 3 N"
        expected2 = "5 1 E"
        # Test results
        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)


if __name__ == '__main__':
    unittest.main()

