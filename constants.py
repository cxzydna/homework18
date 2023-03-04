"""Constants module"""
import os
from pathlib import Path

CONSTANT_NAME = "value"
THIS_FOLDER = Path(__file__).parent.resolve()
LOG_DIR = os.path.join(THIS_FOLDER, "logs")
SQLITE_DB_NAME = 'sqlite:///movies.db'
