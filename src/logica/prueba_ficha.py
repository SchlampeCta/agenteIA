from extraer import ExtractorPDF
from ficha import extraer_ficha
from pathlib import Path
import sys


#Buscar modulos dentro del src y encontrar automaticamente la ruta del proyecto
sys.path.append(str(Path(__file__).resolve().parents[1]))

from extraer import ExtractorPDF
from ficha import extraer_ficha
from bd.guardar_mysql import GuardarMySQL   


ruta_pdf = "/home/usuario/Documentos/AGENTE/docs/Informe_Cierre_PC-2025-014_Cooperativa_Horizonte_Andino.pdf"


print("1. Extrayendo texto del PDF...")

extractor = ExtractorPDF(ruta_pdf)
texto = extractor.extraer_texto()

print("2. Generando ficha con Gemini...")

ficha = extraer_ficha(texto)

print("3. Ficha generada correctamente.")

print(ficha)

#print("4. Guardando ficha en MySQL...")

#guardar = GuardarMySQL()
#guardar.guardar_ficha(ficha)

#print("5. Proceso terminado.")

print("Prueba terminada. La ficha NO se guardó en MySQL.")