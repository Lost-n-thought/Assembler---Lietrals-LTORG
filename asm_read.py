import os
import mot_read as mr
import re

class asm():
    def __init__(self) -> None:
        self.asm_field = ['Mnemonics', 'Operand1', 'Operand2']
        self.registers = ['AREG', 'BREG', 'CREG', 'DREG']
        
    def __get_asm_file(self):
        Directory = os.path.dirname(__file__)
        asm_path= os.path.join(Directory, 'sampleAssembly.asm')
        asm_file = open(asm_path, 'r')
        return asm_file
    
    def _get_asm_dict(self):
        for line in self.__get_asm_file():
            line = line.rstrip().split('\t')
            yield dict(zip(self.asm_field, line))
            
    def _is_register(self, word):
        if word in self.registers:
            return True
        else:
            return False   
    def _is_mnemonics(self, word : str):
        mot_class1 = mr.mot_class()
        return mot_class1.is_Mnemonics(word)
    def _is_literal(self, word : str):
        if re.match("='\d+'", word):
            return True
        else:
            return False
    
    def _is_valid_operand(self, word : str):
        if ((self._is_register(word) or self._is_literal(word)) and not self._is_mnemonics(word)):
            return True
        else:
            return False


# a = asm()
# print(a._is_literal("='0'"))
# print(a._is_register("REG"))
# print(a._is_mnemonics("ADD"))
# print(a._is_valid_operand("ADD"))
# print(a._is_valid_operand("AREG"))
