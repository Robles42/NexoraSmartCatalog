from PIL import Image, ImageDraw, ImageFont
import os

class ImageProcessor:
    def __init__(self):
        self.size = (300, 300) # Tamaño uniforme para el catálogo

    def prepare_image(self, input_path, product_name):
        """Redimensiona y prepara la imagen del producto"""
        if not os.path.exists(input_path):
            # Si no hay imagen, creamos una temporal con el nombre
            img = Image.new('RGB', self.size, color=(73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10,150), f"Foto: {product_name}", fill=(255,255,0))
            output_path = f"assets/temp_{product_name}.png"
            img.save(output_path)
            return output_path
        
        # Si existe, la redimensionamos profesionalmente
        img = Image.open(input_path)
        img = img.resize(self.size, Image.Resampling.LANCZOS)
        output_path = f"assets/proc_{os.path.basename(input_path)}"
        img.save(output_path)
        return output_path