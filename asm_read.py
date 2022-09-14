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
    
    def _get_asm_dict_list_gen(self) -> dict:
        for line_no, line in enumerate(self.__get_asm_file()):
            line = line.rstrip().split('\t')
            properties_dict = {'line_number': line_no}
            line_dict = dict(zip(self.asm_field, line))
            line_dict.get('Operand1')
            line_dict.get('Operand2')
            #dicto
            yield [properties_dict ,line_dict]
            
            
            
            
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
    def literal_value(str : str):
        num_str = str.strip("'=")
        return int(num_str)
    
    def _is_valid_operand(self, word : str):
        if ((self._is_register(word) or self._is_literal(word)) and not self._is_mnemonics(word)):
            return True
        else:
            return False
        
    def _is_valid_line_dict_list(self, line_dict_list : dict):
            if(not self._is_mnemonics(line_dict_list[1]['Mnemonics'])):
                raise Exception('Invalid Mnemonics in line number {}'.format(line_dict_list[0]['line_number']))
            if(not self._is_valid_operand(line_dict_list[1]['Operand1'])):
                raise Exception('Invalid Operand1 in line number {}'.format(line_dict_list[0]['line_number']))
            if(not self._is_valid_operand(line_dict_list[1]['Operand2'])):
                raise Exception('Invalid Operand2 in line number {}'.format(line_dict_list[0]['line_number']))
    
                       
    
    def final_asm_file_gen(self):
        for line_dict_list in self._get_asm_dict_list_gen():
            self._is_valid_line_dict_list(line_dict_list)
            yield line_dict_list


# a = asm()
# print(a._is_literal("='0'"))
# print(a._is_register("REG"))
# print(a._is_mnemonics("ADD"))
# print(a._is_valid_operand("ADD"))
# print(a._is_valid_operand("AREG"))
