import argparse
from commands.add import add_command

def main():
    parser = argparse.ArgumentParser(
        description="🔥 A powerful Python CLI tool 🔥"
    )
    
    subparsers = parser.add_subparsers(dest="command")

    # --- greet command ---
    greet_parser = subparsers.add_parser("greet", help="Say hello!")
    greet_parser.add_argument("name", help="Name to greet")

    args = parser.parse_args()

    # Dispatch commands
    if args.command == "greet":
        add_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
