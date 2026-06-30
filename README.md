#  selenium_whatsapp_reader

A bot that reads WhatsApp Web messages and automatically saves them to an Excel spreadsheet, identifying the sender and the message content.

## 🚀 Features

- Automatic login to WhatsApp Web
- Continuous message reading loop
- Sender number capture
- Filtering of duplicate messages and "junk" data (menus, timestamps, dates)
- Saves data to an Excel spreadsheet (.xlsx)

## 🛠️ Technologies

- Python 3.10+
- Selenium
- OpenPyXL
- WebDriver Manager

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/alcitech7-oss/selenium_whatsapp_reader.git
cd selenium_whatsapp_reader

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

▶️ How to run
python main.py

📂 How the code works
. main.py: Main orchestrator

. core/login.py: Handles WhatsApp login

. core/escritor_master.py: Reads HTML elements (spans), filters junk data, and saves to the spreadsheet

🧪 Project status
. ✅ Message and sender reading

. ✅ Junk data filtering (menus, timestamps, dates)

. ✅ Continuous loop (every 15 seconds)

. ⚠️ Handling open Excel files (in progress)

✅ Project Status
Project validated and tested in a clean environment (fresh clone).

. ✔️ Dependencies installed successfully

. ✔️ Core features validated

. ✔️ Structure and documentation reviewed

. ✔️ Ready for use and demonstration

📌 Development History
Complete refactoring: "Bot do Pão" with class-based selectors and continuous loop

. Organization: Modular structure with `core/` folder

. Cleanup: Test files removed from the repository

. Documentation: README updated and `requirements.txt` added

. Final validation: Project tested and validated from scratch

📌 Next steps
. Message classification (customer, delivery person, supplier)

. Automatic responses

Simple graphical interface

🤝 Contribution
This project is open source. Feel free to contribute!
