from dotenv import load_dotenv
import os

load_dotenv()

BACKPACK_API_KEY = os.getenv("BACKPACK_API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
