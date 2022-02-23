from distutils.log import debug
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getBin/<string:text>')
def get_bin(text):
    # Se reempla el _ por un espacio
    text = text.replace("_", " ")
    bin = ""

    for s in text:
        bin += " " + decimal_to_bin(ord(s))

    return jsonify({ "binario" : bin})

# Funcion para convertir un decimal a binario
def decimal_to_bin(decimal):
    bin = ""

    if decimal > 0:
        while decimal > 0:
            if decimal % 2 == 0: bin += "0"
            else: bin += "1"

            decimal = int(decimal / 2)
    else:
        bin = "0"
        
    return "0" + bin[::-1]

if __name__ == '__main__':
    app.run(debug = True)