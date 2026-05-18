\# Airflow DAG Monitoring \& Reporting Automation



A production-style Python automation tool for monitoring Apache Airflow DAG health, generating consolidated HTML reports, and sending automated email alerts for scheduled and failure-triggered monitoring.



This project was designed to reduce manual DAG monitoring effort, improve incident response time, and provide centralized visibility into workflow health for production data pipelines.



\---



\## Project Overview



Monitoring multiple Airflow DAGs manually becomes inefficient as pipeline count grows. This project automates DAG health monitoring by:



\- Fetching DAG execution metadata from Apache Airflow REST API

\- Tracking execution status for multiple DAGs simultaneously

\- Collecting failure information and execution timestamps

\- Generating a centralized HTML monitoring report

\- Sending automated Gmail alerts for scheduled checks and failure scenarios



This helps data engineering teams proactively monitor pipeline health without manually checking Airflow UI logs.



\---



\## Features



\- Monitor multiple Airflow DAGs simultaneously

\- Fetch latest DAG run metadata via Airflow REST API

\- Consolidated HTML monitoring dashboard

\- Automated Gmail email alerts

\- Scheduled monitoring execution

\- Failure-triggered alert notifications

\- Config-driven architecture using environment variables

\- Modular Python project structure

\- Logging for observability

\- Production-ready code organization



\---



\## Tech Stack



\*\*Programming Language\*\*

\- Python



\*\*Workflow Orchestration\*\*

\- Apache Airflow



\*\*API Integration\*\*

\- Airflow REST API



\*\*Templating\*\*

\- Jinja2



\*\*Email Notifications\*\*

\- Gmail SMTP



\*\*Configuration Management\*\*

\- Python dotenv



\*\*Logging\*\*

\- Python logging module



\---



\## Architecture



```text

&#x20;                   +----------------------+

&#x20;                   |   Apache Airflow     |

&#x20;                   |   DAG Metadata/API   |

&#x20;                   +----------+-----------+

&#x20;                              |

&#x20;                              v

&#x20;                +------------------------------+

&#x20;                |   Airflow Monitoring Client  |

&#x20;                |   Fetch DAG Execution Data   |

&#x20;                +--------------+---------------+

&#x20;                               |

&#x20;                               v

&#x20;                +------------------------------+

&#x20;                |   Data Processing Layer      |

&#x20;                |   Status / Failure Analysis  |

&#x20;                +--------------+---------------+

&#x20;                               |

&#x20;                               v

&#x20;                +------------------------------+

&#x20;                |   HTML Report Generator       |

&#x20;                |   Consolidated Monitoring UI  |

&#x20;                +--------------+---------------+

&#x20;                               |

&#x20;                               v

&#x20;                +------------------------------+

&#x20;                |   Gmail Notification Service |

&#x20;                |   Scheduled / Failure Alerts |

&#x20;                +------------------------------+

```



\---



\## Project Structure



```bash

airflow-dag-monitoring-automation/

│

├── src/

│   ├── config/

│   │   └── settings.py

│   │

│   ├── services/

│   │   ├── airflow\_client.py

│   │   ├── report\_generator.py

│   │   └── email\_service.py

│   │

│   ├── utils/

│   │   └── logger.py

│   │

│   └── main.py

│

├── templates/

│   └── report\_template.html

│

├── reports/

├── tests/

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

```



\---



\## Installation



Clone the repository:



```bash

git clone https://github.com/nagulpranavvs-de/airflow-dag-monitoring-automation.git

cd airflow-dag-monitoring-automation

```



Create virtual environment:



\### Windows

```bash

python -m venv venv

venv\\Scripts\\activate

```



\### Mac/Linux

```bash

python3 -m venv venv

source venv/bin/activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## Configuration



Create `.env` file from template:



```bash

copy .env.example .env

```



Configure:



```env

AIRFLOW\_BASE\_URL=http://localhost:8080/api/v1

AIRFLOW\_USERNAME=admin

AIRFLOW\_PASSWORD=admin



GMAIL\_EMAIL=your\_email@gmail.com

GMAIL\_APP\_PASSWORD=your\_gmail\_app\_password

RECIPIENT\_EMAIL=recipient@gmail.com



DAG\_LIST=dag\_1,dag\_2,dag\_3

```



\---



\## Run the Project



```bash

python src/main.py

```



\---



\## Sample Monitoring Output



Example report includes:



| DAG Name | Status | Start Time |

|--------|--------|------------|

| customer\_ingestion\_dag | success | 2026-05-18 08:30 |

| sales\_etl\_dag | failed | 2026-05-18 08:45 |

| analytics\_refresh\_dag | success | 2026-05-18 09:00 |



\---



\## Business Impact



This automation helps:



\- Reduce manual DAG monitoring effort

\- Improve incident response time

\- Centralize Airflow pipeline observability

\- Minimize alert noise through consolidated notifications

\- Improve operational reliability of data workflows



\---



\## Future Enhancements



Planned improvements:



\- Retry mechanism for transient API failures

\- Task-level failure diagnostics

\- DAG execution duration analytics

\- Docker containerization

\- CI/CD integration

\- Unit test coverage expansion

\- Slack / Teams alert integration

\- Dashboard UI improvements



\---



\## Author



\*\*Nagul Pranav V S\*\*



Cloud Data Engineer | Google Cloud Certified Professional Data Engineer



GitHub: https://github.com/nagulpranavvs-de



LinkedIn: https://linkedin.com/in/nagulpranavvs



\---



\## License



MIT License

