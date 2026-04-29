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

    def display_menu(self):
        print(f"{Fore.CYAN}Please select an operation:{Style.RESET_ALL}")
        for key, (name, _) in CalculatorActions.operations.items():
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}. {name}")
        print(f" {Fore.YELLOW}H{Style.RESET_ALL}. View History")
        print(f" {Fore.RED}Q{Style.RESET_ALL}. Quit")
        print("=" * 50)
