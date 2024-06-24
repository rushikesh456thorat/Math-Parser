
from components import module
from components.constants.TreeType import TreeType
from components.parser.expressions.index import Expression
from components.types.treeNode import TreeNode


class PrimaryExpression(Expression):
    def _expression(self)->TreeNode:
            match self._literalExcutor.get_lookahead().type:
                case TreeType.NUMBER_Literal:
                    return self._literalExcutor.eat_and_lookahead(TreeType.NUMBER_Literal)
                case TreeType.VARIABLE_Literal:
                    return self._literalExcutor.eat_and_lookahead(TreeType.VARIABLE_Literal)
                case TreeType.OPEN_PARANTHESIS_Literal:
                    return self.get_expression_impl(TreeType.PARANTHESISED_EXPRESSION)
                    