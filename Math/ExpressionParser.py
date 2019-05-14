from Math.ExpressionValidator import ExpressionValidator

class ExpressionParser:
    expression = None
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        ExpressionValidator.validate(self.expression)

