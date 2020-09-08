import attr
from typing import List, Optional, Union
from .exceptions import SyntaxException

from .token_type import TokenType


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
            "/": TokenType.SLASH,
        }

        line = 1
        while not scanner.at_end():
            token_type = None
            literal: Optional[Union[str, int, float]] = None

            if scanner.lexeme() == "\n":
                line += 1

            elif scanner.lexeme() in ("\r", "\t", " "):
                pass

            elif scanner.lexeme() == "#":
                while scanner.lookahead() != "\n":
                    scanner.advance()

            elif scanner.lexeme() in single_char_tokens:
                token_type = single_char_tokens[scanner.lexeme()]

            elif scanner.lexeme() == "!":
                if scanner.match("="):
                    token_type = TokenType.BANG_EQUAL
                else:
                    token_type = TokenType.BANG

            elif scanner.lexeme() == "=":
                if scanner.match("="):
                    token_type = TokenType.EQUAL_EQUAL
                else:
                    token_type = TokenType.EQUAL

            elif scanner.lexeme() == ">":
                if scanner.match("="):
                    token_type = TokenType.GREATER_EQUAL
                else:
                    token_type = TokenType.GREATER

            elif scanner.lexeme() == "<":
                if scanner.match("="):
                    token_type = TokenType.LESS_EQUAL
                else:
                    token_type = TokenType.LESS

            elif scanner.lexeme() in ('"', "'"):
                quote = scanner.lexeme()
                token_type = TokenType.STRING
                while not scanner.match(quote):
                    if scanner.at_end() or scanner.lookahead() == "\n":
                        raise SyntaxException(f"Expected {quote}")

                    scanner.advance()
                    continue
                literal = scanner.lexeme()[1:-1]

            elif cls._is_digit(scanner.lexeme()):
                token_type = TokenType.INTEGER
                while cls._is_digit(scanner.lookahead()):
                    scanner.advance()

                literal = int(scanner.lexeme())

                if scanner.match("."):
                    token_type = TokenType.FLOAT
                    while cls._is_digit(scanner.lookahead()):
                        scanner.advance()
                    literal = float(scanner.lexeme())

            elif cls._is_alpha(scanner.lexeme()):
                token_type = TokenType.IDENTIFIER

                while cls._is_alpha_numeric(scanner.lookahead()):
                    scanner.advance()

                keyword = TokenType.match_keyword(scanner.lexeme())
                if keyword:
                    token_type = keyword

            lexeme = scanner.consume()

            if token_type:
                tokens.append(
                    Token(
                        token_type=token_type, lexeme=lexeme, line=line, literal=literal
                    )
                )
            elif lexeme[0] in ("\n", "\t", "\r", "#", " "):
                pass
            else:
                raise SyntaxException(f"Syntax Error on line {line}: '{lexeme}'")

        tokens.append(Token(token_type=TokenType.EOF, lexeme="", line=line))

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

    @classmethod
    def _is_digit(cls, char: str) -> bool:
        return "0" <= char <= "9"

    @classmethod
    def _is_alpha(cls, char: str) -> bool:
        return ("a" <= char <= "z") or ("A" <= char <= "Z") or char == "_"

    @classmethod
    def _is_alpha_numeric(cls, char: str) -> bool:
        return cls._is_alpha(char) or cls._is_digit(char)
