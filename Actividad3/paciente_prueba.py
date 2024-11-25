from patient_with_id import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

family_name = "Gomez"
given_name = "Martin"
birth_date = "2000-07-15"
gender = "male"
phone = "+1135042290"  
document_number = "42305627"  

patient_with_id = create_patient_resource(family_name, given_name, birth_date, gender, phone, document_number)

patient_id = send_resource_to_hapi_fhir(patient_with_id, 'Patient')

if patient_id:
    print(f"Paciente con ID {patient_id} creado exitosamente.")
    get_resource_from_hapi_fhir(patient_id, 'Patient')
else:
    print("Error al crear el paciente.")
