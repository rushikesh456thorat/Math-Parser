
from components import module
from components.constants.TreeType import TreeType
from components.parser.expressions.index import Expression
from components.types.treeNode import TreeNode


class ParanthesisedExpression(Expression):
    def _expression(self)->TreeNode:
            self._literalExcutor.eat_and_lookahead(TreeType.OPEN_PARANTHESIS_Literal)
            exp = self.get_expression_impl(TreeType.ADDITION_EXPRESSION)._expression()
            self._literalExcutor.eat_and_lookahead(TreeType.CLOSE_PARANTHESIS_Literal)
            
            return exp
                    
                    