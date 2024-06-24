from components.constants.TreeType import TreeType
from components.constants.regexSpec import TokenType
from .index import Literals
from components.types.treeNode import TreeNode


class OperatorExpression(Literals):
    def get_literal(self):
        token = self._tokenExcutor.eat_and_lookahead(self._tokenExcutor.get_lookahead().tokenType)
        
        if not token.value :
            raise Exception("Token doesn't have value")
        
        operator = TreeNode(type=TreeType.OPERATOR_Literal,value = token.value)
        return  operator
    