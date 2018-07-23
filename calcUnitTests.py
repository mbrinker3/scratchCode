import calculator
import unittest
from unittest.mock import patch

class calcTestCase(unittest.TestCase):
    def testOne(self):
        calc = calculator.Calculator()
        #Equations called out in the application
        self.assertEqual(calc.evaluate("2+2="), 4)
        self.assertEqual(calc.evaluate("-5* 5/3 ="), -8.3333333333333333)
        self.assertEqual(calc.evaluate("7+-6 ="), 1)
        self.assertEqual(calc.evaluate("-5* 5-15 /3 ="), -30)
    def testTwo(self):
        calc = calculator.Calculator()
        #Other useful test cases
        self.assertEqual(calc.evaluate("11+12+1*20 / 20") , 24)
        self.assertEqual(calc.evaluate("22+22=") , 44)
        self.assertEqual(calc.evaluate("-22/-22=") , 1)
        self.assertEqual(calc.evaluate("-100--50=") , -50)
        #Edge cases
        with self.assertRaises(ZeroDivisionError) as ex:
            calc.evaluate("100/0=")
        exception = ex.exception
        self.assertEqual(exception.args[0],'float division by zero')

    def testThree(self):
        calc = calculator.Calculator()
        #Individual function test cases
        #preProcessing
        self.assertEqual(calc.preProcessExpression("1 + 1 = "), "1+1")
        self.assertEqual(calc.preProcessExpression("1 -- 1 = "), "1n-1")
        self.assertEqual(calc.preProcessExpression("1 + 1 -1 = "), "1+1n1")

        #Getting numbers
        tests = ['5n15/3','11+12+120','15n-20']
        leftExpectedNumbers = ['3','120','-20']
        leftExpectedOriginals = ['5n15/','11+12+','15n']
        rightExpectedNumbers = ['5','11','15']
        rightExpectedOriginals = ['n15/3','+12+120','n-20']

        for i in range(len(tests)):
            self.assertEqual(calc.getNumber(tests[i],"left"),(leftExpectedNumbers[i],leftExpectedOriginals[i]))
            self.assertEqual(calc.getNumber(tests[i],"right"),(rightExpectedNumbers[i],rightExpectedOriginals[i]))

        with self.assertRaises(ValueError) as ex:
            calc.getNumber("11+12+13","center")
        exception = ex.exception
        self.assertEqual(exception.args[0],'Unrecognized direction')

    def testFour(self):
        calc = calculator.Calculator()
        #Text parser test
        #If everything doesn't work as expected, this will enter an infinite loop, or throw an exception.
        tests = list("11+12+1*20 / 20=Q")
        with patch.object(calculator,"getwch",create=True,side_effect = tests):
            c = calculator.Calculator()
            c.inputParser()


def main():
    unittest.main()
if __name__ == "__main__":
    main()