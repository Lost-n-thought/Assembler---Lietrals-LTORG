import mot_read as mr
import Literal as ltP
import asm_read as ar


def LC_processing(final_asm_file_gen):
    m_file = mr.mot()
    ar_class = ar.asm()
    LC = 0
    LT = ltP.Lit()
    
    for asm_dict_list in final_asm_file_gen:
        asm_dict_list[0]['LC'] = asm_dict_list[0].get('LC')
        asm_dict_list[0]['MnemonicsIC'] = asm_dict_list[0].get('MnemonicsIC')
        asm_dict_list[0]['Operand1IC'] = asm_dict_list[0].get('Operand1IC')
        asm_dict_list[0]['Operand2IC'] = asm_dict_list[0].get('Operand2IC')
        
        asm_dict_list[0]['LC'] = LC
        if asm_dict_list[1]['Mnemonics'] in ['LTORG',"END"]:
            LC = LT.ltorg(LC)
        else:
            LC = LC + int(m_file.get_attributes(asm_dict_list[1]['Mnemonics']))
               
        Mn_type = m_file.get_attributes(asm_dict_list[1]['Mnemonics'] , 'Type')
        Mn_type_id = m_file.get_attributes(asm_dict_list[1]['Mnemonics'] , 'Type_id')
        asm_dict_list[0]['MnemonicsIC'] = "({} {})".format(Mn_type, Mn_type_id)
        
        for op in ['Operand1','Operand2']:
            if asm_dict_list[1][op] is not None:
                opIC = op+"IC"
                if ar_class._is_literal(asm_dict_list[1][op]):
                    lit_value = ar_class.literal_value(asm_dict_list[1][op])
                    op1 = "(s,{})".format(LT.get_literal(lit_value))
                    asm_dict_list[0][opIC]
                else:
                    op1 = "(r,{})".format(ar_class.registers.index(asm_dict_list[1][op]))   
                    asm_dict_list[0][opIC] = op1
        
        yield asm_dict_list
    

