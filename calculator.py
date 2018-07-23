import sys
from msvcrt import getwch
class Calculator(object):

    def __init__(self, *args, **kwargs):
        """Simple calculator program."""
        self.operations = {"*" : self.multiply, "/" : self.divide, "+" : self.add, "n" : self.subtract}
        self.operators = ["*","/","+","n"] #This list enforces PEMDAS order.  Python Dictionaries aren't always iterated in the originally-specified order, but lists are.
        self.opsDetectNegative = {"*n" : "*-","/n" : "/-","+n" : "+-","nn" : "n-"}

    def inputParser(self):
        """Accepts input from the user.  
        Supports +,-,*,/ operators.
        Evaluates when '=' is entered.
        Quit with 'Q'"""
        input = ""
        expression = ""
        print("Please input an equation.\n Press = to evaluate, or Q to quit.")
        while input != 'Q':
            input = getwch()
            if(input == '\x08'):#Backspace character
                expression = expression[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            elif (input == '='):
                try:
                    print("= " + str(self.evaluate(expression)))
                    expression = ""
                except:
                    print("Unrecognized expression.")
            elif(input != 'Q'):    
               expression = expression + input
               sys.stdout.write(input)
               sys.stdout.flush()

    def evaluate(self,expression):
        """Accepts an expression as a string of the form: 1+2-3*4/5
        Returns the value of that string.
        """
        expression = self.preProcessExpression(expression)
        value = expression
        for op in self.operators:
            sides = expression.split(op)
            for i in range(len(sides)-1):
                first,left = self.getNumber(sides[i],"left")
                second,right = self.getNumber(sides[i+1],"right")
                value = self.operations[op](first,second)
                sides[i+1] = left + str(value) + right
            expression = sides[len(sides)-1]
        return value

    def preProcessExpression(self,expression):
        """Convert from user input to evaluation format.
        Returns converted string"""
        #remove whitespace, if present
        expression = expression.replace(" ", "")
        #remove the equal sign.
        expression = expression.replace("=","")
        #handle negatives:
        expression = expression.replace("-","n")
        for op in self.opsDetectNegative:
            expression = expression.replace(op,self.opsDetectNegative[op])
        if(expression[0] == "n"):
            expression = "-" + expression[1:]
        return expression

    def getNumber(self, side,direction):
        """Separates an evaluation string into the number being evaluated, and all of the other characters.
        side: the evaluation string
        direction: which side of the equation you're on.  Accepts "left" and "right".
        Since left and right refer to the side of the equation, "left" will return the rightmost number, and "right" will return the leftmost number.
        returns(number, remainder)"""
        original = ""
        if(direction == "left"):
            index = -1
            for op in self.operators:
                if(side.rfind(op) != -1):
                    index = max(index,side.rfind(op))
            if(index != -1):
                original = side[:index+1]
                side = side[index+1:]
        elif(direction == "right"):
            index = len(side)
            for op in self.operators:
                if(min(index,side.find(op)) != -1):
                    index = min(index,side.find(op))
            original = side[index:]
            side = side[:index]
        else:
            raise ValueError("Unrecognized direction")
        return side,original


    #Operators
    @staticmethod
    def add(first, second):
        return float(first) + float(second)
    
    @staticmethod
    def subtract(first, second):
        return float(first) - float(second)
    
    @staticmethod
    def multiply(first, second):
        return float(first) * float(second)
    
    @staticmethod
    def divide(first,second):
        return float(first) / float(second)
        
def main():
    calc = Calculator()
    calc.inputParser()

if __name__ == "__main__":
    main()