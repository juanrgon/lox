import attr
from .expression import Expression
from scanner.token import Token
from typing import Union


@attr.s(auto_attribs=True, kw_only=True)
class Literal(Expression):
    value: Union[str, int, float]
