import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("SUPABASE_URL")
DATABASE_KEY = os.getenv("SUPABASE_KEY")