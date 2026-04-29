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
