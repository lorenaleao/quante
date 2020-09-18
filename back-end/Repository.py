# Standard import libraries
import pathlib
import sys
import os
from string import ascii_letters, digits
from random import choice

# Third party libaries
from google.cloud import storage

class RepositoryBase():
    
    @staticmethod
    def _get_random_string(size = 32):
        return ''.join(choice(ascii_letters + digits) for i in range(size))

    def save(self, file) -> str:
        raise NotImplemented

    def load(self, file_name):
        raise NotImplemented

class LocalRepository(RepositoryBase):
    def __init__(self, repo_base):
        self.repo_base = repo_base
    
    def save(self, file) -> str:
        new_filename = f"{self._get_random_string()}_{file.filename}"
        with open(f"{self.repo_base}{new_filename}", "wb") as img:
            img.write(file.read())
        return new_filename

class ImageGCloudRepository(RepositoryBase):
    def save(self, file) -> str:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secrets/GCredentials.json" 
        client = storage.Client() 
        bucket = client.get_bucket("quante-bucket") 
        blob = bucket.blob(self._get_random_string() + pathlib.Path(file.filename).suffix) 
        blob.upload_from_string(file.read())
        blob.make_public()
        return blob.public_url