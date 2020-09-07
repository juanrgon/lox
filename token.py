import attr
from typing import Any, List
from collections import deque

from token_type import TokenType


@attr.s(auto_attribs=True, kw_only=True)
class Token:
    token_type: TokenType
    lexeme: str
    literal: Any
    line: int


@attr.s(auto_attribs=True, kw_only=True)
class Scanner:
    """
        <- start = 0
    a
    b
    c
        <- end = 2
    d
    e
    f

    advance() increments "end" by 1
    retreat() decrements "end" by 1

    lexeme() returns the current lexeme
    consume() returns the current lexeme and advances "start" and "end" by its length
    """

    source: str
    start: int = 0
    end: int = 1

    @classmethod
    def tokenize(cls, text: str) -> List["Token"]:
        tokens = []
        scanner = Scanner(source=text)

        single_char_tokens = {
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "{": TokenType.LEFT_BRACE,
            "}": TokenType.RIGHT_BRACE,
            ",": TokenType.COMMA,
            ".": TokenType.DOT,
            "-": TokenType.MINUS,
            "+": TokenType.PLUS,
            ";": TokenType.SEMICOLON,
            "*": TokenType.STAR,
        }

        line = 1
        while not scanner.at_end():
            token_type = None
            literal = None

            if scanner.lexeme() == "\n":
                line += 1

            elif scanner.lexeme() in ('\r', '\t', ' '):
                pass

            elif scanner.lexeme() in single_char_tokens:
                token_type = single_char_tokens[scanner.lexeme()]

            elif scanner.lexeme().startswith("!"):
                if scanner.match("="):
                    token_type = TokenType.BANG_EQUAL
                else:
                    token_type = TokenType.BANG

            elif scanner.lexeme().startswith("="):
                if scanner.match("="):
                    token_type = TokenType.EQUAL_EQUAL
                else:
                    token_type = TokenType.EQUAL

            elif scanner.lexeme().startswith(">"):
                if scanner.match("="):
                    token_type = TokenType.GREATER_EQUAL
                else:
                    token_type = TokenType.GREATER

            elif scanner.lexeme().startswith("<"):
                if scanner.match("="):
                    token_type = TokenType.LESS_EQUAL
                else:
                    token_type = TokenType.LESS

            lexeme = scanner.consume()

            if token_type:
                tokens.append(
                    Token(token_type=token_type, lexeme=lexeme, line=line, literal=literal)
                )

        return tokens

    def advance(self, amount: int = 1):
        self.end += amount

    def consume(self) -> str:
        lexeme = self.lexeme()
        self.start, self.end = self.end, self.end + 1
        return lexeme

    def lexeme(self) -> str:
        return self.source[self.start : self.end]

    def lookahead(self, count=1) -> str:
        return self.source[self.end : (self.end + count)]

    def match(self, target: str) -> bool:
        if self.source[self.end : (self.end + len(target))] != target:
            return False

        self.advance(len(target))
        return True

    def retreat(self):
        self.end -= 1

    def at_end(self) -> bool:
        return self.end > len(self.source)


from pprint import pprint
source = """
( != )
 <= >=
 = ==

"""
pprint(Scanner.tokenize(source))
