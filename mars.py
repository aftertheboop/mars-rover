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


if __name__ == '__main__':
    # Comment the below to ignore user input
    mynasa = NASA()
    mynasa.start()


