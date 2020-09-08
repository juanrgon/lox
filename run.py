from scanner import Scanner
from pprint import pprint


def run(code: str):
    pprint(Scanner.tokenize(code))
