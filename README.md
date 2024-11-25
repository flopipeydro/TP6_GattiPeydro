# TP6_GattiPeydro
## Descripción
Este repositorio contiene la solución al Trabajo Práctico N°6 - Interoperabilidad de la materia Informática Médica del ITBA.

## Integrantes
- **Martin Gatti - 59712**
- **Florencia Peydro - 59105**

## Materia
- **Nombre de la materia**: Informática médica (16.22)
- **Profesores**:
  - Carlos Lazzarino
  - Eugenia Camila Berrino
  - Melina Piacentino Castaño
  - Ingrid Celia Spessotti
  
## Institución
- **ITBA** (Instituto Tecnológico de Buenos Aires)

## Estructura del repositorio
Dentro de la carpeta Actividad3 se encuentra el repositorio correspondiente al trabajo practico de interoperabilidad.
- *crear_paciente.py* Creacion del recurso patient con el DNI.
- *paciente_prueba.py* Validación del código anterior.
- *buscar_paciente.py* Buscador de pacientes por DNI en donde devuelve Nombre, ID, Fecha de Nacimiento y Genero.
- *crear_alergia.py* Creacion del recurso AllergyIntolerance.
- *ejemplo_alergia.py* Validación de este ultimo código.
- *alergia_obtenida_paciente.py* Obtiene las alergias de un paciente.
- *ejemplo_paciente.py* Validación de la alergia con el id del paciente.

Ademas podemos observar dentro del repositorio tres archivos mas:
- *patient.py* Creación del recurso paciente con algunos parámetros.
- *base.py* Lectura y escritura de recursos en el servidor público de HAPI FHIR.
- *workflow.py* Desde acá se corre el código. 
