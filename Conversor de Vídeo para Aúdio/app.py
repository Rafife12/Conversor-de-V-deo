from flask import Flask, render_template, request, send_file
from pytube import YouTube
from pydub import AudioSegment
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_type = request.form['format']

    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        out_file = audio_stream.download(output_path=DOWNLOAD_FOLDER)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.' + format_type

        audio = AudioSegment.from_file(out_file)
        audio.export(new_file, format=format_type)
        os.remove(out_file)  

        filename = os.path.basename(new_file)

        return send_file(new_file, as_attachment=True, download_name=filename)

    except Exception as e:
        return f"""
        <h1>Ocorreu um erro:</h1>
        <p>{str(e)}</p>
        <a href="/">Voltar</a>
        """


if __name__ == '__main__':
    app.run(debug=True)
