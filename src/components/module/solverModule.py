

from components.constants.TreeType import TreeType
from components.solver.expressions.binaryExpression import BinaryExpression
from components.solver.expressions.expTree import ExpTree
from components.solver.expressions.numberLiteral import NumberLiteral
from components.solver.expressions.variableLiteral import VariableLiteral


class SolverModule:
    
    crawlingPath = {
        TreeType.EXPR_TREE : ExpTree(),
        TreeType.BINARY_EXPRESSION : BinaryExpression(),
        TreeType.NUMBER_Literal: NumberLiteral(),
        TreeType.VARIABLE_Literal: VariableLiteral(),
    }
    
    @classmethod
    def get_crawler(cls,nodeType):
        crawler = cls.crawlingPath[nodeType]
        if  crawler == None:
            raise Exception("NodeType is not found.")
        
        return crawler