import json
import requests
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.reference import Reference
from fhir.resources.annotation import Annotation
from fhir.resources.allergyintolerance import AllergyIntoleranceReaction

def create_allergy(patient_id):
    url = f"{BASE_URL}/AllergyIntolerance"
    allergy_data = {
        "resourceType": "AllergyIntolerance",
        "identifier": [{"system": "http://example.com/identifier", "value": "A12345"}],
        "patient": {"reference": f"Patient/{patient_id}"},
        "substance": {"coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "1840032", "display": "Penicilina"}]},
        "status": "active",
        "criticality": "high", #reaaccion grave
        "category": "medication",
        "reaction": [
            {
                "substance": {
                    "coding": [
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "1840032",
                            "display": "Penicilina"
                        }
                    ]
                },
                "manifestation": [
                    {
                        "coding": [
                            {
                                "system": "http://snomed.info/sct",
                                "code": "77386006",  # Código SNOMED para caida de presion arterial
                                "display": "Shock disorder or hypotension"
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "system": "http://snomed.info/sct",
                                "code": "267036007",  # Código SNOMED para dificultad para respirar
                                "display": "Dyspnoea"
                            }
                        ]
                    }
                ],
                "severity": "severe", 
                "exposureRoute": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "272741003",  # Código para ruta de exposición intravenosa
                            "display": "Intravenous"
                        }
                    ]
                },
                "note": "El paciente presenta una reacción severa de aumento de presion arterial y dificultad para respirar tras el consumo de penicilina."
            }
        ],
        "note": [
            {
                "text": "El paciente tiene un historial conocido de reacciones alérgicas graves a medicamentos, especialmente a la penicilina."
            }
        ]
      }
    response = requests.post(url, headers={"Content-Type": "application/json"}, json=allergy_data)
    if response.status_code == 201:
        print("Alergia creada con éxito.")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error al crear la alergia:", response.text)
