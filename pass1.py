import asm_read as ar
import LC_processing as LCP
import os 


Directory = os.path.dirname(__file__)
IC_path= os.path.join(Directory, 'IC.txt')
with open(IC_path , 'w') as IC_file:
    pass
a = ar.asm()

# for line in a.final_asm_file_gen():
#     print(line)
# for line in a._get_asm_dict_list_gen():
def list_dict_to_line(list_dict):
    line = ''
    for i in [list_dict[0]['MnemonicsIC'] , list_dict[0]['Operand1IC'] , list_dict[0]['Operand2IC']]:
        if i is not None:
            line = line + i + ' '
    return line + '\n'
#     print(line)
for line in LCP.LC_processing(a._get_asm_dict_list_gen()):
    with open(IC_path , 'a') as IC_file:
        
        IC_line = list_dict_to_line(line)
        IC_file.write(IC_line)
    print(line)

# for line in a._get_asm_file():
#     print(line)
