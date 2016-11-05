'''
Created on 04/11/2016

@author: JAT
'''
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.conv = ConvToInt()
    
    def tearDown(self):
        pass
    
    def testInEmptyOutNone(self):
        assert self.conv.convertRomanToInt("") == None
        assert self.conv.convertRomanToInt(" ") == None
        
    def testInIOut1(self):
        assert self.conv.convertRomanToInt("I") == 1
        
    def testInIIIOut3(self):
        assert self.conv.convertRomanToInt("III") == 3
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class ConvToInt:
    def __init__(self):
        self.dic = {"I" : 1, "V" : 5, "X" : 10}
        
    def convertRomanToInt(self, argRoman):
        if(argRoman == "" or argRoman == " "):
            return None
        return argRoman.count("I")
        
        