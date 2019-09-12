import unittest
from rover import Rover

class NASA:
    """
    The NASA class is the main automation of the program, getting the initial dimensions of the plateau and running the
    Mars Rovers
    """

    def __init__(self):
        self.maxx = 0
        self.maxy = 0
        self.startx = 0
        self.starty = 0

    def start(self):
        # Welcome
        print('** Welcome to NASA\'s Rover Program **')

        # Get the maximum coordinates of the plateau
        plateaucoords = input("Enter the plateau\'s maximum coordinates in 'X Y' format:\n")
        # Set the maximum coordinates of the plateau
        self.setplateau(plateaucoords)
        plateau = self.getplateau()

        # Get rover inputs
        roveronestart = input("Enter Rover One\'s start coordinates and heading in 'X Y H' format:\n")
        roveroneinstructions = input("Enter Rover One\'s start coordinates consisting of L, R and M in a string:\n")
        rovertwostart = input("Enter Rover Two\'s start coordinates and heading in 'X Y H' format:\n")
        rovertwoinstructions = input("Enter Rover Two\'s start coordinates consisting of L, R and M in a string:\n")

        # Set up the rovers
        roverone = Rover(plateau[0], plateau[1])
        roverone.setstart(roveronestart)
        roverone.setoperations(roveroneinstructions)
        rovertwo = Rover()
        rovertwo.setstart(rovertwostart)
        rovertwo.setoperations(rovertwoinstructions)

        # Run the rovers
        roverone.operate()
        rovertwo.operate()

        # Print results
        print(roverone.getposition())
        print(rovertwo.getposition())

    def setplateau(self, plateausize):
        # Split the input into an array
        plateauarray = plateausize.split(' ')
        # Checks the size of the generated array
        if len(plateauarray) != 2:
            raise Exception('Plateau coordinates input incorrect. Please start again')
            exit(1)

        self.maxx = int(plateauarray[0])
        self.maxy = int(plateauarray[1])

    def getplateau(self):
        return [self.maxx, self.maxy]


class RoversUnitTest(unittest.TestCase):
    def test_1(self):
        # Prepare and run Rover One on 5 5 plateau
        oneRover = Rover(5, 5)
        oneRover.setstart('1 2 N')
        oneRover.setoperations('LMLMLMLMM')
        oneRover.operate()
        output1 = oneRover.getposition()
        expected1 = "1 3 N"
        self.assertEqual(output1, expected1)

    def test_2(self):
        # Prepare and run Rover Two on 5 5 plateau
        twoRover = Rover(5, 5)
        twoRover.setstart('3 3 E')
        twoRover.setoperations('MMRMMRMRRM')
        twoRover.operate()
        # Get rover outputs
        output2 = twoRover.getposition()
        # Expected results
        expected2 = "5 1 E"
        # Test results
        self.assertEqual(output2, expected2)


if __name__ == '__main__':
    # Comment the below to ignore user input
    #mynasa = NASA()
    #mynasa.start()

    # Uncomment this to run the unit tests
    unittest.main()

