
class CalcModel:

    ERROR_MESSAGE = "Error occurred"

    def evaluate_expression(self, expression):
        try:
            return str(eval(expression))
        except Exception:
            return self.__class__.ERROR_MESSAGE


