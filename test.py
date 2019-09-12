import unittest
from rover import Rover


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


if __name__ == '__main__':
    unittest.main()

