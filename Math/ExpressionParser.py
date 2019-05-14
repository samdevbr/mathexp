from Math.ExpressionValidator import ExpressionValidator

class ExpressionParser:
    expression = None
    def __init__(self, expression):
        self.expression = str(expression).replace('mod', '%')

    def evaluate(self):
        ExpressionValidator.validate(self.expression)

        return eval(self.expression)

