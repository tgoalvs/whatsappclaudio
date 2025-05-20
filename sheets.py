import gspread

gc = gspread.service_account(filename='credentials.json')
sheet = gc.open('Analises WhatsApp').worksheet('Mensagens')

def salvar_no_sheets(data, numero, original, topicos, plano):
    sheet.append_row([
        data.strftime('%d/%m/%Y %H:%M'),
        numero,
        original,
        topicos,
        plano
    ])