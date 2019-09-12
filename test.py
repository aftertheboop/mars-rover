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

    # Test to check for invalid operations characters
    def test_3(self):
        rover = Rover(5, 5)
        self.assertRaises(Exception, rover.setoperations, str("MMRMKLMMLM"))

    # Test that an exception is raised if the rover goes out of bounds
    def test_4(self):
        rover = Rover(5, 5)
        rover.setstart('1 1 N')
        rover.setoperations('MMMMMM')
        self.assertRaises(Exception, rover.operate)

    # Test that an exception is raised if the plateau does not have an x and a y coordinate
    def test_5(self):
        nasa = NASA()
        self.assertRaises(Exception, nasa.setplateau, "55")
    # Test that an exception is raised if the plateau input has additional parameters
    def test_6(self):
        nasa = NASA()
        self.assertRaises(Exception, nasa.setplateau, "5 6 1")

    # Test that an exception is raised if coordinates are < 1
    def test_7(self):
        nasa = NASA()
        self.assertRaises(Exception, nasa.setplateau, "-1 5")

    # Test for invalid rover start input
    def test_8(self):
        rover = Rover(5, 5)
        self.assertRaises(Exception, rover.setstart, '4 1 D')


if __name__ == '__main__':
    unittest.main()

