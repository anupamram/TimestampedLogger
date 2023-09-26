from TimestampedLogger import TimestampedLogger

tg_bot_token = 'YOUR_BOT_TOKEN'
tg_chat_id = 'YOUR_CHAT_ID'

logger = TimestampedLogger(tg_bot_token=tg_bot_token, tg_chat_id=tg_chat_id)

logger.log("Print message to Terminal Only.") 
# 2023-09-26 19:50:25.272 #1# Print message to Terminal Only.   

logger.tgsend("Print message to Terminal and send same message to Telegram also.")
# 2023-09-26 19:50:25.273 #2# Print message to Terminal and send same message to Telegram also.