from machinetranslation import french_to_english, english_to_french
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = english_to_french(textToTranslate)
    if translation==None:
        return "Failed to translate " + textToTranslate
    return translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = french_to_english(textToTranslate)
    if translation==None:
        return "Echec de traduction pour " + textToTranslate
    return translation


@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
