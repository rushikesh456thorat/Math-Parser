

from components.constants.TreeType import TreeType
from components.types.treeNode import TreeNode


def _is_both_number_operands(left,right):
    return (left.type == TreeType.NUMBER_Literal) & (right.type == TreeType.NUMBER_Literal)

def _is_both_variable_operands(left,right):
    return (left.type == TreeType.VARIABLE_Literal) & (right.type == TreeType.VARIABLE_Literal)

def _is_both_have_same_power(left,right):
     try:
         return (left.power == right.power) 
     except AttributeError:
         return False 

     
def _is_var_and_number_operands(left,right):
    return (left.type == TreeType.VARIABLE_Literal) & (right.type == TreeType.NUMBER_Literal) | (left.type == TreeType.NUMBER_Literal) & (right.type == TreeType.VARIABLE_Literal)
    
def __do__operation__(left,right,operator):
    if not left or not right or not operator:
        raise Exception("Invalid tree!")
    
    match operator:
        case "+":
            if _is_both_number_operands(left,right):
                return  TreeNode (type=TreeType.NUMBER_Literal,value = str(float(left.value) + float(right.value)))
            elif _is_both_variable_operands(left,right) & _is_both_have_same_power(left,right):
                coe = str(float(left.coefficent) + float(right.coefficent))
                return TreeNode(type=TreeType.VARIABLE_Literal, coefficent =coe, power = left.power)
            else:
                return TreeNode(type=TreeType.BINARY_EXPRESSION, operator = operator,left = left, right = right)
            
        case "-":
            if _is_both_number_operands(left,right):
                return  TreeNode (type=TreeType.NUMBER_Literal,value = str(float(left.value) - float(right.value)))
            elif _is_both_variable_operands(left,right) & _is_both_have_same_power(left,right):
                coe = str(float(left.coefficent) - float(right.coefficent))
                return TreeNode(type=TreeType.VARIABLE_Literal, coefficent =coe, power = left.power)
            else:
                return TreeNode(type=TreeType.BINARY_EXPRESSION, operator =operator,left = left, right =right)
            
        case "*":
            if _is_both_number_operands(left,right):
                return  TreeNode (type=TreeType.NUMBER_Literal,value = str(float(left.value) * float(right.value)))
            elif _is_both_variable_operands(left,right):
                pow = str(float(left.power) + float(right.power))
                coe = str(float(left.coefficent) * float(right.coefficent))
                return TreeNode(type=TreeType.VARIABLE_Literal, coefficent = coe, power = pow)
            else:
                return TreeNode(type=TreeType.BINARY_EXPRESSION, operator = operator,left = left, right = right)
        
        case "/":
            if _is_both_number_operands(left,right):
                return  TreeNode (type=TreeType.NUMBER_Literal,value = str(float(left.value) / float(right.value)))
            elif _is_both_variable_operands(left,right) & _is_both_have_same_power(left,right):
                pow = str(float(left.power) - float(right.power))
                coe = str(float(left.coefficent) / float(right.coefficent))
                return TreeNode(type=TreeType.VARIABLE_Literal, coefficent = coe, power = pow)
            else:
                return TreeNode(type=TreeType.BINARY_EXPRESSION, operator =operator,left = left, right =right)