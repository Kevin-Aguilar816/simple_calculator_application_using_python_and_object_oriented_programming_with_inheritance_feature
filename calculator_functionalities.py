import time
from abc import ABC, abstractmethod
from typing import Tuple, Optional
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class CalculatorError(Exception):
    pass


class InvalidOperationError(CalculatorError):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class InvalidInputError(CalculatorError):
    pass


class BaseCalculator(ABC):
    def __init__(self):
        self.history = []

    @abstractmethod
    def calculate(self, num_one: float, num_two: float) -> float:
        pass
