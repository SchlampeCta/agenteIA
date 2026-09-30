import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


class GuardarMySQL:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD"),
            database="procesa_consultores"
        )

    def guardar_ficha(self, ficha):

        cursor = self.conexion.cursor()

        # Guardar información general del proyecto
        sql_proyecto = """
            INSERT INTO proyectos (
                codigo_proyecto,
                cliente,
                sector,
                periodo_ejecucion,
                problema,
                objetivos,
                metodologia,
                lecciones_aprendidas,
                recomendaciones
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        objetivos = "\n".join(ficha.objetivos)
        metodologia = "\n".join(ficha.metodologia)
        lecciones = "\n".join(ficha.lecciones_aprendidas)
        recomendaciones = "\n".join(ficha.recomendaciones)

        valores_proyecto = (
            ficha.codigo_proyecto,
            ficha.cliente,
            ficha.sector,
            ficha.periodo_ejecucion,
            ficha.problema,
            objetivos,
            metodologia,
            lecciones,
            recomendaciones
        )

        cursor.execute(sql_proyecto, valores_proyecto)

        proyecto_id = cursor.lastrowid

        # Guardar resultados
        sql_resultado = """
            INSERT INTO resultados (
                proyecto_id,
                indicador,
                linea_base,
                meta,
                resultado,
                estado
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for resultado in ficha.resultados:

            valores_resultado = (
                proyecto_id,
                resultado.indicador,
                resultado.linea_base,
                resultado.meta,
                resultado.resultado,
                resultado.estado
            )

            cursor.execute(sql_resultado, valores_resultado)

        self.conexion.commit()

        cursor.close()
        self.conexion.close()

        print("Ficha guardada correctamente en MySQL.")