'''
Created on 04/11/2016

@author: JAT
@source: https://github.com/apdaros/tdd-numeros_romanos/blob/master/src/main/java/RomanConverter.java
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
    
    def testInVOut5(self):
        assert self.conv.convertRomanToInt("V") == 5
            
    def testInVIIIOut8(self):
        assert self.conv.convertRomanToInt("VIII") == 8
        
    def testInIXOut9(self):
        assert self.conv.convertRomanToInt("IX") == 9
            
    def testInXOut10(self):
        assert self.conv.convertRomanToInt("X") == 10
        
    def testInXIXOut19(self):
        assert self.conv.convertRomanToInt("XIX") == 19
    
    def testInXVIOut16(self):
        assert self.conv.convertRomanToInt("XVI") == 16
        
    def testInXLOut40(self):
        assert self.conv.convertRomanToInt("XL") == 40
        
    def testInCLXXOut170(self):
        assert self.conv.convertRomanToInt("CLXX") == 170
        
    def testInDXCOut590(self):
        assert self.conv.convertRomanToInt("DXC") == 590
        
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
