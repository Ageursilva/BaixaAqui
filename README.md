
## BaixeAqui - Fork com Interface Gráfica
Este é um fork do projeto original BaixeAqui, com a adição de uma interface gráfica intuitiva para facilitar o download de playlists e musicas do YouTube em formato MP3.
## Alterações Principais
-   Adição de interface gráfica utilizando Jinja2 e FastAPI
-   Suporte a downloads via formulário (Form-Data)
-   Manutenção das funcionalidades originais de download de playlists
## Requisitos
Para instalar as dependências necessárias, execute:
```
pip install -r requirements.txt
```
## Instalação
-   Clonar repositório: `git clone https://github.com/Ageursilva/BaixaAqui.git`
-  Acessar a pasta:`cd BaixeAqui`
-   Instalar dependências: `pip install -r requirements.txt`
-   Instalar FFmpeg: 
-   Windows: Baixe [aqui](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip) e adicione ao PATH. 
-   Linux/MacOS: `sudo apt update && sudo apt install ffmpeg`   
## Uso
## Interface Web

-   Rodar servidor: `python -m uvicorn app:app --reload` (Windows) ou `python3 -m uvicorn app:app --reload` (Linux/MacOS) 
-   Acessar: `http://127.0.0.1:8000`
-   Inserir URL da playlist no formulário

![Interface](https://iili.io/2kCgIjV.png)   
## API (Form-Data)

-   Endpoint: `POST /download_playlist/`
-   Parâmetro: `playlist_url` (Form-Data)    
-   Exemplo de requisição: 

```
POST http://127.0.0.1:8000/download_playlist/

Content-Type: application/x-www-form-urlencoded

playlist_url=https://www.youtube.com/playlist?list=OLAK5uy_mxLRWtpm13rbHsw05VcE8-qwJON6DFoTc
```
![Api](https://iili.io/2kCN9FR.png)
##  Erros de download
 Se algum vídeo da playlist for privado ou não estiver disponível, o download continuará para os próximos vídeos, e o erro será registrado em um arquivo de log chamado **yt_dlp_errors.log**.
## Créditos
-   Projeto original: [BaixeAqui](https://github.com/Rivaldo12/BaixaAqui)
-   Desenvolvedor do fork: [Ageu Silva](https://ageursilva.github.io/)  
## Desenvolvimento

-   Clonar repositório: `git clone https://github.com/seu_usuario/baixeaqui-fork.git`
-   Instalar dependências: `pip install -r requirements.txt`    
-   Executar projeto: `python -m uvicorn app:app --reload`