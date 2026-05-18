import requests
from requests.auth import HTTPBasicAuth
class AirflowClient:
 def __init__(self, base_url, username, password):
  self.base_url=base_url; self.auth=HTTPBasicAuth(username,password)
 def get_latest_dag_run(self, dag_id):
  r=requests.get(f'{self.base_url}/dags/{dag_id}/dagRuns?limit=1', auth=self.auth, timeout=30)
  r.raise_for_status(); data=r.json().get('dag_runs',[])
  return data[0] if data else None
