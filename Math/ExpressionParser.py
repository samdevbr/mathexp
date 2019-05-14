from Math.ExpressionValidador import ExpressionValidador

class ExpressionParser:
    expression = None
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        ExpressionValidador.validate(self.expression)
            
