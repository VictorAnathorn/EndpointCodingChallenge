import sys
import argparse
from src.filesystem import FileSystem

def main(args):

    def proccess_input(input_path, output_path):
        with open(input_path, 'r') as f:
            commands = f.readlines()

        # Redirect stdout to the output file if specified
        if output_path:
            sys.stdout = open(output_path, 'w')

        for command in commands:
            command = command.strip()
            if not command:
                continue
            fs.execute_command(command)

        # Close the output file if we opened it earlier
        if output_path:
            sys.stdout.close()

    fs = FileSystem()

    if args.default:
        proccess_input('verification-input.txt', 'verification-output.txt')
    elif args.input:
        proccess_input(args.input, args.output if args.output else None)
    else:
        print("Enter your commands. Enter empty string to end input:")
        commands = []
        for line in sys.stdin:
            command = line.strip()
            if not command:
                break
            commands.append(command)
        for command in commands:
            fs.execute_command(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Directory Management System')
    parser.add_argument('--default', action='store_true', help='Use the default command list from verification-input.txt and write output in verification-output.txt')
    parser.add_argument('--input', type=str, help='Specify an input file path')
    parser.add_argument('--output', type=str, default="output.txt", help='Specify an output file path (Only works with --default or when --input is present)')
    args = parser.parse_args()
    main(args)
