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
        
    def testInIVOut4(self):
        assert self.conv.convertRomanToInt("IV") == 4
        
    def testStrOutrtS(self):
        assert self.conv.invertString("Str") == "rtS"
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class ConvToInt:
    def __init__(self):
        self.dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
    def convertRomanToInt(self, argRoman):
        if(argRoman == "" or argRoman == " "):
            return None
        else:
            str = self.invertString(argRoman)
            sum = 0
            lastNumber = 0
            for i in str:
                current = self.dic[i]
                positioner = 1
                if(current < lastNumber):
                    positioner = -1
                sum += self.dic[i] * positioner
                lastNumber = current
            print(sum)
            return sum
        
    def invertString(self, str):
        return str[::-1]