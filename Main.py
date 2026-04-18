# This import must be at the very top to ensure UTF-8 encoding is set up before anything else runs.
import Utils.Windows_Fix

# main.py
import time
import logging

# Import utils
from Utils.Logger import setup_logging
from Utils.Helpers import get_name
from Utils.Screen import clear

# Import ALL games
from Games import (
    Age_Checker,
    Calculator,
    Cafe,
    Guessing_Game,
    Text_Search,
    Rock_Paper_Scissors,
    Encrypt_Decrypt,
    Random_Picker,
    Number_Game,
    Password_Generator,
)

# Check for cowsay
try:
    import cowsay

    cowsay_available = True
except ImportError:
    print("cowsay is not installed. Please install it using 'pip install cowsay'")
    cowsay_available = False
    cowsay = None

# Setup logging
setup_logging()


def mainmenu(name):
    """Display the main menu and return user's choice."""
    clear()
    print(f"{name}, Choose something!")
    print()
    print("1. Age checker")
    print("2. Calculator")
    print("3. Cafe system")
    print("4. Guessing game")
    print("5. Big text search")
    print("6. Rock-Paper-Scissors Game")
    print("7. Encrypt / Decrypt messages")
    print("8. Random picker wheel")
    print("9. Number guessing game")
    print("10. Password generator")
    print("11. Exit")
    return input("Enter your choice: ")


def main():
    """Main game loop."""
    try:
        name = get_name()

        while True:
            choice = mainmenu(name)

            if choice == "1":
                Age_Checker.run()
            elif choice == "2":
                Calculator.run()
            elif choice == "3":
                Cafe.run(name)
            elif choice == "4":
                Guessing_Game.run()
            elif choice == "5":
                Text_Search.run()
            elif choice == "6":
                Rock_Paper_Scissors.run()
            elif choice == "7":
                Encrypt_Decrypt.run()
            elif choice == "8":
                Random_Picker.run()
            elif choice == "9":
                Number_Game.run()
            elif choice == "10":
                Password_Generator.run()
            elif choice == "11":
                print("Goodbye!")
                logging.info("User exited the game")
                break
            else:
                print("Please choose a number from 1 to 11!")

            input("\nPress Enter to return to main menu...")

        # Cow at the end
        if cowsay_available:
            cow_text = input("Before you go, What do you want the cow to say? ").strip()
            if cow_text:
                print("Here is a cow for you!")
                cowsay.cow(cow_text)
            else:
                print("Here's a default cow for you:")
                cowsay.cow("Moo!")
        else:
            print("Sorry, cowsay is not available. No cow for you :(")

        print("\n" + "=" * 40)
        print("I really hope you enjoyed that")
        print("=" * 40)
        print("\nMy discord user: just_pat123")
        input("\nPress Enter to exit...")

    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! (Interrupted by user)")
        logging.info("User interrupted the program with KeyboardInterrupt")
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}", exc_info=True)
        print("\n⚠️  An unexpected error occurred. Check data/game.log for details.")


if __name__ == "__main__":
    main()
