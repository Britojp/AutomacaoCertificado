import fitz
import os

def converter_pdf_para_jpg(caminho_pdf, dpi=300):
    if caminho_pdf.lower().endswith('.pdf'):
        pdf_documento = fitz.open(caminho_pdf)

        for numero_pagina in range(len(pdf_documento)):
            pagina = pdf_documento.load_page(numero_pagina)

            escala = dpi / 72

            matriz = fitz.Matrix(escala, escala)

            pix = pagina.get_pixmap(matrix=matriz)

            nome_jpg = f"{os.path.splitext(caminho_pdf)[0]}.jpg"
            pix.save(nome_jpg)

def converter_pdfs_na_pasta(pasta, dpi=300):
    for arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, arquivo)
        converter_pdf_para_jpg(caminho_completo, dpi)


caminho_da_pasta = "modelos certificados"
converter_pdfs_na_pasta(caminho_da_pasta, dpi=300)
