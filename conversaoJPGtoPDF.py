import os
from PIL import Image
from main import sheet

nomesAlunos = [
    sheet.cell(row=row, column=1).value
    for row in range(2, sheet.max_row + 1)
]

nomesPalestrantes = [
    sheet.cell(row=row, column=2).value
    for row in range(2, sheet.max_row + 1)
]

def converter_jpg_para_pdf(caminho_jpg, caminho_pdf):
    try:
        imagem = Image.open(caminho_jpg)
        imagem.save(caminho_pdf, "PDF", resolution=300.0, save_all=True)
    except Exception as e:
        print(f"Erro ao converter {caminho_jpg}: {e}")

def converter_jpgs_na_pasta(pasta):
    for raiz, dirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.jpg'):
                caminho_jpg = os.path.join(raiz, arquivo)
                caminho_pdf = os.path.splitext(caminho_jpg)[0] + '.pdf'
                converter_jpg_para_pdf(caminho_jpg, caminho_pdf)

for palestrante in nomesPalestrantes:
    caminho_da_pasta = os.path.join("certificados prontos", palestrante)
    if os.path.exists(caminho_da_pasta):
        converter_jpgs_na_pasta(caminho_da_pasta)
