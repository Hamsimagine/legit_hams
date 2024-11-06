import time
import requests
from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_TOKEN = '6731188785:AAFOA1-ys5S_HvouOcoBDOHOxwfmjHGKIvk'
CHAT_ID = '+6283862870827'
IOT_API_URL ='http://202.152.158.130:8081/dashiotlokal/page/det_pressure/12'

bot = Bot(token=TELEGRAM_TOKEN)

def send_alert(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
    except TelegramError as e:
        print(f"failed to send message: {e}")

def check_iot_status():
    try:
        response = requests.get(IOT_API_URL)
        response.raise_for_status()
        data = response.json()
        last_update_time = data.get('last_update')
        current_time = time.time()
        time_diff = (current_time - last_update_time) / 60

        if time_diff>15:
            send_alert(f"Tidak ada data diterima dari dashboard {int(time_diff)}menit!")
        else:
            print("Data diterima dalam interval yang diharapkan")

    except requests.RequestException as e:
            send_alert(f"Error : Gagal memeriksa Dashboard -{e}")
            print(f"Request error: {e}")

if __name__ == "__main__":
     while True:
          check_iot_status()
          time.sleep(60)
