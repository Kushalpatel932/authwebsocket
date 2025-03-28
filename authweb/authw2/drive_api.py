

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def upload_to_drive(credentials_dict, file_path):
    creds = Credentials.from_authorized_user_info(credentials_dict)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {"name": file_path.split("/")[-1]}
    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(body=file_metadata, media_body=media).execute()
    return file.get("id")
