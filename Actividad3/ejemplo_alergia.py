patient_id = "2595883"  # ID del paciente previamente creado
substance_code = "1840032"  # Código para Penicilina
substance_display = "Penicilina"  # Nombre de la sustancia
criticality = "high"  # Nivel de gravedad
category = "medication"  # Categoría de la alergia (medicación)
manifestation_code = "77386006"  # Código de manifestación Presion alta
manifestation_display = "Shock disorder or hypotension"  # Descripción de la manifestación
severity = "severe"  # Severidad de la reacción
note = "El paciente tiene una reacción severa en la presion tras el consumo de penicilina."  # Nota descriptiva


allergy_dict = create_allergy_intolerance_resource(
    patient_id, substance_code, substance_display, criticality, category,
    manifestation_code, manifestation_display, severity, note
)

send_allergy_intolerance_to_fhir(allergy_dict)
