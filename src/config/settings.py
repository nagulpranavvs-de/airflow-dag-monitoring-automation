import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
 AIRFLOW_BASE_URL=os.getenv('AIRFLOW_BASE_URL')
 AIRFLOW_USERNAME=os.getenv('AIRFLOW_USERNAME')
 AIRFLOW_PASSWORD=os.getenv('AIRFLOW_PASSWORD')
 GMAIL_EMAIL=os.getenv('GMAIL_EMAIL')
 GMAIL_APP_PASSWORD=os.getenv('GMAIL_APP_PASSWORD')
 RECIPIENT_EMAIL=os.getenv('RECIPIENT_EMAIL')
 DAG_LIST=[d.strip() for d in os.getenv('DAG_LIST','').split(',') if d.strip()]
