from components.constants.TreeType import TreeType
from components.constants.regexSpec import TokenType
from .index import Literals
from components.types.treeNode import TreeNode


class NumberExpression(Literals):
    
    def get_literal(self):
        token = self._tokenExcutor.eat_and_lookahead(TokenType.NUMBER_LITERAL)

        if not token.value :
            raise Exception("Token doesn't have value")


        number = TreeNode(type=TreeType.NUMBER_Literal,value = token.value)
        return  number
    
