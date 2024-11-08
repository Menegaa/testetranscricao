import whisper
import streamlit as st
import os
from tempfile import NamedTemporaryFile

# Inicializa o modelo do Whisper (escolha o tamanho: tiny, base, small, medium, large)
model = whisper.load_model("small")

# Título da Aplicação
st.title("Transcrição de Vídeo com Whisper")

# Instruções
st.write("Faça o upload de um vídeo para transcrição.")

# Upload de Arquivo
uploaded_file = st.file_uploader("Escolha um arquivo de vídeo", type=["mp4", "mov", "mkv", "avi", "mp3", ".ogg"])

# Processamento do arquivo de vídeo
if uploaded_file is not None:
    # Salva o arquivo temporariamente
    with NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    # Exibe o progresso
    with st.spinner("Transcrevendo o áudio..."):
        # Transcreve o vídeo
        result = model.transcribe(temp_path)
        transcription = result["text"]

    # Exibe a transcrição
    st.subheader("Transcrição:")
    st.write(transcription)

    # Remove o arquivo temporário após o uso
    os.remove(temp_path)
