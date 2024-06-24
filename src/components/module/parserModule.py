
from components.parser.expressions.additionExpression import AdditiveExpression
from components.parser.expressions.index import Expression
from components.parser.expressions.literalExcutor import LiteralExcutor
from components.parser.expressions.literals.paranthesisLiteral import CloseParanthesis, OpenParanthesis
from components.parser.expressions.multiplicationExpression import MultiplicativeExpression
from components.parser.expressions.literals.numberExpression import NumberExpression
from components.parser.expressions.literals.operatorExpression import OperatorExpression
from components.parser.expressions.paranthesisedExpression import ParanthesisedExpression
from components.parser.expressions.primaryExpression import PrimaryExpression
from components.tokenizer.index import Tokenizer
from components.parser.tokenExcutor import TokenExcutor
from components.constants.regexSpec import Spec
from components.parser.index import Parser
from ..parser.expressions.literals.variableExpresssion import VariableExpression
from components.parser.exprTree import ExprTree
from components.parser.expressionList import ExpressionList
from components.parser.expressions.literals.index import Literals

class Module:
    
    
    _tokenizer = None
    _token_executor = None
    _parser = None
    _expr_tree = None
    _expression_list = None
    _variable_expression = None
    _number_expression = None
    _literal = None
    _operator_expression = None
    _addition_expression = None
    _subtraction_expression=None
    _expression = None
    _multiplication_expression = None
    _division_expression = None
    _paranthesis_expression = None
    _literal_excutor = None
    _primary_expression = None
    _open_paranthesis = None
    _close_paranthesis = None
    _paranthesised_expression = None
    

    @classmethod
    def get_tokenizer(cls):
        if cls._tokenizer == None:
            cls._tokenizer = Tokenizer(Spec)
        return cls._tokenizer
    
    @classmethod    
    def get_token_executor(cls):
        if  cls._token_executor == None:
            cls._token_executor = TokenExcutor(cls.get_tokenizer())
        return cls._token_executor
    
    @classmethod
    def get_expr_tree(cls):
        if cls._expr_tree == None:
            cls._expr_tree = ExprTree(cls.get_expression_list())
        return cls._expr_tree
    
    @classmethod
    def get_expression_list(cls):
        if cls._expression_list == None:
            cls._expression_list = ExpressionList(cls.get_token_executor())
        return cls._expression_list
    
    @classmethod
    def get_literal_excutor(cls):
        if cls._literal_excutor == None:
            cls._literal_excutor = LiteralExcutor(cls.get_expression_list())
        return cls._literal_excutor
    
    @classmethod
    def get_expression(cls):
        if cls._expression == None:
            cls._expression = Expression(cls.get_literal_excutor())
        return cls._expression
    
    @classmethod
    def get_additive_expression(cls):
        if cls._addition_expression == None:
            cls._addition_expression = AdditiveExpression(cls.get_literal_excutor())
        return cls._addition_expression
    
    @classmethod
    def get_multiplicative_expression(cls):
        if cls._multiplication_expression == None:
           cls._multiplication_expression = MultiplicativeExpression(cls.get_literal_excutor())
        return cls._multiplication_expression
    
    @classmethod
    def get_primary_expression(cls):
        if cls._primary_expression == None:
           cls._primary_expression = PrimaryExpression(cls.get_literal_excutor())
        return cls._primary_expression
    
    @classmethod
    def get_literal(cls):
        if cls._literal == None:
            cls._literal = Literals(cls.get_token_executor())
        return cls._literal
    
    @classmethod
    def get_variable_expression(cls):
        if cls._variable_expression == None:
            cls._variable_expression = VariableExpression(cls.get_token_executor())
        return cls._variable_expression
    
    @classmethod
    def get_number_expression(cls):
        if cls._number_expression == None:
            cls._number_expression = NumberExpression(cls.get_token_executor())
        return cls._number_expression
    
    @classmethod
    def get_open_paranthesis(cls):
        if cls._open_paranthesis == None:
            cls._open_paranthesis = OpenParanthesis(cls.get_token_executor())
        return cls._open_paranthesis
    
    @classmethod
    def get_close_paranthesis(cls):
        if cls._close_paranthesis == None:
            cls._close_paranthesis = CloseParanthesis(cls.get_token_executor())
        return cls._close_paranthesis
    
    @classmethod
    def get_paranthesised_expression(cls):
        if cls._paranthesised_expression == None:
            cls._paranthesised_expression = ParanthesisedExpression(cls.get_token_executor())
        return cls._paranthesised_expression
    
    @classmethod
    def get_operator_expression(cls):
        if cls._operator_expression == None:
            cls._operator_expression = OperatorExpression(cls.get_token_executor())
        return cls._operator_expression
    
    @classmethod
    def get_parser(cls):
        if cls._parser == None:
            cls._parser = Parser(
                cls.get_tokenizer(),
                cls.get_token_executor(),
                cls.get_expr_tree(),
            )
        return cls._parser
