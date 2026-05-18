import logging, os
os.makedirs('logs', exist_ok=True)
def get_logger():
 logger=logging.getLogger('dag_monitor')
 if not logger.handlers:
  logger.setLevel(logging.INFO)
  fh=logging.FileHandler('logs/app.log')
  logger.addHandler(fh)
 return logger
