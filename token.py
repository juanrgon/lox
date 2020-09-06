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

    @classmethod
    def tokenize(cls, text: str) -> List["Token"]:
        tokens = []
        lexeme = ""
        text = deque(text)

        while text:
            lexeme += text.popleft()
            token_type = TokenType.match(lexeme)
            if token_type is not None:
                tokens.append(Token(token_type=token_type, lexeme=lexeme, line=1))


@attr.s(auto_attribs=True, kw_only=True)
class Tokenizer:
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
    end: int = 0

    def advance(self):
        self.end += 1

    def consume(self) -> str:
        lexeme = self.lexeme()
        self.start, self.end = self.end, (2 * self.end - self.start)
        return lexeme

    def lexeme(self) -> str:
        return self.source[self.start: self.end]

    def retreat(self):
        self.end -= 1
