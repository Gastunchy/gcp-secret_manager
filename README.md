# Secret Manager Demo en GCP con Cloud Run

Este proyecto es un MVP que utiliza Google Cloud Secret Manager y Cloud Run para desplegar una aplicación web mínima que muestra el valor de un secreto o cualquier error que ocurra.

## Prerrequisitos

1. **Cuenta de Google Cloud Platform (GCP)**: Debes tener una cuenta en GCP.
2. **Proyecto en GCP**: Debes tener un proyecto creado en GCP.
3. **Google Cloud SDK**: Debes tener instalado y configurado el Google Cloud SDK en tu máquina local.
4. **Python**: Debes tener Python instalado en tu máquina local.

## Paso 1: Configurar Secret Manager

1. **Habilitar Secret Manager API**:
   - Ve a la consola de GCP.
   - Navega a "APIs & Services" > "Library".
   - Busca "Secret Manager API" y haz clic en "Enable".

2. **Crear un secreto**:
   - Ve a la consola de GCP.
   - Navega a "Secret Manager".
   - Haz clic en "Create Secret".
   - Ingresa un nombre para el secreto (por ejemplo, `test-base-secret`).
   - Ingresa el valor del secreto.
   - Haz clic en "Create".

## Paso 2: Crear el script de Python con Flask

Crea un archivo `main.py` con el siguiente contenido:

```python
from flask import Flask, jsonify
from google.cloud import secretmanager
import os

app = Flask(__name__)

@app.route('/')
def access_secret():
    try:
        client = secretmanager.SecretManagerServiceClient()
        secret_name = "projects/970772571927/secrets/test-base-secret/versions/latest"
        secret = client.access_secret_version(request={"name": secret_name}).payload.data.decode("UTF-8")
        return jsonify({"secret": secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))