# TimestampedLogger

# Usage example:

# Method 1:
# logger = TimestampedLogger()
# logger.log("Print message to Terminal Only.")
# logger.tgsend("Print message to Terminal Only as Telegram credentials are not passed.")

# Method 2:
# logger = TimestampedLogger(tg_bot_token="YOUR_BOT_TOKEN", tg_chat_id="YOUR_CHAT_ID")
# logger.log("Print message to Terminal Only.")
# logger.tgsend("Print message to Terminal and send same message to Telegram also.")
