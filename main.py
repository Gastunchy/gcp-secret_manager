from flask import Flask, jsonify
from google.cloud import secretmanager
import os

app = Flask(__name__)

@app.route('/')
def access_secret():
    try:
        client = secretmanager.SecretManagerServiceClient()
        secret_name = "projects/488709866434/secrets/test-base-secret/versions/lates"
        secret = client.access_secret_version(request={"name": secret_name}).payload.data.decode("UTF-8")
        return jsonify({"secret": secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))