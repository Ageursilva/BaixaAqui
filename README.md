# **baixeaqui**

**baixeaqui** é uma API simples construída com FastAPI e yt-dlp para baixar playlists do YouTube em formato MP3 e compactá-las em um arquivo ZIP. Ela ignora erros como vídeos privados e continua o download dos próximos vídeos na playlist.

## **Requisitos**

Antes de rodar a aplicação, você precisa ter o Python instalado e as dependências necessárias. O projeto também utiliza o **yt-dlp** para fazer o download dos vídeos, o **FFmpeg** para converter para MP3 e o **FastAPI** para a API.

### **Dependências**

- Python 3.7 ou superior
- FFmpeg (certifique-se de ter o **FFmpeg** instalado no seu sistema)

## **Instalação**

## **1. Clonar o repositório**

###Clone o repositório para o seu diretório de trabalho:

```bash
git clone https://github.com/seu_usuario/baixeaqui.git
cd baixeaqui

```

## **2. Instalar as dependências**
### Execute o seguinte comando para instalar as dependências necessárias:
```bash
pip install fastapi uvicorn yt-dlp
```

## **3. Instalar o FFmpeg**
### Windows:

Baixe o FFmpeg [aqui](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip)  e extraia o conteúdo.
Adicione o diretório bin do FFmpeg ao PATH do seu sistema.

### Linux/MacOS:

```bash
Copiar código
sudo apt update
sudo apt install ffmpeg
```

## **Uso**
## **1. Rodando o servidor**

### Windows:

```bash
Copiar código
python -m uvicorn app:app --reload
```
### Linux/MacOS:
```bash
Copiar código
python3 -m uvicorn app:app --reload
```
### **Isso iniciará o servidor localmente na URL http://127.0.0.1:8000.**

## **2. Endpoint para download da playlist**
### Você pode fazer uma requisição POST para o endpoint /download_playlist/, fornecendo a URL da playlist do YouTube que deseja baixar.

### **Exemplo de requisição:**
```bash
POST http://127.0.0.1:8000/download_playlist/

{
  "playlist_url": "https://www.youtube.com/playlist?list=OLAK5uy_mxLRWtpm13rbHsw05VcE8-qwJON6DFoTc"
}
```

![App Screenshot](https://iili.io/2OZtXlp.png) 

### Isso irá baixar a playlist em formato MP3.

## **3. Erros de download**

### Se algum vídeo da playlist for privado ou não estiver disponível, o download continuará para os próximos vídeos, e o erro será registrado em um arquivo de log chamado yt_dlp_errors.log.