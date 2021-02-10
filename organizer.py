import os

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png', '.ai']
documentos_ext = ['.txt', '.log', '.pdf']
box_Virtual_ext = ['.deb', '.ova', '.iso', '.dcm']
ssh_AWS_ext = ['.pem']


def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]


def organizar(diretorio):
    AUDIOS_DIR =  os.path.join(diretorio, "Audios")
    IMAGENS_DIR =  os.path.join(diretorio, "Imagens")
    DOCS_DIR =  os.path.join(diretorio, "Documentos")
    VIDEOS_DIR =  os.path.join(diretorio, "Videos")
    SSH_ACCESS_DIR =  os.path.join(diretorio, "SSH_AWS")
    BOX_DIR = os.path.join(diretorio, "Virtual")
    OUTROS_DIR =  os.path.join(diretorio, "Outros")

    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)
    if not os.path.isdir(SSH_ACCESS_DIR):
        os.mkdir(SSH_ACCESS_DIR)
    if not os.path.isdir(BOX_DIR):
        os.mkdir(BOX_DIR)

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIOS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            elif extensao in ssh_AWS_ext:
                nova_pasta = SSH_ACCESS_DIR
            elif extensao in box_Virtual_ext:
                nova_pasta = BOX_DIR
            else:
                nova_pasta = OUTROS_DIR
            
            
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print("Moveu:", velho, "->", novo)


if __name__ == '__main__':
    organizar('Downloads')
