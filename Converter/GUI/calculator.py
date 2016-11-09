'''
Created on 08/11/2016

@author: JAT
'''
import unittest
from ToArabic import RomanToArabic as cvi
from ToRoman import ArabicToRoman as cvr


class Test(unittest.TestCase):
    def setUp(self):
        self.toInt = cvi.ConvToInt()
        self.toRoman = cvr.ConvToRoman()
        self.calc = math()
    
    def test_plus_works_for_2_plus_2_equal_4(self):
        assert self.calc.calculate(2,2, "+") == 4
    
    def test_if_input_is_roman_2_minus_2_ouput_is_0(self):
        assert self.calc.calculate("I", "I", "-") == 0
    

class math:

    def __init__(self):
        self.actions = {
            "+" : lambda arg1, arg2 : arg1 + arg2,
            "-" : lambda arg1, arg2 : arg1 - arg2,
            "*" : lambda arg1, arg2 : arg1 * arg2,
            "/" : lambda arg1, arg2 : arg1 / arg2,
            "%" : lambda arg1, arg2 : arg1 % arg2,
            }

    def calculate(self, arg1, arg2, operator):
        result = self.actions[operator]
        return result(arg1, arg2)