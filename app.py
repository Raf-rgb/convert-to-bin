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

@app.route('/getText/<string:bin>')
def get_text(bin):
    # Se obtiene una lista de los numeros
    # binarios con la funcino split
    bins = bin.split("_")

    text = ""

    for b in bins:
        text += chr(bin_to_decimal(b))

    return jsonify({ "texto" : text})

# Funcion para convertir un decimal a binario
def bin_to_decimal(bin):
    pos = 0
    decimal = 0

    # Se invierte el arreglo para recorrerlo de derecha a izquierda
    bin = bin[::-1]

    for d in bin:
        # Se eleva el 2 a la posicion
        mult = 2**pos

        # Se acumula la multiplicacion del digito del arreglo
        # por multiplicador
        decimal += int(d) * mult
        
        # Se aumenta la posicion del arreglo
        pos += 1
    return decimal

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