import os
import json
from google.oauth2.service_account import Credentials

creds_dict = json.loads(os.getenv("GOOGLE_CREDS_JSON"))
creds = Credentials.from_service_account_info(creds_dict)

gc = gspread.authorize(creds)