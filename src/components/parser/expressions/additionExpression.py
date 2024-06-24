

from components import module
from components.constants.TreeType import TreeType
from components.parser.expressions.index import Expression
from components.types.treeNode import TreeNode


class AdditiveExpression(Expression):
      def _expression(self)->TreeNode:
            return self.get_binary_expression(
                TreeType.MULTIPLICATION_EXPRESSION,
                "+"
            )