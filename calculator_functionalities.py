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

    def show_history(self):
        if not self.history:
            print(f"{Fore.YELLOW}No calculations yet. {Style.RESET_ALL}")
            return
        print(
            f"{Fore.CYAN}Calculation History ({len(self.history)} entries):{Style.RESET_ALL}")
        for i, calc in enumerate(self.history[-5:], 1):
            print(f"{Fore.GREEN}{i}. {calc['timestamp']}{Style.RESET_ALL}")
            print(
                f"{calc[num_one]} {calc['operation']} {calc['num_two']} = {calc['result']}")
