import sys
import os
from decouple import AutoConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ADD PATHS
PATH_RROTOBUFS = os.path.join(BASE_DIR,'protobufs')

LIST_PATH_TO_ADD=[
    PATH_RROTOBUFS
]

sys.path.extend(LIST_PATH_TO_ADD)

# IMPORT ENVIROMENT VARIABLES
PATH_FILE_ENV = os.path.join(BASE_DIR,'kernel')
config = AutoConfig(search_path=PATH_FILE_ENV)
    