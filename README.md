# 🍞 Bot do Pão

Bot que lê mensagens do WhatsApp Web, classifica por categoria (Pedido, Reclamação, Entrega, etc.) e salva em planilha Excel.

## 🚀 Funcionalidades
- Login automático via QR Code
- Leitura de mensagens em tempo real
- Classificação com inteligência (spaCy)
- Planilha com abas separadas por categoria
- Filtro de mensagens repetidas

## 🛠️ Tecnologias
- Python 3.10+
- Selenium
- OpenPyXL
- spaCy

## 📦 Como instalar
```bash
git clone https://github.com/seu-usuario/bot_do_pao.git
cd bot_do_pao
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
▶️ Como rodar
bash
python main.py
📂 Estrutura
. main.py: orquestrador

. core/login.py: login no WhatsApp

. core/extrator.py: extrai e classifica mensagens

. core/seletores.py: seletores XPath

📌 Status
✅ Leitura de mensagens
✅ Classificação por categoria
✅ Loop contínuo
⚠️ Ajuste fino da classificação (em andamento)

🤝 Contribuição
Sinta-se à vontade para contribuir!