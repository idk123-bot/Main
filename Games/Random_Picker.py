# games/random_picker.py
from Utils.Logger import setup_logging
import time
import random
from Utils.Helpers import returnx

logging = setup_logging()


def run(name=None):
    """Create a list of items and randomly pick from it."""
    logging.info("User selected random picker")
    choices = []
    print("===== RANDOM PICKER WHEEL =====")
    print("Commands: 'done' = finish list, 'Return' to return to main menu\n")

    while True:
        user_input = input(f"Enter item #{len(choices)+1}: ").strip()

        if returnx(user_input):
            return

        if user_input.lower() == "done":
            logging.info("User finished building the list for random picker")
            break

        if user_input:
            if user_input in choices:  # ← Duplicate check HERE
                print(f"❌ '{user_input}' is already in the list!")
                logging.info(f"User tried to add duplicate: {user_input}")
                continue  # ← CONTINUE is fine here—inside the loop
            choices.append(user_input)
            print(f"✅ Added: {user_input}")
        else:
            print("Please enter a valid item!")
            logging.warning("User entered empty item")

    if not choices:
        print("\nYou didn't enter any items!")
        logging.warning("User tried to use random picker without entering any items")
        time.sleep(2)
        return

    print(f"\n📋 Your list ({len(choices)} items): {', '.join(choices)}")

    while True:
        winner = random.choice(choices)
        print(f"\n🎲 The computer picks: --- {winner} ---")
        pick_another = (
            input("\nPick again? (y/n or 'Return' to return to main menu): ")
            .strip()
            .lower()
        )
        if returnx(pick_another):
            return
        elif pick_another in ["n", "no"]:
            print("\nThanks for using the random picker!")
            logging.info("User finished using the random picker")
            time.sleep(2)
            return
        elif pick_another in ["y", "yes"]:
            continue
        else:
            print("Please enter y, n, or return.")
            logging.warning(
                f"User entered invalid input for random picker: {pick_another}"
            )
            time.sleep(2)
            continue
