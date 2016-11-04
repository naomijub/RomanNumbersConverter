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
        
    def testIn14OutXIV(self):
        assert self.conv.convertIntToRoman(14) == "XIV"
        
    def testIn44OutXLIV(self):
        assert self.conv.convertIntToRoman(44) == "XLIV"
        
    def testIn99OutXCIX(self):
        assert self.conv.convertIntToRoman(99) == "XCIX"
    
    def testIn350OutCCCL(self):
        assert self.conv.convertIntToRoman(350) == "CCCL"
        
    def testIn500OutD(self):
        assert self.conv.convertIntToRoman(500) == "D"
        
    def testIn900OutCM(self):
        assert self.conv.convertIntToRoman(900) == "CM"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class ConvToRoman:
    
    def __init__(self):
        self.dic = {"u": ["I", "V", "X"], "d" : ["X", "L", "C"], "c" : ["C", "D", "M"]}
    
    def convertIntToRoman(self, argInt):
        if (argInt <= 0):
            return None
        str = ""
        str += self.GetStringValue(self.HundredValue(argInt), "c")
        str += self.GetStringValue(self.TenValue(argInt), "d")
        str += self.GetStringValue(self.UnitValue(argInt), "u")
        print(argInt, str)
        return str
        
    def UnitValue(self, argInt):
        return (argInt % 10)
    
    def TenValue(self, argInt):
        if(argInt > 9):
            return int(argInt / 10) % 10
        return 0
    
    def HundredValue (self, argInt):
        if(argInt > 99):
            return int(argInt / 100) % 10
        return 0;
    
    def GetStringValue(self, argValue, key):          
        if (argValue == 0):
            return ""
        elif(argValue <=3):
            return self.dic[key][0] * argValue
        elif(argValue < 9):
            diff = argValue - 5;
            if(diff == -1):
                return self.dic[key][0] + self.dic[key][1] 
            else:
                return self.dic[key][1] + (self.dic[key][0] * diff)
        else:
            return self.dic[key][0] + self.dic[key][2]
        
        