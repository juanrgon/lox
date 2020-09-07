from enum import Enum, auto
from typing import List, Dict, Optional


class TokenType(str, Enum):
    def _generate_next_value_(name: str, start, count, last_values) -> str:  # noqa
        return name

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
    DEF = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    EOF = auto()

    @classmethod
    def match_keyword(cls, lexeme: str) -> Optional["TokenType"]:
        return {
            "and": cls.AND,
            "class": cls.CLASS,
            "else": cls.ELSE,
            "false": cls.FALSE,
            "def": cls.DEF,
            "for": cls.FOR,
            "if": cls.IF,
            "nil": cls.NIL,
            "or": cls.OR,
            "print": cls.PRINT,
            "return": cls.RETURN,
            "super": cls.SUPER,
            "this": cls.THIS,
            "true": cls.TRUE,
            "var": cls.VAR,
            "while": cls.WHILE,
        }.get(lexeme)
