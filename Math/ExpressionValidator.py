import re

class ExpressionValidator:
    @staticmethod
    def has_operators(expression):
        return re.findall(r"(\+|\-|\/|\*|\%)", expression, re.I | re.M).__len__() > 0

    @staticmethod
    def has_numbers(expression):
        return re.findall(r"(\d)", expression, re.I | re.M).__len__() > 0

    @staticmethod
    def has_alphanumeric_chars(expression):
        return re.findall(r"[a-z]", expression, re.I | re.M).__len__() > 0

    @staticmethod
    def is_expression(expression):
        if len(str(expression).replace(' ', '')) < 3:
            return False

        number_quantity = len(re.findall(r"(\d+)", expression, re.I | re.M))
        operator_quantity = len(re.findall(r"(\-|\+|\*{1,2}|\/+|\%)", expression, re.I | re.M))

        return (number_quantity - 1) == operator_quantity

    @staticmethod
    def validate(expression):
        if not ExpressionValidator.has_operators(expression):
            raise Exception('Given expression does not contain any valid operators. Which is (+, -, *, /)')
        elif not ExpressionValidator.has_numbers(expression):
            raise Exception('Given expression does not contain any number.')
        elif ExpressionValidator.has_alphanumeric_chars(expression):
            raise Exception('Given expression contains undefined variables.')
        elif not ExpressionValidator.is_expression(expression):
            raise Exception('Given string isn\'t an valid math expression.')
