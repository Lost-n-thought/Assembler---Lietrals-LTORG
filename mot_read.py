import os

class mot():
    
    def __init__(self):
        mot_file = self.__get_mot_file()
        first_line = mot_file.readline()
        self.field_names = first_line.rstrip().split('\t')
    
    def __get_mot_file(self):
        Directory = os.path.dirname(__file__)
        mot_directory = os.path.join(Directory, 'MOT.tsv')
        
        self.mot_file = open(mot_directory, 'r')
        
        mot_file = self.mot_file
        return mot_file

    def _get_mot_dict(self):
        for line in self.__get_mot_file():
            line = line.rstrip().split('\t')
            yield dict(zip(self.field_names, line))
            
    def _check(self):
        for line in self._get_mot_dict():
            print(line)
            
    def is_Mnemonics(self, word):
        for line in self._get_mot_dict():
            if line['Mnemonics'] == word:
                return True
        return False
    def get_attributes(self, word : str , attribute : str = 'Size'):
        for line in self._get_mot_dict():
            if line['Mnemonics'] == word:
                return line[attribute]
        return None

# a = mot_class()
# a._check()
# print('Hello')
# a._check()

# a = mot_class()
# print(a.get_attributes('ADD' , 'Size'))