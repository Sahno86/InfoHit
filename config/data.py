import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    PHONE = os.getenv("PHONE")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
