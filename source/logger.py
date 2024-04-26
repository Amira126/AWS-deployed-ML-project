import logging
import os
from datetime import datetime

#Filename
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Creating a directory path; current working directory, create "logs" directory, filename
LOG_FILE_PATH=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(LOG_FILE_PATH, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO
)