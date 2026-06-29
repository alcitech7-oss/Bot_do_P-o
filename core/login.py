from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


def login_whatsapp():
    print("   🔐 Iniciando módulo de login...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com")
    print("   📱 QR Code carregado. Aguardando login...")

    logado = False
    tentativas = 0
    while not logado:
        try:
            driver.find_element(By.XPATH, "//div[@role='row']")
            logado = True
            print("   ✅ LOGIN DETECTADO!")
            return driver
        except NoSuchElementException:
            tentativas += 1
            print(f"   ⏳ Aguardando... ({tentativas}s)", end="\r")
            time.sleep(1)
    return None
