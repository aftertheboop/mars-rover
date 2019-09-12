import unittest
from rover import Rover
from mars import NASA


class RoversUnitTest(unittest.TestCase):
    # Tests the primary conditions of the challenge
    def test_1(self):
        # Prepare and run Rover One on 5 5 plateau
        rover = Rover(8, 8)
        rover.setstart('1 2 E')
        rover.setoperations('MMLMRMMRRMML')
        rover.operate()
        output1 = rover.getposition()
        expected1 = "3 3 S"
        self.assertEqual(output1, expected1)

    # Tests an alternative rover movement plan
    def test_2(self):
        # Prepare and run Rover Two on 5 5 plateau
        rover = Rover(5, 5)
        rover.setstart('3 3 E')
        rover.setoperations('MMRMMRMRRM')
        rover.operate()
        # Get rover outputs
        output2 = rover.getposition()
        # Expected results
        expected2 = "5 1 E"
        # Test results
        self.assertEqual(output2, expected2)

    # Test to check the rover for invalid operations characters, including out of bounds
    def test_3(self):
        rover = Rover(5, 5)
        self.assertRaises(Exception, rover.setoperations, str("MMRMKLMMLM"))    # invalid character in commands
        rover.setstart('1 1 N')                                     # start the rover at 1 1
        rover.setoperations('MMMMMM')                               # move the rover out of bounds positively
        self.assertRaises(Exception, rover.operate)                 # execute the operation and throw an error
        rover.setstart('1 1 S')                                     # start the rover at 1 1 facing south
        rover.setoperations('MMM')                                  # move 3 spaces down
        self.assertRaises(Exception, rover.operate)                 # check for a negative exception

    # Test that an exception is raised if the plateau input has additional or incorrect parameters
    def test_4(self):
        nasa = NASA()
        self.assertRaises(Exception, nasa.setplateau, "55")         # insufficient input
        self.assertRaises(Exception, nasa.setplateau, "5 6 1")      # too much input
        self.assertRaises(Exception, nasa.setplateau, "-1 5")       # negative input in first field
        self.assertRaises(Exception, nasa.setplateau, "1 -5")       # negative input in second field
        self.assertRaises(Exception, nasa.setplateau, "5 5 5 5")    # too much input
        self.assertRaises(Exception, nasa.setplateau, "1 E")        # non-numeric input

    # Test for invalid rover start input
    def test_5(self):
        rover = Rover(5, 5)
        self.assertRaises(Exception, rover.setstart, '4 1 D')       # invalid direction in command
        self.assertRaises(Exception, rover.setstart, '4 E')         # insufficient input


if __name__ == '__main__':
    unittest.main()

