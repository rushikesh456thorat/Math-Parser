
from ..helper.index import __do__operation__
from components.constants.TreeType import TreeType
from components.module import solverModule
from components.solver.expressions.crawler import Crawler


class BinaryExpression(Crawler):
      def _crawler(self, node=...):
            left = solverModule.SolverModule.get_crawler(node.left.type)._crawler(node.left)
            right = solverModule.SolverModule.get_crawler(node.right.type)._crawler(node.right)
            print (node.operator)
            operationValue = __do__operation__(left,right,node.operator)
           
            return operationValue