import mot_read as mr
import os

class Lit_class():
    current_PT = 1
    last_index = 0
    Directory = os.path.dirname(__file__)
    LT_path= os.path.join(Directory, 'Lit.txt')
    PT_path = os.path.join(Directory, 'PT.txt')
    
    def __init__(self) -> None:
        self.__file_create()
        
    def __file_create(self):

        open(self.LT_path, 'w')
        open(self.PT_path, 'w')
        
    def get_literal(self, int_value : int) -> int:
        # input Literal value
        # return index of literal value
        self.last_index = self._LT_append(self, int_value)
        return self.last_index
       
    
    def ltorg(self, LC_value : int) -> int:
        for i in range(self.current_PT , self.last_index +1):
            self._LT_update(i, LC_value)
            LC_value += 1
        
        self.current_PT = self.last_index + 1
        return LC_value
    
    def _pool_add(self) -> int:
        with open(self.PT_path, 'a') as PT:
            PT.write(str(self.current_PT) + '\n')
            
    def _LT_update(self, index : int , LC : int ):
        LTr = open(self.LT_path, 'r')
        LTLines = LTr.readlines()
        for line_no , line in enumerate(LTLines):
            if line_no + 1 == index:
                LTLines[line_no] = '{} {}\n'.format(LTLines[line_no], LC)
        LTr.close()
        
        with open(self.LT_path, 'w') as LTw:
            for line in LTLines:
                LTw.write(line)
    def _LT_append(self, Literal_value : int):
        with open(self.LT_path, 'a') as LTa:
            LTa.write('{}\n'.format(Literal_value))
        with open(self.LT_path, 'r') as LTa:
            for line_no , line in enumerate(LTa):
                    return line_no+1
        
        