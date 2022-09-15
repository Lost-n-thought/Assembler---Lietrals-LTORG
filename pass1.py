import asm_read as ar

a = ar.asm()

# for line in a.final_asm_file_gen():
#     print(line)
for line in a._get_asm_dict_list_gen():
    print(line)

# for line in a._get_asm_file():
#     print(line)