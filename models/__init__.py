"""The __init__ method for models directory"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()