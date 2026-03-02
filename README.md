# Cyclistic Bike-Share — Caso de estudio 1

Este repositorio documenta un caso de estudio de analítica de datos enfocado en comprender cómo difiere el uso del servicio de bicicletas compartidas Cyclistic entre **miembros anuales** y **usuarios ocasionales**, y cómo esas diferencias pueden traducirse en oportunidades de marketing orientadas a incrementar la conversión a membresías anuales.

Cyclistic opera en Chicago con una red de 692 estaciones y una flota de 5,824 bicicletas (clásicas, eléctricas y de carga). El contexto del negocio establece que los miembros anuales son significativamente más rentables que los usuarios ocasionales; por ello, la estrategia prioriza convertir a los usuarios existentes de tipo casual en miembros anuales. En este proyecto se aborda principalmente la pregunta: **¿en qué se diferencia el uso del servicio entre socios anuales y usuarios ocasionales?**

## Estructura del repositorio

```txt
.
├── Data/
│   ├── Processed/                 # Datos limpios para análisis
│   └── Raw/                       # Datos crudos (CSVs mensuales)
├── Docs/
│   └── Case Study 1_ How does a bike-share navi....pdf
├── Reporte/
│   └── Informec.pdf               # Reporte completo del proyecto
├── Scripts/
│   └── Limpieza.py                # Limpieza y preparación (Pandas)
├── Visualizaciones/
│   ├── Bicicletas mas utilizadas por usuarios.png
│   ├── Caso de estudio 1.twb
│   ├── Demanda a lo largo del tiempo.png
│   ├── Estaciones con mayor trafico de usuarios.png
│   └── Total de miembros inscritos.png
└── .gitignore
```

## Metodología

El proyecto sigue el marco de análisis de datos de seis fases: **Preguntar, Preparar, Procesar, Analizar, Compartir y Actuar**.

### Preguntar

La Directora de Marketing determinó que el futuro de Cyclistic depende de maximizar las membresías anuales, priorizando la base de usuarios existente sobre la captación de nuevos clientes. La campaña de conversión se guía por tres preguntas fundamentales: en qué se diferencian los miembros anuales y los usuarios ocasionales en su forma de usar el servicio; por qué un usuario ocasional compraría una membresía anual; y cómo puede Cyclistic utilizar los medios digitales para influir en esa decisión. Este proyecto aborda específicamente la primera pregunta.

### Preparar

Se seleccionó un periodo de estudio de 12 meses (4 de marzo de 2025 al 4 de febrero de 2026) para capturar el ciclo completo de estacionalidad y los patrones de movilidad más recientes. El dataset unificado contiene las variables necesarias para segmentar cada viaje por tipo de usuario (`member_casual`), analizar comportamiento temporal (`started_at`, `ended_at`), caracterizar el producto utilizado (`rideable_type`) y observar concentración espacial a través de estaciones y coordenadas geográficas. Aunque el dataset no incluye métricas directas de campañas digitales, sí ofrece señales claras para orientar la estrategia: a qué segmento hablarle, en qué momentos y en qué zonas concentrar los mensajes.

### Procesar

Para manejar el gran volumen de datos (más de 5.5 millones de registros), el procesamiento se realizó con Python y la librería Pandas. Se integraron los 12 archivos mensuales en un único dataframe anual con `glob` y `pd.concat`, se eliminaron registros con valores nulos y se estandarizaron las columnas de tiempo al tipo `datetime`. Posteriormente se construyó la métrica `ride_length` y se filtraron outliers: viajes con duración negativa o igual a cero (errores de registro) y viajes mayores a 4 horas (bicicletas robadas, en mantenimiento o mal ancladas), ya que no representan el uso real del servicio.

**Reporte de limpieza:**

| Métrica | Valor |
|---|---|
| Registros iniciales (crudos) | 5,552,092 filas |
| Registros finales (limpios) | 3,682,941 filas |
| Registros eliminados | 1,869,151 filas |

*Criterios de eliminación: celdas vacías o tiempos fuera de rango.*

### Analizar

Con el dataset limpio cargado en Tableau, se validaron tipos de datos y se ajustó el tratamiento de coordenadas para su correcta interpretación como campos geográficos. El análisis se centró en la distribución de viajes por segmento, preferencias por tipo de bicicleta, y patrones de uso segmentados por mes, día de la semana y hora del día. Los miembros anuales representan el **64.19%** de los viajes (2,364,243), mientras que los usuarios ocasionales conforman el **35.81%** restante (1,318,698).

Se identificó un pico de demanda entre finales de agosto e inicios de septiembre. A nivel semanal, los miembros concentran su actividad entre semana (patrón utilitario), mientras que los usuarios ocasionales aumentan su uso en fines de semana (patrón recreativo). En horario, los miembros presentan picos en la mañana y la noche; los casuales alcanzan su máximo entre 16:00 y 17:00. Geográficamente, los usuarios ocasionales se concentran en zonas costeras, parques y puntos turísticos como el Navy Pier, mientras que los miembros se distribuyen hacia el interior de la ciudad en zonas financieras y residenciales.

### Compartir

Los resultados se presentaron mediante visualizaciones interactivas construidas en Tableau (workbook `Visualizaciones/Caso de estudio 1.twb`) y exportadas como imágenes PNG dentro de la carpeta `Visualizaciones/`. El reporte narrativo completo, que incluye hallazgos, implicaciones estratégicas y recomendaciones, se encuentra documentado en `Reporte/Informec.pdf`.

> 📄 Para ver el análisis completo en profundidad, incluyendo hallazgos detallados, visualizaciones y recomendaciones estratégicas, dirígete a [`Reporte/Informec.pdf`](https://github.com/Czamudioo121/Google-Data-Analytics-Capstone-Case-Study-1/blob/main/Reporte/Informe.pdf).

### Actuar

Con base en los hallazgos, se proponen tres estrategias de conversión. La primera consiste en integrar beneficios exclusivos para bicicletas eléctricas dentro de la membresía anual (como tarifas reducidas por minuto o desbloqueos gratuitos), aprovechando que el segmento casual muestra una adopción casi equitativa entre bicicletas clásicas y eléctricas. La segunda es ejecutar campañas estacionales geolocalizadas al cierre del verano (agosto–septiembre), enfocadas en estaciones de alta actividad turística con un mensaje financiero de ahorro frente a la compra repetida de pases. La tercera es reposicionar la membresía como un producto para el uso recreativo de fin de semana, comercializándola como un "pase de libertad" y evaluando beneficios que reduzcan la fricción de cobros adicionales para viajes largos.

## Autor

Cesar Zamudio
