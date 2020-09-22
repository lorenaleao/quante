# Standard import libraries
import pathlib
import sys
import os
from string import ascii_letters, digits
from random import choice

class RepositoryBase():
    
    @staticmethod
    def _get_random_string(size = 32):
        return ''.join(choice(ascii_letters + digits) for i in range(size))

    def save(self, file) -> str:
        raise NotImplementedError

    def load(self, file_name):
        raise NotImplementedError

class LocalRepository(RepositoryBase):
    def __init__(self, repo_base):
        self.repo_base = repo_base
    
    def save(self, file) -> str:
        new_filename = f"{self._get_random_string()}_{file.filename}"
        with open(f"{self.repo_base}{new_filename}", "wb") as img:
            img.write(file.read())
        return new_filename
    
    def load(self, file_name):
        with open(f"{self.repo_base}{file_name}", "rb") as img:
            return img.read()