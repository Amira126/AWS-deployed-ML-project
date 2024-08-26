import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Creating a directory path; current working directory, create "logs" directory, filename
LOG_PATH=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(LOG_PATH, exist_ok=True)


LOG_FILE_Path = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_Path,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")