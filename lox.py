import sys
from scanner import Scanner, SyntaxException
from pprint import pprint
from repl import repl
from run_file import run_file


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

if __name__ ==  "__main__":
    main()
