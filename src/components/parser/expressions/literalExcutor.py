

class LiteralExcutor:
    def __init__(self,expressionList) -> None:
        self._expressionList = expressionList
        self.id = 0
        self.elementList = self._expressionList.expressionList
        self._lookahead = self.get_next_node()
    
    def get_next_node(self):
        if self.id <= len(self.elementList):
            element = self.elementList[self.id]
            self.id += 1
            return element
        
    def eat_and_lookahead(self,nodeType):
        node = self._lookahead
        
        if node.type != nodeType:
            raise Exception(f"Unexpected token {node.value}. Expected token type {nodeType}.") 
        
        if node.type == None:
            raise Exception(f"Unexpected end of input, expected : {nodeType}")
        
        if self.id < len(self.elementList):
          self._lookahead = self.get_next_node()
        return node
    
    def get_lookahead(self):
        return self._lookahead
    
    def set_lookahead(self,node):
        self._lookahead = node