import logging
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime("%Y-%b-%d-%H-%M-%S")}.log"
# print(LOG_FILE)

logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok = True)
# print(logs_path)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
# print(LOG_FILE_PATH)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


