from Backend.src.parser_prescription import PrescriptionParser
import pytest


@pytest.fixture()
def doc_1_maria():
    document_text = '''
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:
    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''

    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_abhram():
    document_text = '''
    Name: Abhram Lincon Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:
    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''

    return PrescriptionParser(document_text)

def test_get_name(doc_1_maria, doc_2_abhram):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_abhram.get_field('patient_name') == 'Abhram Lincon'


def test_get_address(doc_1_maria, doc_2_abhram):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_abhram.get_field('patient_address') == '9 tennis court, new Russia, DC'





