from enum import Enum, auto
from typing import Optional


class TokenType(str, Enum):

    # Single-character tokens.
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    # One or two character tokens.
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Literals.
    IDENTIFIER = auto()
    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()

    # Keywords.
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUNC = auto()
    FOR = auto()
    IF = auto()
    NONE = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    SELF = auto()
    TRUE = auto()
    LET = auto()
    WHILE = auto()

    EOF = auto()

    @classmethod
    def match_keyword(cls, lexeme: str) -> Optional["TokenType"]:
        return {
            "and": cls.AND,
            "class": cls.CLASS,
            "else": cls.ELSE,
            "False": cls.FALSE,
            "func": cls.FUNC,
            "for": cls.FOR,
            "if": cls.IF,
            "None": cls.NONE,
            "or": cls.OR,
            "print": cls.PRINT,
            "return": cls.RETURN,
            "super": cls.SUPER,
            "self": cls.SELF,
            "True": cls.TRUE,
            "let": cls.LET,
            "while": cls.WHILE,
        }.get(lexeme)

    def _generate_next_value_(name: str, start, count, last_values) -> str:  # noqa
        return name
