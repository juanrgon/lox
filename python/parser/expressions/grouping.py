import attr
from .expression import Expression
from scanner.token import Token


@attr.s(auto_attribs=True, kw_only=True)
class Grouping(Expression):
    expression: Expression
