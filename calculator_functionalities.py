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

    def add_to_history(self, operation: str, num_one: float, num_two: float, result: float):
        self.history.append({
            "operation": operation,
            "num_one": num_one,
            "num_two": num_two,
            "result": result,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
