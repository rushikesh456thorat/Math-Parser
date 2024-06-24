import re

class TokenType:
    NULL_TYPE = None
    NUMBER_LITERAL = "number"
    ADDITION_OPERATOR_TYPE = "+"
    MULTIPLICATION_OPERATOR_TYPE = "*"
    VARIABLE_TYPE = "variable"
    EQUALITY_TYPE = "="
    OPEN_PARANTHESIS_TYPE = "("
    CLOSE_PARANTHESIS_TYPE = ")"
    POWER_OPERATOR_TYPE = "^"
    

Spec = [
     {"regex": re.compile(r"^\s+"), "token_type": TokenType.NULL_TYPE},
     {"regex": re.compile(r"^(?:(?:[\d]*[.])?[\d]+)?x(?:\^[+-]?(?:[\d]*[.])?[\d]+)?"), "token_type": TokenType.VARIABLE_TYPE},
     {"regex": re.compile(r"^([\d]*[.])?[\d]+"), "token_type": TokenType.NUMBER_LITERAL},
     {"regex": re.compile(r"^[+\-]"), "token_type": TokenType.ADDITION_OPERATOR_TYPE},
     {"regex": re.compile(r"^[*\/]"), "token_type": TokenType.MULTIPLICATION_OPERATOR_TYPE},
     {"regex": re.compile(r"^\^"), "token_type": TokenType.POWER_OPERATOR_TYPE},
     {"regex": re.compile(r"^\="), "token_type": TokenType.EQUALITY_TYPE},
     {"regex": re.compile(r"^\("), "token_type": TokenType.OPEN_PARANTHESIS_TYPE},
     {"regex": re.compile(r"^\)"), "token_type": TokenType.CLOSE_PARANTHESIS_TYPE},
         
]