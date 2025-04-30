# 📢 Alerta de Pré-Tickets - GLPI

Automação que verifica e a quantidade de **pré-tickets** no GLPI e envia essa informação para um grupo do Telegram utilizando um bot. O objetivo é manter a equipe informada, em tempo real, sobre a fila de chamados que precisam ser direcionados para o setor responsavel.

O script é executado automaticamente a cada 5 minutos via **Agendador de Tarefas do Windows**, rodando em um servidor.

## 📁 Estrutura dos Arquivos

- **main.py**  
  Arquivo principal que orquestra a execução das funções e classes do projeto.

- **glpi_bot.py**  
  Realiza o acesso à URL dos pré-tickets no GLPI, analisa a tabela e retorna a **quantidade atual de pré-tickets** registrados.

- **alermigo_bot.py**  
  Envia a informação obtida (número de pré-tickets) para um grupo do Telegram usando um bot previamente configurado.

## ⚙️ Funcionamento

1. O `glpi_bot.py` acessa a página dos pré-tickets no GLPI e conta quantos registros há na tabela.
2. O `alermigo_bot.py` envia essa quantidade para o grupo do Telegram via bot.
3. O `main.py` centraliza o processo.
4. O script é executado automaticamente a cada 5 minutos pelo Agendador de Tarefas do Windows.

## 💡 Observações

- Ideal para equipes de suporte que precisam de **monitoramento contínuo** da fila de atendimento.
- Evita que pré-tickets passem despercebidos ou fiquem muito tempo sem atenção.
- Simples, direto e com impacto real na agilidade da triagem.

---

Automação criada para **facilitar o acompanhamento de chamados no GLPI** e agilizar a comunicação interna da equipe.
