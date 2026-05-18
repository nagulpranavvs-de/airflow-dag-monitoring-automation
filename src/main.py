from config.settings import Settings
from services.airflow_client import AirflowClient
from services.report_generator import ReportGenerator
from services.email_service import EmailService
from utils.logger import get_logger
logger=get_logger()
def main():
 client=AirflowClient(Settings.AIRFLOW_BASE_URL,Settings.AIRFLOW_USERNAME,Settings.AIRFLOW_PASSWORD)
 report_generator=ReportGenerator(); email_service=EmailService(Settings.GMAIL_EMAIL,Settings.GMAIL_APP_PASSWORD)
 dag_results=[]
 for dag_id in Settings.DAG_LIST:
  try:
   run=client.get_latest_dag_run(dag_id)
   dag_results.append({'dag_id':dag_id,'state':run.get('state') if run else 'NO_RUN','start_date':run.get('start_date') if run else 'N/A'})
  except Exception as e:
   logger.error(str(e))
 report_path=report_generator.generate(dag_results)
 html=open(report_path,encoding='utf-8').read()
 email_service.send_email(Settings.RECIPIENT_EMAIL,'Airflow DAG Monitoring Report',html)
if __name__=='__main__': main()
