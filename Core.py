from lark import Lark
from Grammer import grammer
from TreeProcessor import Calculator

def process(text):
    parser = Lark(grammer, start="exp", parser="earley", lexer="standard")
    calculator = Calculator()
    answer = calculator.transform(parser.parse(text))
    return answer
