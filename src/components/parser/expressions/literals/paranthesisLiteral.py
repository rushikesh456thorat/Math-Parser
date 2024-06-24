
from components.constants.TreeType import TreeType
from components.parser.expressions.literals.index import Literals
from components.types.treeNode import TreeNode


class OpenParanthesis(Literals):
    def get_literal(self):
        token = self._tokenExcutor.eat_and_lookahead(self._tokenExcutor.get_lookahead().tokenType)
        
        if not token.value :
            raise Exception("Token doesn't have value")
        
        return TreeNode(type=TreeType.OPEN_PARANTHESIS_Literal)
    
class CloseParanthesis(Literals):
    def get_literal(self):
        token = self._tokenExcutor.eat_and_lookahead(self._tokenExcutor.get_lookahead().tokenType)
        
        if not token.value :
            raise Exception("Token doesn't have value")
        
        return TreeNode(type=TreeType.CLOSE_PARANTHESIS_Literal)