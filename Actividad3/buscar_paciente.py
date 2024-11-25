import requests
# Endpoint base del servidor FHIR
BASE_URL = "https://launch.smarthealthit.org/v/r4/fhir"

# Buscar paciente por documento
def search_patient_by_document(document_number):
    url = f"{BASE_URL}/Patient?identifier={document_number}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        patients = response.json().get('entry', [])

        if patients:
            print(f"Paciente(s) encontrado(s) con el documento {document_number}:")
            for patient_entry in patients:
                patient = patient_entry['resource']
                name = patient.get('name', [{}])[0]
                given_name = name.get('given', [''])[0]
                family_name = name.get('family', '')
                birth_date = patient.get('birthDate', 'No especificada')
                gender = patient.get('gender', 'No especificado')

                print(f"ID: {patient['id']}")
                print(f"Nombre: {given_name} {family_name}")
                print(f"Fecha de nacimiento: {birth_date}")
                print(f"Género: {gender}")
                print("-------------------------------")
        else:
            print(f"No se encontró ningún paciente con el documento {document_number}.")
    else:
        print(f"Error al buscar el paciente: {response.status_code}")
        print(response.json())
