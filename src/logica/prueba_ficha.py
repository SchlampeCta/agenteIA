from extraer import ExtractorPDF
from ficha import extraer_ficha


ruta_pdf = "/home/usuario/Documentos/AGENTE/docs/Informe_Cierre_PC-2026-006_Supermercados_La_Canasta.pdf"


# 1. Extraer texto del PDF

extractor = ExtractorPDF(ruta_pdf)

texto = extractor.extraer_texto()


# 2. Extraer la ficha utilizando Gemini

ficha = extraer_ficha(texto)


# 3. Mostrar la ficha

print(ficha)