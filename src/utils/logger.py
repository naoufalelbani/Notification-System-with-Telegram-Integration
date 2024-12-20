import logging
import os
from config import LOG_LEVEL

if not os.path.exists("logs"):
  os.makedirs("logs")
  
def get_logger(name:str, filename:str="app.log"):
  logger = logging.getLogger(name)
  logger.setLevel(LOG_LEVEL)
  
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)
  
  file_handler = logging.FileHandler(f'logs/{filename}')
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)
  
  # Avoid duplicate logs
  logger.propagate = False
  
  return logger
