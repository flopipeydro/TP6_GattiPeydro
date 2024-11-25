import json
import requests
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.codeablereference import CodeableReference
from fhir.resources.reference import Reference
from fhir.resources.annotation import Annotation
from fhir.resources.allergyintolerance import AllergyIntoleranceReaction

def create_allergy_intolerance_resource(patient_id, substance_code, substance_display, criticality, category, manifestation_code, manifestation_display, severity, note):
    note_annotation = Annotation(text=note)
    substance = CodeableConcept(
        coding=[{
            "code": substance_code,
            "display": substance_display,
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm"
        }]
    )

    manifestation = [
        CodeableReference(
            concept=CodeableConcept(
                coding=[{
                    "system": "http://snomed.info/sct",
                    "code": manifestation_code,
                    "display": manifestation_display
                }]
            )
        )
    ]

    reaction = AllergyIntoleranceReaction(
        substance=substance,
        manifestation=manifestation,
        severity=severity,
        note=[note_annotation]
    )

    allergy_intolerance = AllergyIntolerance(
        resourceType="AllergyIntolerance",
        patient=Reference(reference=f"Patient/{patient_id}"),
        reaction=[reaction],
        category=[category],
        criticality=criticality
    )

    allergy_dict = allergy_intolerance.dict(by_alias=True)
    print("JSON generado para la alergia:")
    print(json.dumps(allergy_dict, indent=4))
    return allergy_dict

def send_allergy_intolerance_to_fhir(allergy_dict):
    url = f"{BASE_URL}/AllergyIntolerance"
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(url, headers=headers, json=allergy_dict)

    if response.status_code == 201:
        print("Alergia creada exitosamente.")
    else:
        print(f"Error al crear la alergia: {response.status_code}")
        print("Detalles del error:")
        print(response.text)
        try:
            print("Respuesta JSON del error:")
            print(response.json())
        except ValueError:
            print("La respuesta no contiene un JSON válido.")
