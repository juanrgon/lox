import sys
from scanner import SyntaxException
from run import run
import sys


def repl():
    history = []

    while True:
        try:
            line = input(f"In [{len(history)}]: ")
            history.append(line)
        except EOFError:
            sys.exit()

        if not line:
            break

        try:
            run(line)
        except SyntaxException as e:
            print(e)
