from lark import Lark
from Grammer import grammer
from TreeProcessor import Calculator

parser = Lark(grammer, start="exp", parser="earley", lexer="standard")
calculator = Calculator()
answer = calculator.transform(parser.parse('(3 * -4) + sqrt(4)'))
print(answer)
