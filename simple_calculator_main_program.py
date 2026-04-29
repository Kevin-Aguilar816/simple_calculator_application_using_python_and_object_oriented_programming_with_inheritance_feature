import os
import time
import sys
from calculator_functionalities import (
    CalculatorActions, DivisionByZeroError, InvalidInputError)


class SimpleCalculator:
    def __init__(self):
        self.clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
