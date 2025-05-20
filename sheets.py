import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Carrega credenciais do JSON da variável de ambiente
creds_dict = json.loads(os.getenv("GOOGLE_CREDS_JSON"))

# Define escopos corretos (sheets + drive)
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Autenticação com Google
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
gc = gspread.authorize(creds)

# Abre a planilha e aba
sheet = gc.open(os.getenv("GOOGLE_SHEET_NAME")).worksheet("Mensagens")

# Função de gravação no Google Sheets
def salvar_no_sheets(data, numero, original, topicos, plano):
    sheet.append_row([
        data.strftime('%d/%m/%Y %H:%M'),
        numero,
        original,
        topicos,
        plano
    ])