import whisper
import streamlit as st
import requests
from tempfile import NamedTemporaryFile

# Inicializa o modelo do Whisper (escolha o tamanho: tiny, base, small, medium, large)
model = whisper.load_model("small")

# Título da Aplicação
st.title("Transcrição de Vídeo com Whisper")

# Instruções
st.write("Insira o link de um vídeo hospedado (por exemplo, na AWS) para transcrição.")

# Entrada para o link do vídeo
video_url = st.text_input("URL do Vídeo")

# Processamento do link do vídeo
if video_url:
    try:
        # Baixa o vídeo temporariamente
        st.write("Baixando o vídeo...")
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Verifica se o download foi bem-sucedido

        # Salva o vídeo em um arquivo temporário
        with NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
            temp_path = temp_file.name

        # Exibe o progresso
        with st.spinner("Transcrevendo o áudio..."):
            # Transcreve o vídeo
            result = model.transcribe(temp_path)
            transcription = result["text"]

        # Exibe a transcrição
        st.subheader("Transcrição:")
        st.write(transcription)

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao baixar o vídeo: {e}")
    except Exception as e:
        st.error(f"Ocorreu um erro ao transcrever o vídeo: {e}")
