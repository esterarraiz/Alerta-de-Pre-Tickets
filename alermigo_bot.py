import requests
from datetime import datetime

class AlermigoBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f'https://api.telegram.org/bot{self.token}/sendMessage'

    def formatar_mensagem(self, quant, link):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        plural = "s" if quant > 1 else ""
        mensagem = (
            f"🚨 *Alerta de Pré-Ticket*\n"
            f"📅 _{agora}_\n\n"
            f"Há *{quant}* pré-ticket{plural} no GLPI aguardando análise.\n"
            f"🔗 [Acessar chamados]({link})"
        )
        return mensagem


    def enviar_mensagem(self, mensagem):
        payload = {
            'chat_id': self.chat_id,
            'text': mensagem,
            'parse_mode': 'Markdown'
        }
        try:
            response = requests.post(self.api_url, data=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
