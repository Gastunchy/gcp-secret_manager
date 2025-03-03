from flask import Flask, render_template_string
import os
from google.cloud import secretmanager

app = Flask(__name__)

# Función para cargar el secreto desde Google Secret Manager
def load_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    secret = client.access_secret_version(request={"name": secret_name}).payload.data.decode("UTF-8")
    return json.loads(secret)

secreto = load_secret("projects/488709866434/secrets/test-base-secret/versions/2")


@app.route('/')
def mostrar_contenido():
    dia = os.getenv('DIA')
    mes = os.getenv('MES')
    año = os.getenv('AÑO')
    secreto_dia = secreto.get('DIA_SECRETO')
    secreto_mes = secreto.get('MES_SECRETO')
    secreto_año = secreto.get('AÑO_SECRETO')
    
    contenido = f"""
    <h1>Contenido de las Variables de Entorno</h1>
    <p>Día: {dia}</p>
    <p>Mes: {mes}</p>
    <p>Año: {año}</p>
    <p>Dia del secreto: {secreto_dia}</p>
    <p>Mes del secreto: {secreto_mes}</p>
    <p>Año del secreto: {secreto_año}</p>
    """
    return render_template_string(contenido)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)