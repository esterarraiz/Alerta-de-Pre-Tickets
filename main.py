from glpi_bot import GLPIBot
from alermigo_bot import AlermigoBot

usuario = "Seu usuario"
senha= "sua_senha"

glpi = GLPIBot(usuario, senha)
glpi.login()

preticket = glpi.extrair_chamados()
print(f"Total de pré-tickets encontrados: {preticket}")
link="Link para mensagem que será enviada pelo BOT"

if preticket > 0:
    bot = AlermigoBot(token='Token_do_BOT', chat_id='ID_do_chat')
    mensagem = bot.formatar_mensagem(preticket, link)
    bot.enviar_mensagem(mensagem)
else:
    print("Nenhum chamado encontrado.")
