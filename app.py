import subprocess
import sys
import os
from commands.add import add_command
from commands.view import view_command

def run_menu_loop():
    while True:
        print("\nWhat Action would you like to perform?")
        print("1. Add")
        print("2. Delete")
        print("3. Edit")
        print("4. View")
        print("5. Clear")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            print("You selected: Add")
            add_command()
        elif choice == "2":
            print("You selected: Delete")
        elif choice == "3":
            print("You selected: Edit")
        elif choice == "4":
            print("You selected: View")
            view_command()
        elif choice == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


def main():
    if "--session" not in sys.argv:
        script = os.path.abspath(__file__)
        cwd = os.path.dirname(script)

        # Correct: pass args separately, NO embedded quotes
        subprocess.Popen(
            ["cmd.exe", "/k", "python", script, "--session"],
            cwd=cwd
        )
        return

    run_menu_loop()




if __name__ == "__main__":
    main()
