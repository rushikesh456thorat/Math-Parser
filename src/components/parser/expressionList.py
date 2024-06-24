from components.constants.TreeType import TreeType
from ..module import parserModule

class ExpressionList:
    def __init__(self,tokenExcutor) -> None:
        self._tokenExcutor = tokenExcutor
        self.expressionList = []
        
    
    def get_expression_list(self):
        while True:
            lookahead = self._tokenExcutor.get_lookahead()

            if lookahead is None:
                break

            expression = parserModule.Module.get_literal().get_literal_impl()
            self.expressionList.append(expression)

        
        return parserModule.Module.get_expression().get_expression_impl(TreeType.ADDITION_EXPRESSION)._expression()
