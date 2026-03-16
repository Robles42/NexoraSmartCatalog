# Nexora Smart-Catalog

Sistema automatizado de generación de catálogos comerciales para las marcas **Nexora** e **IconicHats**. Este proyecto integra procesamiento de imágenes, generación de códigos QR dinámicos y maquetación de documentos PDF profesionales mediante Python.

## Características Técnicas
* **Procesamiento de Imágenes:** Normalización y redimensionamiento de activos visuales mediante la librería **Pillow**.
* **Generación de QR:** Creación automática de códigos QR vinculados a WhatsApp para cada producto, facilitando la conversión de ventas.
* **Maquetación Dinámica:** Generación de documentos PDF de alta calidad utilizando la librería **ReportLab**.
* **Gestión de Datos:** Arquitectura desacoplada que utiliza **JSON** como base de datos ligera para facilitar la escalabilidad y edición de productos.

## Estructura del Proyecto
```text
NexoraSmartCatalog/
├── src/
│   ├── generator.py    # Lógica de construcción del PDF y QR
│   └── processor.py    # Transformación y normalización de imágenes
├── data/
│   └── productos.json  # Base de datos de productos (Marcas, precios, links)
├── assets/             # Almacenamiento de imágenes procesadas y QRs generados
├── output/             # Directorio de salida para los catálogos finales
└── main.py             # Punto de entrada y orquestador del sistema