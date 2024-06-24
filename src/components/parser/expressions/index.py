from components import module
from components.constants.TreeType import TreeType
from components.types.treeNode import TreeNode


class Expression:
    def __init__(self,literalExcutor) -> None:
        self._literalExcutor = literalExcutor
    
    def get_expression_impl(self,treeType = TreeType):
        match treeType:
            case TreeType.ADDITION_EXPRESSION:
                return module.Module.get_additive_expression()
            case TreeType.MULTIPLICATION_EXPRESSION:
                return module.Module.get_multiplicative_expression()
            case TreeType.PRIMARY_EXPRESSION:
                return module.Module.get_primary_expression()
            case TreeType.PARANTHESISED_EXPRESSION:
                return module.Module.get_paranthesised_expression()
                
   
       
    def get_binary_expression(self,nodeType = TreeType, operator = str):
        return self.get_expression(TreeType.BINARY_EXPRESSION,operator,nodeType)
    
    def get_expression(self,expType = TreeType,operator = str,tempNodeType = TreeType):
        _left = self.get_expression_impl(tempNodeType)._expression()
        
        while getattr(self._literalExcutor.get_lookahead(), 'value', 'Not found') == operator:
            _op = self._literalExcutor.eat_and_lookahead(TreeType.OPERATOR_Literal).value
            _right = self.get_expression_impl(tempNodeType)._expression()
            
            _left = TreeNode(
                type = expType,
                operator = _op,
                left = _left,
                right = _right
            )
            
        return _left
        
    
    