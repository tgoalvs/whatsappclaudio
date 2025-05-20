import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Credenciais e escopos
creds_dict = json.loads(os.getenv("GOOGLE_CREDS_JSON"))
scopes = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

# Autenticação e planilha
gc = gspread.authorize(creds)
sheet = gc.open(os.getenv("GOOGLE_SHEET_NAME")).worksheet("Mensagens")

# Função de escrita
def salvar_no_sheets(data, numero, original, topicos, plano):
    sheet.append_row([
        data.strftime('%d/%m/%Y %H:%M'),
        numero,
        original,
        topicos,
        plano
    ])