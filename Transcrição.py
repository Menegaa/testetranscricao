import whisper

# Carregar o modelo Whisper (escolha o tamanho que preferir: tiny, base, small, medium, large)
model = whisper.load_model("small")

# Caminho para o arquivo de vídeo que você quer transcrever
video_path = 'COLOQUE AQUI O CAMINHO DO VÍDEO'

# Transcrever o vídeo
result = model.transcribe(video_path)

# Exibir o texto transcrito
print(result["text"])

# (Opcional) Salvar a transcrição em um arquivo de texto
# with open("transcricao.txt", "w") as f:
#     f.write(result["text"])








