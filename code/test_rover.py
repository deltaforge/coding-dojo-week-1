#!/opt/rh/python33/root/usr/bin/python

import rover
import unittest

class TestRover(unittest.TestCase):
    def testConstructor(self):
        r = rover.Rover(10,12,'N')
        self.assertEqual(10, r.x)
        self.assertEqual(12, r.y)
        self.assertEqual('N', r.orientation)

if __name__ == '__main__':
    unittest.main()
