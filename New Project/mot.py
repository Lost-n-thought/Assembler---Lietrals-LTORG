import os

# default format list[properties_dict(), line_dict()]

def __init__():
        mot_file = __get_mot_file()
        first_line = mot_file.readline()
        field_names = first_line.rstrip().split('\t')
    
def __get_mot_file():
    Directory = os.path.dirname(__file__)
    mot_directory = os.path.join(Directory, 'MOT.tsv')
    
    mot_file = open(mot_directory, 'r')
    
    mot_file = mot_file
    return mot_file

def _get_mot_dict():
    for line in __get_mot_file():
        line = line.rstrip().split('\t')
        yield dict(zip(field_names, line))
        
def _check():
    for line in _get_mot_dict():
        print(line)
        
def is_Mnemonics(, word):
    for line in _get_mot_dict():
        if line['Mnemonics'] == word:
            return True
    return False
def get_attributes(, word : str , attribute : str = 'Size'):
    for line in _get_mot_dict():
        if line['Mnemonics'] == word:
            return line[attribute]
    return None