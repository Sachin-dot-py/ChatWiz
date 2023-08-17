from flask import Flask, jsonify, request, render_template, Markup
import os
import zipfile
from whatsapp import WhatsAppAnalyzer

app = Flask(__name__)


@app.route('/whatsapp', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("whatsapp_index.html")
    else:
        file = request.files['chat']
        name = file.filename.split(".zi")[0].split(" - ")[1]
        file_like_object = file.stream._file
        zipfile_ob = zipfile.ZipFile(file_like_object)
        file_names = zipfile_ob.namelist()
        # Filter names to only include the filetype that you want:
        file_names = [file_name for file_name in file_names if file_name.endswith(".txt")]
        content = [zipfile_ob.open(name).read() for name in file_names][0]
        content = content.decode("utf-8")
        analysis = WhatsAppAnalyzer(content=content)
        return render_template("whatsapp_analysis.html", analysis=analysis, emojidf=list(analysis.emojidf[:20]), worddf=list(analysis.worddf.items())[:20], wordcloud=Markup(analysis.wordcloud()), name=name)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
