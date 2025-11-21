from pytubefix import YouTube
import os

def sanitize_filename(name: str) -> str:
    invalid = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for ch in invalid:
        name = name.replace(ch, '')
    return name

def carregar_links(arquivo_txt):
    with open(arquivo_txt, "r", encoding="utf-8") as f:
        links = [linha.strip() for linha in f if linha.strip()]
    return links

def baixar_videos_do_txt(arquivo_txt, pasta_saida="videos"):
    links = carregar_links(arquivo_txt)

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for link in links:
        try:
            yt = YouTube(link)
            
            # stream de maior qualidade mp4
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

            nome_video = sanitize_filename(yt.title)
            print(f"Baixando: {nome_video}...")

            stream.download(output_path=pasta_saida, filename=f"{nome_video}.mp4")
            print("✔ Download concluído!\n")

        except Exception as e:
            print(f"Erro ao baixar {link}: {e}")

# Usar:
baixar_videos_do_txt("links.txt")
