import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Carrega credenciais do JSON vindo da variável de ambiente
creds_dict = json.loads(os.getenv("GOOGLE_CREDS_JSON"))
creds = Credentials.from_service_account_info(creds_dict)

# Autentica com o Google Sheets
gc = gspread.authorize(creds)

# Abre a planilha e aba
sheet = gc.open(os.getenv("GOOGLE_SHEET_NAME")).worksheet("Mensagens")

# Função de salvamento
def salvar_no_sheets(data, numero, original, topicos, plano):
    sheet.append_row([
        data.strftime('%d/%m/%Y %H:%M'),
        numero,
        original,
        topicos,
        plano
    ])