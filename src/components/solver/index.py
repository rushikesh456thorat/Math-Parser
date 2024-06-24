

from components.module import solverModule
from components.parser.index import Parser


class Solver:
    def __init__(self,parser = Parser) -> None:
        self._parser = parser
        
    def solve(self,expression):
        tree = self._parser.parser(expression)
        s = solverModule.SolverModule()
        return s.get_crawler(tree.type)._crawler(tree)