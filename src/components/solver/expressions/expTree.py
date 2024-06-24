
from components.module import solverModule
from components.solver.expressions.crawler import Crawler


class ExpTree(Crawler):
    def _crawler(self, node=...):
        if not node.body:
            raise Exception("Body not found...!")
        
        return solverModule.SolverModule.get_crawler(node.body.type)._crawler(node.body)