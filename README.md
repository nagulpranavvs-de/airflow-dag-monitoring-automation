# Airflow DAG Monitoring & Reporting Automation

A production-style Python automation tool for monitoring Apache Airflow DAG health, generating consolidated HTML reports, and sending automated email alerts for scheduled and failure-triggered monitoring.

This project was designed to reduce manual DAG monitoring effort, improve incident response time, and provide centralized visibility into workflow health for production data pipelines.

---

## Project Overview

Monitoring multiple Airflow DAGs manually becomes inefficient as pipeline count grows.

This project automates DAG health monitoring by:

- Fetching DAG execution metadata from Apache Airflow REST API
- Tracking execution status for multiple DAGs simultaneously
- Collecting failure information and execution timestamps
- Generating a centralized HTML monitoring report
- Sending automated Gmail alerts for scheduled checks and failure scenarios

---

## Features

- Monitor multiple Airflow DAGs simultaneously
- Fetch latest DAG run metadata via Airflow REST API
- Consolidated HTML monitoring dashboard
- Automated Gmail email alerts
- Failure-triggered alert notifications
- Config-driven architecture
- Modular Python code structure
- Logging support

---

## Tech Stack

- Python
- Apache Airflow
- Airflow REST API
- Jinja2
- Gmail SMTP
- Python dotenv
- Logging

---

## Architecture

```text
Apache Airflow
      |
      v
Airflow API Client
      |
      v
DAG Monitoring Logic
      |
      v
HTML Report Generator
      |
      v
Gmail Alert Notification
```

---

## Project Structure

```text
airflow-dag-monitoring-automation/
│
├── src/
│   ├── config/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── templates/
├── reports/
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nagulpranavvs-de/airflow-dag-monitoring-automation.git
cd airflow-dag-monitoring-automation
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file with the following:

```env
AIRFLOW_BASE_URL=http://localhost:8080/api/v1
AIRFLOW_USERNAME=admin
AIRFLOW_PASSWORD=admin
GMAIL_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@gmail.com
DAG_LIST=dag_1,dag_2,dag_3
```

---

## Run Project

```bash
python src/main.py
```

---

## Business Impact

This project helps:

- Reduce manual DAG monitoring effort
- Improve incident response time
- Centralize workflow observability
- Reduce alert noise
- Improve pipeline reliability

---

## Future Enhancements

- Task-level failure diagnostics
- Retry logic
- Docker support
- CI/CD pipeline
- Slack / Teams alerts
- Better dashboard UI

---

## Author

**Nagul Pranav V S**  
Cloud Data Engineer | Google Cloud Certified Professional Data Engineer

GitHub: https://github.com/nagulpranavvs-de  
LinkedIn: https://linkedin.com/in/nagulpranavvs