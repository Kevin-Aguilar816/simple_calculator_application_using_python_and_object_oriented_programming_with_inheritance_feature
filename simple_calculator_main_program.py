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

    def display_banner(self):
        banner = f""" {Fore.RED + Back.YELLOW}
╔══════════════════════════════════════════════════════╗
║                      KEVCULATOR                      ║
║                   Maangas, Ugh Argh                  ║
╚══════════════════════════════════════════════════════╝  
{Style.RESET_ALL}"""
        print(banner)
