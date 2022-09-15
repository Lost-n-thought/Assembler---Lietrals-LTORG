import mot_read as mr
import Literal as lt
import asm_read as ar

m_file = mr.mot()
ar_class = ar.asm()
final_asm_file_gen = ar_class.final_asm_file_gen()
LC = 0
LT = lt.Lit_class()
def LC_processing():
    
    for asm_dict_list in final_asm_file_gen:
        asm_dict_list[0].get('LC')
        asm_dict_list[0].get('MnemonicsIC')
        asm_dict_list[0].get('Operand1IC')
        asm_dict_list[0].get('Operand2IC')
        asm_dict_list[0]['LC'] = LC
        if asm_dict_list[1]['Mnemonics'] in ['LTORG',"END"]:
            LC = LT.ltorg(LC)
            
        Mn_type = m_file.get_attributes(asm_dict_list[1]['Mnemonics'] , 'Type')
        Mn_type_id = m_file.get_attributes(asm_dict_list[1]['Mnemonics'] , 'Type_id')
        asm_dict_list[0]['MnemonicsIC'] = "({} {})".format(Mn_type, Mn_type_id)
        
        if ar_class._is_literal(asm_dict_list[1]['Operand1']):
            lit_value = ar_class.literal_value(asm_dict_list[1]['Operand1'])
            op1 = "(s,{})".format(LT.get_literal(lit_value))
            asm_dict_list[0]['Operand1IC']
        else:
            op1 = "(r,{})".format(ar_class.registers.index(asm_dict_list[1]['Operand1']))   
            asm_dict_list[0]['Operand1IC'] = op1
        
        if ar_class._is_literal(asm_dict_list[1]['Operand2']):
            lit_value = ar_class.literal_value(asm_dict_list[1]['Operand2'])
            op2 = "(s,{})".format(LT.get_literal(lit_value))
            asm_dict_list[0]['Operand2IC']
        else:
            op2 = "(r,{})".format(ar_class.registers.index(asm_dict_list[1]['Operand1']))   
            asm_dict_list[0]['Operand2IC'] = op2
    yield asm_dict_list
    
for i in LC_processing():
    print(i)
