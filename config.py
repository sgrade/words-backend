
from google.cloud import firestore

# Import data from the Firestore
# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()
# Read 
words_ref = db.collection(u'words')
words_docs = words_ref.stream()
# Fill the dict
words = dict()
for doc in words_docs:
    words[doc.id] = doc.to_dict()
    words[doc.id]['id'] = doc.id

