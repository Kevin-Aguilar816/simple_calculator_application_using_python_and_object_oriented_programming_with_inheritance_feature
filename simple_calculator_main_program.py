import os
from random import choice
import time
import sys

from colorama import Fore, Style
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

    def get_user_input(self) -> tuple:
        while True:
            self.display_menu()
            choice = input(
                f"{Fore.MAGENTA}Enter your choice: {Style.RESET_ALL}").strip().upper()

            if choice == 'Q':
                return, None, None
            elif choice == 'H':
                CalculatorActions.show_all_history()
                input(
                    f"\n{Fore.YELLOW}Press Enter to continue... {Style.RESET_ALL}")
                self.clear_screen()
                self.display_banner()
                continue
            else:
                operation, calculator = CalculatorActions.get_operation_info(
                    choice)
                if operation:
                    print(f"{Fore.GREEN}You selected: {operation}{Style.RESET_ALL}")
                    return operation, calculator
                print(
                    f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

    def get_numbers(self) -> tuple:
        while True:
            try:
                num_one_str = input(
                    f"{Fore.BLUE}Enter the first number: {Style.RESET_ALL}").strip()
                num_two_str = input(
                    f"{Fore.BLUE}Enter the second number: {Style.RESET_ALL}").strip()

                num_one = float(num_one_str)
                num_two = float(num_two_str)
                return num_one, num_two

            except ValueError:
                print(
                    f"{Fore.RED}Invalid input. Please enter valid numbers.{Style.RESET_ALL}")
