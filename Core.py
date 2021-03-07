from lark import Lark
from Grammer import grammer
from TreeProcessor import Calculator

parser = Lark(grammer, start="exp", parser="earley", lexer="standard")
calculator = Calculator()
answer = calculator.transform(parser.parse('|5.5 - 6|'))
print(answer)