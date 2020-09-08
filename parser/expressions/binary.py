import attr
from .expression import Expression
from scanner.token import Token


@attr.s(auto_attribs=True, kw_only=True)
class Binary(Expression):
    left: Expression
    operator: Token
    right: Expression
