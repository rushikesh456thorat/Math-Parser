# src/app.py

from components.module.parserModule import Module
from components.solver.index import Solver

ex = input("Enter your input: ")


module_instance = Module()
parser = module_instance.get_parser()

print(parser.parser(ex))

# below code not work because solver is incomplete

#sol = soln.solve(ex)
#sol.__str__()
#print(sol)
