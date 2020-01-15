# words-backend
Python backend for Words app. 

Hosted on Google Cloud Platform. Uses Google Firestore database for data and Google Cloud Storage for image files. 

swagger-server folder is [auto-generated](https://github.com/sgrade/words-api-python-flask) by Swagger Codegen from [words-api](https://github.com/sgrade/words-api)

# Work with the backend locally
Install swagger_ui and google-cloud-firestore
```
pip install connexion[swagger-ui]
pip install google-cloud-firestore
```

Source credentials for the database. 

Note: The credentials are not included in the repo.

Run the app
```
python main.py
```

# Deploy to Google Cloud
gcloud app deploy

# Relevant GCP docs
## Store images 
https://cloud.google.com/appengine/docs/flexible/python/serving-static-files
## Quickstart with Python and other servers
https://cloud.google.com/firestore/docs/quickstart-servers
## Firestore Python API
https://googleapis.dev/python/firestore/latest/client.html
