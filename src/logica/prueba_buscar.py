from pathlib import Path

from buscar import BuscadorInformes


carpeta_docs = Path("/home/usuario/Documentos/AGENTE/docs")

buscador = BuscadorInformes(carpeta_docs)

termino = "inventario"

print(f"Buscando: {termino}")
print("=" * 60)

resultados = buscador.buscar(termino)

for resultado in resultados:

    print(f"\nInforme: {resultado['informe']}")
    print(f"Página: {resultado['pagina']}")
    print(resultado["fragmento"])
    print("-" * 60)

print(f"\nTotal de coincidencias: {len(resultados)}")