"""Biblioteca PyMuPDF para trabajar con archivos PDF."""
import pymupdf 


class ExtractorPDF:

    def __init__(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf

    def extraer_texto(self):
        """
        Extrae todo el texto del PDF.
        """
        documento = pymupdf.open(self.ruta_pdf)

        texto_completo = ""

        for pagina in documento:
            texto_completo += pagina.get_text()

        documento.close()

        return texto_completo

if __name__ == "__main__":

    extraerDocUno = ExtractorPDF("/home/usuario/Documentos/AGENTE/docs/Informe_Cierre_PC-2026-006_Supermercados_La_Canasta.pdf")

    texto = extraerDocUno.extraer_texto()

    print(texto)