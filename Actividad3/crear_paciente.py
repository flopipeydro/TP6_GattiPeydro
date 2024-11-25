from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

# Endpoint base del servidor FHIR
BASE_URL = "https://launch.smarthealthit.org/v/r4/fhir"

# Crear un recurso Patient
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_number=None):
    patient = Patient()
    
    
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    
    if birth_date:
        patient.birthDate = birth_date

    
    if gender:
        patient.gender = gender

    
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]
    
    
    if document_number:
        patient.identifier = [{
            "use": "official",  # Identificador oficial
            "system": "http://argentina.gob/dni",  # Sistema de emisión del documento
            "value": document_number  # Número de documento
        }]
    
    return patient
