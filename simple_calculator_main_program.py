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

    def calculate(self, operation: str, calculator, num_one: float, num_two: float):
        try:
            result = calculator.calculate(num_one, num_two)
            calculator.add_to_history(num_one, operation, num_two, result)

            print(f"\n{Fore.YELLOW{"="*60}}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Calculation Result:{Style.RESET_ALL}")
            print(
                f"{Fore.WHITE}{num_one} {operation} {num_two} = {Fore.GREEN}{result}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW{"="*60}}{Style.RESET_ALL}")

            return True

        except DivisionByZeroError as error:
            print(f"{Fore.RED}{error}{Style.RESET_ALL}")
            return False
        except Exception as error:
            print(f"{Fore.RED}An error occurred: {str(error)}{Style.RESET_ALL}")
            return False

    def ask_to_continue(self) -> bool:
        print(f"/n{Fore.GREEN}{"="*50}{Style.RESET_ALL}")

        while True:
            choice = input(
                f"{Fore.CYAN}Do you want to perform another calculation? (Y/N): {Style.RESET_ALL}").strip().upper()
            if choice in ['y', 'yes', '']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print(
                    f"{Fore.YELLOW}Invalid choice. Please enter Y or N.{Style.RESET_ALL}")
