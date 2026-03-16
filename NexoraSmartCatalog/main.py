import json
from src.generator import CatalogGenerator
from src.processor import ImageProcessor

def main():
    print("--- Iniciando Nexora Smart-Catalog System ---")
    
    # 1. Cargar Datos
    try:
        with open('data/productos.json', 'r', encoding='utf-8') as f:
            productos = json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo de productos.")
        return

    # 2. Inicializar Herramientas
    img_proc = ImageProcessor()
    catalog = CatalogGenerator(brand_name="Nexora & IconicHats")

    # 3. Procesar cada producto
    print(f"Procesando {len(productos)} productos...")
    for p in productos:
        # Procesamos la imagen (o generamos una temporal)
        p['img_final'] = img_proc.prepare_image(p['imagen'], p['nombre'])
        print(f" > Producto {p['nombre']} listo.")

    # 4. Generar el PDF final
    catalog.create_pdf(productos)
    print("\n¡Listo! Revisa la carpeta 'output/' para ver tu catálogo.")

if __name__ == "__main__":
    main()