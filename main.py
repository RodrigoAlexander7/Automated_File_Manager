from app.pdf_reader import get_words_pdf

if __name__ == "__main__":
    ruta = "test.pdf"
    dictionary = get_words_pdf(ruta)
    print(f"Todo ok ({len(dictionary)} caracteres):\n")
    print(dictionary)