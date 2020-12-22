def sum_two_numbers(number1: float, number2: float) -> float:
    try:
        if validate_numeric(number1) and validate_numeric(number2):
            total = float(number1) + float(number2)
            return total
    except ValueError:
        pass


def subtract_two_numbers(number1: float, number2: float) -> float:
    if validate_numeric(number1) and validate_numeric(number2):
        total = number1 - number2
        return total


def multiply_two_numbers(number1: float, number2: float) -> float:
    if validate_numeric(number1) and validate_numeric(number2):
        total = number1 * number2
        return total


def divide_two_numbers(number1: float, number2: float) -> float:
    if validate_numeric(number1) and validate_numeric(number2) and validate_number_not_zero(number2):
        total = number1 / number2
        return total


def validate_numeric(number: float) -> bool:
    if isinstance(number, float) or isinstance(number, int):
        return True
    raise ValueError(f'Value {number} is not numeric.')


def validate_number_not_zero(number: float) -> bool:
    if number != 0:
        return True
    raise ValueError(f'The divisor can not be 0.')