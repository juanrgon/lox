import attr
from .expression import Expression
from scanner.token import Token


@attr.s(auto_attribs=True, kw_only=True)
class Unary(Expression):
    operator: Token
    right: Expression
