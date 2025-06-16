from app.pdf_reader import get_text_pdf

if __name__ == "__main__":
    ruta = "example.pdf"
    texto = get_text_pdf(ruta)
    print(f"Todo ok ({len(texto)} caracteres):\n")
    print(texto[:1000])  
