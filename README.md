# 🤖 Busca - Agente IA (Extractor de Informes Técnicos)

Sistema operativo: Linux
Lenguaje: Python
Interfaz: Consola
Modelo de lenguaje: Gemini API
Base de datos: MySQL
Fuente documental: 4 informes PDF
Arquitectura: Agente IA con dos herramientas: búsqueda documental y consulta SQL.


> **Criterio de Diseño:** 

Este proyecto implementa un **Agente de IA** diseñado para procesar, estructurar y consultar informes técnicos del sector. Su objetivo principal es recibir documentos (PDFs), extraer información clave mediante Inteligencia Artificial (Gemini SDK) y guardar/buscar los resultados de manera persistente en una base de datos MySQL.

---

## 🛠️ Cómo Instalar y Ejecutar

Todo el código fuente se encuentra alojado en este repositorio de GitHub. Sigue estos pasos para poner en marcha la solución localmente:

### 1. Clonar el repositorio y preparar el entorno
```bash
git clone <https://github.com/SchlampeCta/agenteIA.git>
cd AGENTE
```

### 2. Configurar las Variables de Entorno (Seguridad)
Crea un archivo `.env` en la raíz del proyecto para proteger tus credenciales. **Este archivo está configurado en el `.gitignore` para evitar su filtración pública.**

### 3. Instalar librerías de Python
Asegúrate de tener Python instalado y ejecuta:
```bash
pip install google-genai mysql-connector-python python-dotenv pydantic
```

### 4. Ejecutar la solución
Para iniciar el agente principal:
```bash
python src/main.py
```

---

## 📐 Arquitectura y Decisiones Técnicas

El proyecto sigue una arquitectura modular con separación de responsabilidades dividida en clases específicas (dentro del paquete raíz `src/`):

```text


AGENTE/
.env
docs
src
     bd
         buscar_fichas
         guardar_mysql  # Conexión, creación de tablas
      logica
         _init_.py
         agente.py #Preguntas y el modelo elige que metodo de busqueda
         buscar.py  # Búsqueda 
         extraer.py # Conexión PDF, extraccion de informacion
         ficha.py  #Fichas/ formato de la información resumida de PDF
     init_.py
     main.py # Punto de entrada y flujo de ejecución

```

### ¿Por qué se tomó esta decisión?
* **`clase extraer.py` :** Conecta el PDF con la IA y MySQL. Genera un prompt estructurado usando ** Pydantic (response format)** para garantizar que Gemini siempre responda en el formato JSON exacto requerido sin desviaciones.
* **`clase buscar.py`:** Implementa búsquedas eficientes por palabra clave. Pasa el nombre del documento a la base de datos, retorna el `ID` correspondiente y extrae los datos asociados de la tabla de resultados sin recargar toda la página.
* **`clase agente.py`:** Administra el inicio de los códigos base y asegura la cohesión del espacio de trabajo y es el integrador de preguntas

---

## 📋 Desglose de Datos Extraídos
El agente lee los archivos PDF y extrae de forma estricta los siguientes campos del negocio para guardarlos en MySQL:
* **Código de Proyecto**
* **Cliente / Sector**
* **Periodo de Ejecución**
* **Problema y Objetivos**
* **Metodología aplicada**
* **Resultados -> Indicadores **
* **Lecciones Aprendidas y Recomendaciones**
* **Fuente del Documento** *(Ref: PC-2026-006 sup la)*

---

## 🧠 Supuestos Asumidos

1. **Estructura del PDF:** Se asume que los PDFs contienen texto legible directamente de forma nativa por las librerías seleccionadas o que el SDK de Gemini procesará directamente el archivo binario.
2. **Formato del Output:** Se asume que cualquier informe técnico procesado mantendrá una estructura mínima que permita rellenar los bloques de *Metodología, Resultados y Lecciones Aprendidas*.
3. **Consistencia de BD:** Se asume que el ID del documento es único y autoincremental (`ID = 1`, etc.) para agilizar el retorno de consultas puntuales en `buscar.py`.

---

## ⚠️ Limitaciones Conocidas

* **Dependencia de Red:** Al delegar la extracción en el SDK de Gemini, el sistema requiere conexión a internet constante; fallará si Google AI Studio sufre una degradación del servicio.
* **Límites de Rate Limit (Tokens por minuto):** Procesar PDFs sumamente masivos de forma simultánea podría agotar los tokens gratuitos de la API Key.

---

## 💰 Estimación de Costos de Uso 

Evaluación de costos basada en el modelo **Gemini 2.5 Flash** para un escenario de **50 consultores activos a diario**:

* **Uso Promedio:** Cada consultor sube/analiza **5 informes técnicos al día** (Total = 250 informes/día).
* **Tamaño del Documento:** Promedio de 15 páginas por PDF (~10,000 tokens de entrada).
* **Cálculo de Tokens Diarios:** 250 informes × 10,000 tokens = **2,500,000 tokens de entrada / día**.
* **Costo Financiero:** Con los precios actuales de Gemini 2.5 Flash (\$0.075 por millón de tokens de entrada), el costo operativo aproximado es de **\$0.19 USD al día** (~\$6.00 USD al mes para todo el equipo de 50 personas), lo que demuestra que es una solución altamente escalable y extremadamente rentable.
