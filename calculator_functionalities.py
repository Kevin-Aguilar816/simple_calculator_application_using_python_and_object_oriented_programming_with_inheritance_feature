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
        print("=" + 70)
        for i, calc in enumerate(self.history[-5:], 1):
            print(f"{Fore.GREEN}{i}. {calc['timestamp']}{Style.RESET_ALL}")
            print(
                f"{calc[num_one]} {calc['operation']} {calc['num_two']} = {calc['result']}")
        print("=" + 70)


class AdditionCalculator(BaseCalculator):
    def calculate(self, num_one: float, num_two: float) -> float:
        return num_one + num_two


class SubtractionCalculator(BaseCalculator):
    def calculate(self, num_one: float, num_two: float) -> float:
        return num_one - num_two


class MultiplicationCalculator(BaseCalculator):
    def calculate(self, num_one: float, num_two: float) -> float:
        return num_one * num_two


class DivisionCalculator(BaseCalculator):
    def calculate(self, num_one: float, num_two: float) -> float:
        if num_two == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return num_one / num_two


class CalculatorActions:
    operations = {
        "a": ("Addition (+)", AdditionCalculator()),
        "s": ("Subtraction (-)", SubtractionCalculator()),
        "m": ("Multiplication (*)", MultiplicationCalculator()),
        "d": ("Division (/)", DivisionCalculator())
    }

    @staticmethod
    def get_operation_info(choice: str) -> tuple:
        if choice in CalculatorActions.operations:
            name, calculator = CalculatorActions.operations[choice]
            return name.split()[0], calculator
        return None, None

    @staticmethod
    def show_all_history():
        print(f"\n{Fore.MAGENTA}All Calculator History:{Style.RESET_ALL}")
        has_history = False

        for calc_name, (_, calculator) in CalculatorActions.operations.items():
            if calculator.history:
                print(
                    f"\n{Fore.BLUE}{calc_name.upper()} History:{Style.RESET_ALL}")
                for calc in calculator.history[-3]:
                    print(
                        f"{calc[num_one]} {calc['operation']} {calc['num_two']} = {calc['result']}")
                    has_history = True

        if not has_history:
            print(
                f"{Fore.YELLOW}No calculations have been performed yet. {Style.RESET_ALL}")
