import requests

def get_allergies_by_patient_id(patient_id):
    url = f"http://hapi.fhir.org/baseR4/AllergyIntolerance?patient={patient_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        allergies = response.json().get('entry', [])

        if allergies:
            print(f"Alergias encontradas para el paciente con ID {patient_id}:")
            for allergy_entry in allergies:
                allergy = allergy_entry['resource']

                print(f"ID de la alergia: {allergy.get('id', 'No ID disponible')}")

                if 'reaction' in allergy and len(allergy['reaction']) > 0:
                    substance = allergy['reaction'][0].get('substance', {})
                    if substance and 'coding' in substance:
                        substance_display = substance['coding'][0].get('display', 'No disponible')
                        print(f"Sustancia: {substance_display}")
                    else:
                        print("Sustancia: No disponible")
                else:
                    print("Sustancia: No disponible")

                if 'reaction' in allergy and len(allergy['reaction']) > 0:
                    severity = allergy['reaction'][0].get('severity', 'No disponible')
                    print(f"Severidad: {severity}")

                    manifestation = allergy['reaction'][0].get('manifestation', [{}])
                    if manifestation and 'coding' in manifestation[0]:
                        manifestation_display = manifestation[0]['coding'][0].get('display', 'No disponible')
                        print(f"Reacción: {manifestation_display}")
                    else:
                        print("Reacción: No disponible")
                else:
                    print("Severidad o Reacción: No disponible")

                category = allergy.get('category', 'No disponible')
                print(f"Categoría: {category}")

                # Mostrar las notas
                if 'reaction' in allergy and len(allergy['reaction']) > 0:
                    reaction = allergy['reaction'][0]
                    if 'note' in reaction:
                        for note in reaction['note']:
                            print(f"Nota: {note.get('text', 'No disponible')}")
                    else:
                        print("Nota: No disponible")
                else:
                    print("Nota: No disponible")

                print("-------------------------------")
        else:
            print(f"No se encontraron alergias para el paciente con ID {patient_id}.")
    else:
        print(f"Error al buscar alergias: {response.status_code}")
        print(response.json())
