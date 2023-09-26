import os
import sys

try:
    import pytz
except (ModuleNotFoundError, ImportError):
    print("pytz module not found, attempting to install...")
    os.system(f"{sys.executable} -m pip install -U pytz")
finally:
    import pytz
    
try:
    import requests
except (ModuleNotFoundError, ImportError):
    print("requests module not found, attempting to install...")
    os.system(f"{sys.executable} -m pip install -U requests")
finally:
    import requests
    
from datetime import datetime
import urllib.parse

class TimestampedLogger:
    def __init__(self, tg_bot_token=None, tg_chat_id=None):
        self.timezone = pytz.timezone('Asia/Kolkata')
        self.counter = 0
        self.tg_bot_token = tg_bot_token
        self.tg_chat_id = tg_chat_id

    def _timenow(self):
        return datetime.now(pytz.timezone('UTC')).astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    def log(self, message):
        timestamp = self._timenow()
        self.counter += 1
        formatted_message = f"{timestamp} #{self.counter}# {message}"
        print(formatted_message)
        return formatted_message

    def tgsend(self, message):
        formatted_message = self.log(message)
        if self.tg_bot_token is not None and self.tg_chat_id is not None:
            message_text_encoded = urllib.parse.quote(formatted_message)
            tg_url = f'https://api.telegram.org/bot{self.tg_bot_token}/sendMessage?chat_id={self.tg_chat_id}&text={message_text_encoded}'

            try:
                response = requests.get(tg_url)
                response.raise_for_status()  # Raise an exception for non-200 response codes
            except requests.exceptions.RequestException as e:
                print(f"Error sending message to Telegram: {e}")

# Usage example:
# logger = TimestampedLogger()
# logger.log("Print message to Terminal Only.")
# logger.tgsend("Print message to Terminal Only as Telegram credentials are not passed.")

# logger = TimestampedLogger(tg_bot_token="YOUR_BOT_TOKEN", tg_chat_id="YOUR_CHAT_ID")
# logger.log("Print message to Terminal Only.")
# logger.tgsend("Print message to Terminal and send same message to Telegram also.")
