import os
import json
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel
from google import genai


load_dotenv()


# -----------------------------------
# Estructura de cada resultado
# -----------------------------------

class Resultado(BaseModel):
    indicador: str
    linea_base: Optional[str]
    meta: Optional[str]
    resultado: Optional[str]
    estado: Optional[str]


# -----------------------------------
# Estructura de la ficha del proyecto
# -----------------------------------

class FichaProyecto(BaseModel):
    codigo_proyecto: Optional[str]
    cliente: Optional[str]
    sector: Optional[str]
    periodo_ejecucion: Optional[str]
    problema: Optional[str]

    objetivos: list[str]
    metodologia: list[str]

    resultados: list[Resultado]

    lecciones_aprendidas: list[str]
    recomendaciones: list[str]


# -----------------------------------
# Cliente Gemini
# -----------------------------------

cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -----------------------------------
# Extracción de la ficha
# -----------------------------------

def extraer_ficha(texto):

    instrucciones = """
Analiza el siguiente informe de cierre de proyecto.

Extrae únicamente información que esté presente en el informe.

NO inventes información.

NO hagas suposiciones.

Si un dato no aparece claramente en el documento,
devuelve null.

Debes extraer:

- código del proyecto
- cliente
- sector
- periodo de ejecución
- problema
- objetivos
- metodología
- resultados
- lecciones aprendidas
- recomendaciones

Los resultados deben estar separados por indicador.

Para cada indicador debes extraer:

- indicador
- línea base
- meta
- resultado
- estado

Conserva los valores tal como aparecen en el informe.

No agregues información que no esté en el documento.

INFORME:

""" + texto

    respuesta = cliente.interactions.create(
        model="gemini-3.8-flash",
        input=instrucciones,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": FichaProyecto.model_json_schema()
        }
    )

    datos = json.loads(respuesta.output_text)

    return FichaProyecto.model_validate(datos)