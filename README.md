# Flask App con Google Secret Manager

Este proyecto es una aplicación Flask que obtiene datos almacenados en **Google Secret Manager** y los muestra en una página web.

## Requisitos

### 1. Herramientas necesarias
- Python 3.8 o superior
- Google Cloud SDK instalado y autenticado
- Una cuenta de Google Cloud con un proyecto activo
- `gcloud` configurado con el proyecto correcto
- Permisos para acceder a Google Secret Manager

### 2. Librerías necesarias
Instala las dependencias con:
```sh
pip install flask google-cloud-secret-manager
```

## Configuración en Google Cloud

### 1. Habilitar Secret Manager
Asegúrate de que **Secret Manager** esté habilitado en tu proyecto:
```sh
gcloud services enable secretmanager.googleapis.com
```

### 2. Crear un secreto en Google Secret Manager
Ejecuta este comando para crear el secreto:
```sh
echo '{"DIA_SECRETO": "10", "MES_SECRETO": "Marzo", "AÑO_SECRETO": "2025"}' | \
gcloud secrets create test-base-secret --replication-policy="automatic" --data-file=-
```

Si ya existe y quieres actualizarlo:
```sh
echo '{"DIA_SECRETO": "15", "MES_SECRETO": "Abril", "AÑO_SECRETO": "2026"}' | \
gcloud secrets versions add test-base-secret --data-file=-
```

### 3. Asignar permisos a la cuenta de servicio
Si ejecutas en **Cloud Run**, **Cloud Functions** o **Compute Engine**, debes asignar el rol `Secret Manager Secret Accessor` a la cuenta de servicio:
```sh
gcloud projects add-iam-policy-binding [PROJECT_ID] --member=serviceAccount:[SERVICE_ACCOUNT] --role=roles/secretmanager.secretAccessor
```
Reemplaza `[PROJECT_ID]` con tu ID de proyecto y `[SERVICE_ACCOUNT]` con el email de la cuenta de servicio.

## Ejecutar la aplicación

1. Clona este repositorio:
```sh
git clone https://github.com/tu-repo/flask-secret-manager.git
cd flask-secret-manager
```
2. Ejecuta el servidor Flask:
```sh
python app.py
```
3. Abre el navegador en `http://127.0.0.1:8080/`

## Desplegar en Cloud Run

1. **Autenticar Docker en Google Cloud**
```sh
gcloud auth configure-docker
```

2. **Construir la imagen con Cloud Build**
```sh
gcloud builds submit --tag gcr.io/[PROJECT_ID]/flask-secret-app
```

3. **Desplegar en Cloud Run**
```sh
gcloud run deploy flask-secret-app --image gcr.io/[PROJECT_ID]/flask-secret-app --platform managed --allow-unauthenticated --region us-central1
```
Reemplaza `[PROJECT_ID]` con tu ID de proyecto.

## Notas
- Si la aplicación no muestra los valores esperados, verifica los permisos de Secret Manager.
- Usa `gcloud secrets versions access latest --secret=test-base-secret` para verificar el contenido del secreto.
- Para registrar logs en Cloud Run, revisa `gcloud logging read "resource.type=cloud_run_revision"`.

## Licencia
Este proyecto está bajo la licencia MIT.

