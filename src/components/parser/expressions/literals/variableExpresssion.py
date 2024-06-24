import re
from components.constants.TreeType import TreeType
from components.constants.regexSpec import TokenType
from .index import Literals
from components.types.treeNode import TreeNode


class VariableExpression(Literals):
    
    def get_literal(self):
        token = self._tokenExcutor.eat_and_lookahead(TokenType.VARIABLE_TYPE)

        if not token.value :
            raise Exception("Wrong type declaration for VariableExpression")

        coefficent_match = re.match(r"^([\d]*[.])?[\d]+", token.value[0:])
        coefficent = float(coefficent_match.group()) if coefficent_match else 1.0

        power_match = re.match(r"^([\d]*[.])?[\d]+", token.value[(len(coefficent_match.group())+2):] 
                               if coefficent_match else token.value[2:])
        power = float(power_match.group()) if power_match else 1.0

        variable = TreeNode(type=TreeType.VARIABLE_Literal, coefficent = coefficent,power = power)
        return  variable