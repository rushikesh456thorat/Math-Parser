class TokenExcutor:
    def __init__(self,tokenizer) :
        self._tokenizer = tokenizer
        self._lookahead = None
    
    def eat_and_lookahead(self,tokenType):
        token = self._lookahead
        
        if token.tokenType != tokenType:
            raise Exception(f"Unexpected token {token.value}. Expected token type {tokenType}.") 
        
        if token.tokenType == None:
            raise Exception(f"Unexpected end of input, expected : {tokenType}")
        
        
        self.set_lookahead(self._tokenizer.get_next_tokens())
        return token
    
    def get_lookahead(self):
        return self._lookahead
    
    def set_lookahead(self,token):
        self._lookahead = token