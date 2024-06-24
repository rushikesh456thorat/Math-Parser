
class Parser:
    def __init__(self,tokenizer,tokenExcutor,exprTree):
        self._tokenizer = tokenizer
        self._tokenExcutor = tokenExcutor
        self._exprTree = exprTree
        self._mathString = ""
        
    def parser(self,mathString):
        self._mathString = mathString
        self._tokenizer.init_tokenizer(self._mathString)
        self._tokenExcutor.set_lookahead(self._tokenizer.get_next_tokens())
        return self._exprTree.get_expr_tree()
        
        
        
        
    