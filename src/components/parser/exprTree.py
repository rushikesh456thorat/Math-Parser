from components.types.treeNode import TreeNode
from ..constants.TreeType import TreeType 

class ExprTree:
    def __init__(self,expressionList):
        self._exprList = expressionList
        
        
    def get_expr_tree(self):
        
        return TreeNode(
            type = TreeType.EXPR_TREE,
            body = self._exprList.get_expression_list()
        )
        