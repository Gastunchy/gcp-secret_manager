from flask import Flask, render_template_string
import json
from google.cloud import secretmanager

app = Flask(__name__)

def load_secret():
    """Carga el secreto desde Google Secret Manager."""
    client = secretmanager.SecretManagerServiceClient()
    secret_name = "projects/488709866434/secrets/test-base-secret/versions/latest"
    try:
        secret = client.access_secret_version(request={"name": secret_name}).payload.data.decode("UTF-8")
        return json.loads(secret)  # Retorna como diccionario
    except Exception:
        return {}  # Devuelve un diccionario vacío si falla

secreto = load_secret()

@app.route('/')
def mostrar_contenido():
    """Muestra los valores del secreto en una página HTML simple."""
    contenido = f"""
    <h1>Contenido del Secreto</h1>
    <p>Día: {secreto.get('DIA_SECRETO', 'No definido')}</p>
    <p>Mes: {secreto.get('MES_SECRETO', 'No definido')}</p>
    <p>Año: {secreto.get('AÑO_SECRETO', 'No definido')}</p>
    """
    return render_template_string(contenido)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
