from core.login import login_whatsapp
from core.extractor import extract_containers
from datetime import datetime
import time
from selenium.webdriver.common.by import By

print("=" * 60)
print("📦 BOT DO PÃO - CLASSIFYING MESSAGES")
print("📌 Each execution creates a new file")
print("=" * 60)

driver = login_whatsapp()

if driver:
    print("\n✅ LOGIN SUCCESSFUL!")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"classified_{timestamp}.xlsx"
    print(f"📂 Session file: {filename}")

    print("🔄 Starting loop...\n")

    try:
        while True:
            try:
                close_popup = driver.find_element(
                    By.XPATH, "//div[@role='button' and @aria-label='Fechar']"
                )
                close_popup.click()
                print("   🔔 Pop-up closed!")
                time.sleep(1)
            except:
                pass

            extract_containers(driver, filename)
            print("⏳ Waiting 10 seconds...\n")
            time.sleep(10)
    except KeyboardInterrupt:
        driver.quit()
        print("\n👋 Bot stopped.")
else:
    print("❌ Login failed.")
