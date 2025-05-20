from flask import Flask, request, jsonify
from gpt import analisar_como_ceo
from sheets import salvar_no_sheets
from datetime import datetime

app = Flask(__name__)

NUMERO_ORIGEM = '5511976643447'  # sem + ou "whatsapp:"

@app.route('/webhook', methods=['POST'])
def receber_mensagem():
    dados = request.json
    try:
        numero_remetente = dados['message']['from']
        mensagem = dados['message']['body']

        print(f"📨 Mensagem recebida de {numero_remetente}: {mensagem}")

        if numero_remetente == NUMERO_ORIGEM:
            resposta = analisar_como_ceo(mensagem)
            salvar_no_sheets(
                datetime.now(),
                numero_remetente,
                mensagem,
                resposta.get('topicos', ''),
                resposta.get('plano', '')
            )
            print("✅ Mensagem processada e registrada")
        else:
            print("⚠️ Número não autorizado. Ignorado.")

    except Exception as e:
        print(f"❌ Erro ao processar mensagem: {e}")

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)