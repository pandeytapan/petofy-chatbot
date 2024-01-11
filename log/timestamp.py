import logging
 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
file_handler = logging.FileHandler('/home/anmol/Desktop/Petofy-chatbot/log/all_logs')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)