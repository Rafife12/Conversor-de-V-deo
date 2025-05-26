# 🎧 YouTube to Audio Converter

Um conversor simples de vídeos do YouTube para arquivos de áudio (MP3, WAV, AAC, OGG) com uma interface web moderna feita em Flask + TailwindCSS.

## 🚀 Funcionalidades

- ✅ Conversão de vídeos do YouTube para áudio.
- ✅ Suporte aos formatos: **MP3**, **WAV**, **AAC** e **OGG**.
- ✅ Interface responsiva e moderna.
- ✅ Download direto do áudio convertido.

## 🖥️ Tecnologias Utilizadas

- Python
- Flask
- PyTube
- PyDub
- Tailwind CSS
- FFmpeg (para conversão de áudio)

---

## 📦 Instalação e Uso

### 🔧 Pré-requisitos

- Python instalado (3.8 ou superior)
- FFmpeg instalado e configurado no PATH  
→ Download: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- Git instalado (opcional, para clonar)

### 🚀 Clonar o projeto

```bash
git clone https://github.com/seu-usuario/youtube-to-audio.git
cd youtube-to-audio
```

### ⚙️ Instalar as dependências

```bash
pip install -r requirements.txt
```

### ▶️ Rodar a aplicação

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 📂 Estrutura de Pastas

```
youtube-to-audio/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── downloads/ (gerada automaticamente)
```

---

## 📝 Licença

Este projeto é de livre uso para fins de estudo.  
⚠️ **Respeite os direitos autorais dos conteúdos do YouTube.**

---

## 🤝 Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests!  
💡 Sugestões de melhorias são muito bem-vindas.

---

## 💻 Desenvolvido por

**Seu Nome** — [@seu-usuario](https://github.com/seu-usuario)
