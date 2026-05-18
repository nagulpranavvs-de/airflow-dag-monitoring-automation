from jinja2 import Environment, FileSystemLoader
class ReportGenerator:
 def __init__(self, template_dir='templates'):
  self.env=Environment(loader=FileSystemLoader(template_dir))
 def generate(self, dag_data):
  template=self.env.get_template('report_template.html')
  html=template.render(dag_data=dag_data)
  path='reports/generated_report.html'
  open(path,'w',encoding='utf-8').write(html)
  return path
