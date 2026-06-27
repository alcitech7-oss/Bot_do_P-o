# 🍞 Bot do Pão

Bot que lê mensagens do WhatsApp Web e salva automaticamente em uma planilha Excel, identificando remetente e mensagem.

## 🚀 Funcionalidades

- Login automático no WhatsApp Web
- Leitura de mensagens em loop
- Captura do número do remetente
- Filtro de mensagens repetidas e lixo (menus, horários, datas)
- Salva em planilha Excel (.xlsx)

## 🛠️ Tecnologias

- Python 3.10+
- Selenium
- OpenPyXL
- WebDriver Manager

## 📦 Como instalar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/bot_do_pao.git
cd bot_do_pao

2. Crie e ative um ambiente virtual:

bash
python -m venv venv
venv\Scripts\activate

3. Instale as dependências:

bash
pip install -r requirements.txt


▶️ Como rodar
bash
python main.py
📂 Como funciona o código
main.py: orquestrador principal

core/login.py: responsável pelo login no WhatsApp

core/escritor_master.py: lê os spans, filtra lixo e salva na planilha

🧪 Status do projeto
✅ Leitura de mensagens e remetente
✅ Filtro de lixo (menus, horários, datas)
✅ Loop contínuo (a cada 15 segundos)
⚠️ Tratamento de arquivo Excel aberto (em andamento)

📌 Próximos passos
Classificação de mensagens (cliente, entregador, fornecedor)

Respostas automáticas

Interface gráfica simples

🤝 Contribuição
Este projeto é open source. Sinta-se à vontade para contribuir!
