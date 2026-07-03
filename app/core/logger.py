from loguru import logger
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
os.makedirs(LOG_PATH, exist_ok=True)

logger.add(os.path.join(LOG_PATH, "app.log"), rotation="1 MB", retention="7 days")