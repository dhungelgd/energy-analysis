import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # go up from src/ to repo root

def get_data_path(*parts):
    return os.path.join(BASE_DIR, "data", *parts)