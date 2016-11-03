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

    def testIn2OutII(self):
        assert self.conv.convertIntToRoman(2) == "II"

    def testIn3OutIII(self):
        assert self.conv.convertIntToRoman(3) == "III"
        
    def testIn0OutNone(self):
        assert self.conv.convertIntToRoman(0) == None
    
    def testIn4OutIV(self):
        assert self.conv.convertIntToRoman(4) == "IV"
        
    def testIn5OutV(self):
        assert self.conv.convertIntToRoman(5) == "V"
        
    def testIn8OutVIII(self):
        assert self.conv.convertIntToRoman(8) == "VIII"
        
    def testIn9OutIX(self):
        assert self.conv.convertIntToRoman(9) == "IX"
        
    def testIn10OutX(self):
        assert self.conv.convertIntToRoman(10) == "X"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class ConvToRoman:
    def convertIntToRoman(self, argInt):
        if (argInt <= 0):
            return None
        elif(argInt <=3):
            return "I" * argInt
        elif(argInt < 9):
            diff = argInt - 5;
            if(diff == -1):
                return "IV"
            else:
                return "V" + ("I" * diff)
        elif (argInt == 9):
            return "IX"
        else:
            return "X"
        
        
        