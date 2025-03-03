from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def mostrar_contenido():
    dia = os.getenv('DIA')
    mes = os.getenv('MES')
    año = os.getenv('AÑO')
    
    contenido = f"""
    <h1>Contenido de las Variables de Entorno</h1>
    <p>Día: {dia}</p>
    <p>Mes: {mes}</p>
    <p>Año: {año}</p>
    """
    return render_template_string(contenido)

if __name__ == '__main__':
    app.run(debug=True)