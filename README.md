# Vehicle Ads Dashboard

Aplicación web interactiva construida con **Streamlit** y **Plotly** para
explorar un conjunto real de anuncios de venta de autos en Estados Unidos.
Permite visualizar el dataset y generar gráficos sobre la relación entre
precio, kilometraje y año del vehículo.

## Demo

> Aplicación desplegada en Render:
> `https://proyecto-sprint7-zsy8.onrender.com/`
>
> *(El plan gratuito de Render puede tardar unos segundos en "despertar".)*

## Objetivo del negocio

Dar a un comprador o vendedor una vista rápida del mercado de autos usados:
¿cómo se distribuye el kilometraje?, ¿qué relación hay entre el precio y las
millas recorridas? El panel responde estas preguntas de forma visual e
interactiva.

## Funcionalidades

- Tabla completa del dataset de anuncios.
- Botón para construir un **histograma** del kilometraje (millas).
- Botón para construir un **gráfico de dispersión** Precio vs Millas.
- Descarga de una muestra limpia del dataset en CSV.

## Tecnologías

- Python 3.11
- Streamlit — interfaz web
- Plotly Express — gráficos interactivos
- pandas — manipulación de datos

## Estructura del proyecto

```
vehicle-ads-dashboard/
├── app.py                          # aplicación Streamlit
├── notebooks/
│   └── EDA.ipynb                   # análisis exploratorio previo
├── vehicles1_us.csv                # dataset de anuncios
├── vehicles_us_clean_sample.csv    # muestra limpia (precio/odómetro sin nulos)
├── requirements.txt
├── LICENSE
└── README.md
```

## Cómo ejecutar localmente

```bash
git clone https://github.com/OrlandoCorona/vehicle-ads-dashboard.git
cd vehicle-ads-dashboard

python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt

streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`.

## Proceso de análisis (notebook)

El notebook [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb) carga el dataset,
revisa su estructura y tipos, explora la distribución del kilometraje y la
relación precio–kilometraje, y genera la muestra limpia que usa la app.

## Trabajo futuro

- Añadir filtros por tipo de vehículo, año y condición.
- Incluir más gráficos (precio por marca, días en publicación).
- Mostrar métricas resumidas (precio medio, mediana de kilometraje).
