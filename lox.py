import sys
from scanner import Scanner
from pprint import pprint


# TODO: use click?
def main():
    args = sys.argv
    if len(args) > 2:
        print('Usage: plox [script]')
        sys.exit(64)
    elif len(args) == 2:
        run_file(args[1])
    else:
        repl()

def repl():
    while True:
        print('> ', end='')

        try:
            line = input()
        except EOFError:
            sys.exit()

        if not line:
            break

        run(line)

def run(code: str):
    pprint(Scanner.tokenize(code))

def run_file(path: str):
    with open(path) as file:
        run(file.read())



if __name__ ==  "__main__":
    main()
