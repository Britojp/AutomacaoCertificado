import os

def excluir_pdfs_na_pasta(pasta):
    for raiz, dirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.jpg'):
                caminho_pdf = os.path.join(raiz, arquivo)
                os.remove(caminho_pdf)

caminho_da_pasta = "certificados prontos vFINAL/PDF"
excluir_pdfs_na_pasta(caminho_da_pasta)
