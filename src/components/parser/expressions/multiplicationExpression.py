

from components.constants.TreeType import TreeType
from components.parser.expressions.index import Expression
from components.types.treeNode import TreeNode


class MultiplicativeExpression(Expression):
    def _expression(self)->TreeNode:
            return self.get_binary_expression(
                TreeType.PRIMARY_EXPRESSION,
                "*"
            )