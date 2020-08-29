from string import ascii_letters, digits
from random import choice
import pathlib
import sys

import os
from google.cloud import storage

class ImageRepository():
    def __init__(self, dirBase : str, sizeName = 32):
        self.dirBase = dirBase
        self.sizeName = sizeName

    def __getRandomString(self, size = 32):
        return ''.join(choice(ascii_letters + digits) for i in range(32))

    def save(self, file) -> str:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secrets/GCredentials.json" #Set gloud credentials.
        client = storage.Client() #Set gcloud client.
        bucket = client.get_bucket("quante-bucket") #Specify gcloud bucket.
        blob = bucket.blob(self.__getRandomString() + pathlib.Path(file.filename).suffix) #Set filename format (uploads/year/month/filename).
        blob.upload_from_string(file.read())
        blob.make_public()
        return blob.public_url