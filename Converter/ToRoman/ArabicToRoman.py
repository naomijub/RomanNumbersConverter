'''
Created on 02/11/2016

@author: JAT
'''
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.conv = ConvToRoman()


    def tearDown(self):
        pass


    def testIn1OutI(self):
        assert self.conv.convertIntToRoman(1) == "I"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class ConvToRoman:
    def convertIntToRoman(self, argInt):
        return "I"