import re
from ..constants import regexSpec

class Tokenizer:
    def __init__(self,spec):
        self.spec = spec
        self._cursor = 0
    
    def init_tokenizer(self, expr):
        self.string = expr
        self._cursor = 0
        
    def has_tokens(self)->bool:
        if not self.string:
            return False
        return self._cursor < len(self.string)
    
    def get_next_tokens(self) :
        if not self.string:
            raise Exception("Tokenizer is not Initialized")
        
        if not self.has_tokens():
            return None
        
        string = self.string[self._cursor:]
        
        for spec in regexSpec.Spec:
            tokenValue = self._matched(spec["regex"],string)
            
            if not tokenValue:
                continue
            
            if spec["token_type"] == None:
                return Tokenizer.get_next_tokens()
            
            return Token(spec["token_type"],tokenValue)
            
        
        raise Exception(f"Unexpected token {string[0]}.")
            
            
    def _matched(self,regex,string):
        matched = re.match(regex,string)
        
        if not matched:
            return None
        
        self._cursor += len(matched[0])
        
        return matched[0]
    
class Token:
    def __init__(self,tokenType,value):
        self.value = value
        self.tokenType = tokenType
        
    def __str__(self) -> str:
         return f"Token[value={self.value}, tokenType={self.tokenType}]"

        