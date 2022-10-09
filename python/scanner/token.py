import attr
from typing import Any
from .token_type import TokenType


@attr.s(auto_attribs=True, kw_only=True)
class Token:
    token_type: TokenType
    lexeme: str
    literal: Any = None
    line: int
