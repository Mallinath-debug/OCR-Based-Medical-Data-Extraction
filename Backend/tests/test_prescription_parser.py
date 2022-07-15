from Backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone(000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks-
    Lialda - take 2 pill everyday for 1 month
    Refill: 3 times
    '''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
       Dr John Smith, M.D
       2 Non-Important Street,
       New York, Phone(000)-111-2222
       Name: dhoni Kohli Date: 5/11/2022
       Address: 2 cricket blvd, New Delhi
       Omeprazole 40 mg
       Directions:Use two tablets daily for three months
       Refill : 4 times
       '''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')

def test_get_name(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_field('patient_name') == 'dhoni Kohli'
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field('patient_address') == None

def test_get_medicine(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert doc_2_virat.get_field('medicines') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_field('medicines') == None

def test_get_directions(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('Directions') == 'Prednisone, Taper 5 mg every 3 days, \n Finish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_virat.get_field('Directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_field('Directions') == None

def test_get_refill(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('refills') == '3'
    assert doc_2_virat.get_field('refills') == '4'
    assert doc_3_empty.get_field('refills') == None

def test_parse(doc_1_maria,doc_2_virat,doc_3_empty):
    record_maria=doc_1_maria.parser()
    assert record_maria['patient_name'] == 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert record_maria['directions'] == 'Prednisone, Taper 5 mg every 3 days, \n Finish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert record_maria['refills'] == '3'

    record_virat = doc_2_virat.parser()
    assert record_virat == {
        'patient_name': 'dhoni Kohli',
        'patient_address':'2 cricket blvd, New Delhi',
        'medicines':'Omeprazole 40 mg',
        'directions':'Use two tablets daily for three months',
        'refills':'4'
    }






