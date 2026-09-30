#Será la herramienta que posteriormente
# permitirá buscar en el texto original de los informes.

import pymupdf


class BuscadorInformes:

    def __init__(self, carpeta_docs):
        self.carpeta_docs = carpeta_docs

    def buscar(self, termino):

        resultados = []

        for archivo in self.carpeta_docs.glob("*.pdf"):

            documento = pymupdf.open(archivo)

            for numero_pagina, pagina in enumerate(documento):

                texto = pagina.get_text()

                posicion = texto.lower().find(termino.lower())

                if posicion != -1:

                    inicio = max(0, posicion - 300)
                    fin = min(len(texto), posicion + len(termino) + 500)

                    fragmento = texto[inicio:fin]

                    resultados.append({
                        "informe": archivo.name,
                        "pagina": numero_pagina + 1,
                        "fragmento": fragmento
                    })

            documento.close()

        return resultados