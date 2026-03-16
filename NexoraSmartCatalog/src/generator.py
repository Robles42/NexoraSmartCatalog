from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
import os

class CatalogGenerator:
    def __init__(self, brand_name):
        self.brand = brand_name
        self.output_path = "output/"
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def generate_qr(self, product_id, link):
        qr = qrcode.make(link)
        path = f"assets/qr_{product_id}.png"
        qr.save(path)
        return path

    def create_pdf(self, products):
        filename = f"{self.output_path}Catalogo_{self.brand}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        
        c.setFont("Helvetica-Bold", 20)
        c.drawString(200, 750, f"Catálogo Oficial: {self.brand}")
        
        y_position = 650
        for p in products:
            # Generar QR dinámico
            qr_path = self.generate_qr(p['id'], p['link'])
            
            # Dibujar Info
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, y_position, p['nombre'])
            c.setFont("Helvetica", 12)
            c.drawString(100, y_position - 20, f"Precio: ${p['precio']}")
            
            # Dibujar QR
            c.drawImage(qr_path, 400, y_position - 50, width=80, height=80)
            
            y_position -= 120
            if y_position < 100:
                c.showPage()
                y_position = 700
                
        c.save()
        print(f"Catálogo generado exitosamente en: {filename}")