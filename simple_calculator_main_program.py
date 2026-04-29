import os
import time
import sys
from calculator_functionalities import (
    CalculatorActions, DivisionByZeroError, InvalidInputError)


class SimpleCalculator:
    def __init__(self):
        self.clear_screen()
