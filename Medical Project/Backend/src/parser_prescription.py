import re
from Backend.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name' : self.get_field('patient_name'),
            'patient_address' : self.get_field('patient_address'),
            'medicines' : self.get_field('medicines'),
            'Diretions_to_use' : self.get_field('Diretions_to_use'),
            'refill' : self.get_field('refill')
        }

    def get_field(self, field_name):

        pattern_dict = {
            'patient_name' : {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'Diretions_to_use': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)times', 'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags = pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':

    pp = PrescriptionParser(document_text)
    print(pp.parse())
    #print(pp.get_address())
