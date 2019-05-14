from sys import argv
from Math.ExpressionParser import ExpressionParser

expression = ' '.join(argv[1:])

expression_parser = ExpressionParser(expression)

try:
    expression_parser.evaluate()
except Exception as error:
    print(error)