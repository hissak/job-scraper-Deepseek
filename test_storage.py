import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(url, key)

bucket = "resumes"  # or whatever your bucket is named
file_name = "resume.pdf"

try:
    # Attempt to download the file
    data = supabase.storage.from_(bucket).download(file_name)
    print(f"Success! Downloaded {len(data)} bytes.")
except Exception as e:
    # Print the full exception details
    print(f"Exception type: {type(e)}")
    print(f"Exception args: {e.args}")
    # If it's a dictionary-like object, try to see its content
    if hasattr(e, '__dict__'):
        print(f"Exception dict: {e.__dict__}")
    # For Supabase storage errors, try to get the response
    if hasattr(e, 'response'):
        print(f"Response status: {e.response.status_code}")
        print(f"Response text: {e.response.text}")
