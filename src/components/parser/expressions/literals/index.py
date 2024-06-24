from ....module import parserModule
from components.constants.regexSpec import TokenType



class Literals:
    def __init__(self,tokenExcutor) -> None:
        self._tokenExcutor = tokenExcutor
        
    def get_literal_impl(self):
        lookahead = self._tokenExcutor.get_lookahead()
        match lookahead.tokenType:
            case TokenType.VARIABLE_TYPE:
                return parserModule.Module.get_variable_expression().get_literal()
            case TokenType.NUMBER_LITERAL:
                return parserModule.Module.get_number_expression().get_literal()
            case TokenType.ADDITION_OPERATOR_TYPE | TokenType.MULTIPLICATION_OPERATOR_TYPE:
                return parserModule.Module.get_operator_expression().get_literal()
            case TokenType.OPEN_PARANTHESIS_TYPE:
                return parserModule.Module.get_open_paranthesis().get_literal()
            case TokenType.CLOSE_PARANTHESIS_TYPE:
                return parserModule.Module.get_close_paranthesis().get_literal()
                