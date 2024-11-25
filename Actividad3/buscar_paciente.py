import requests
# Endpoint base del servidor FHIR
BASE_URL = "https://launch.smarthealthit.org/v/r4/fhir"
def search_patient_manually(document_id, system_url):
    search_url = f"{BASE_URL}/Patient"
    response = requests.get(search_url, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        all_patients = response.json().get("entry", [])
        for patient in all_patients:
            resource = patient.get("resource", {})
            identifiers = resource.get("identifier", [])
            for identifier in identifiers:
                if identifier["system"] == system_url and identifier["value"] == document_id:
                    print("Paciente encontrado:")
                    print(json.dumps(resource, indent=2))
                    return
        print(f"No se encontró ningún paciente con el documento {document_id}.")
    else:
        print("Error al buscar pacientes:", response.status_code, response.text)
