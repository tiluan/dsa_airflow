# Projeto 3 - Extração de Dados via API com Apache Airflow

# Imports
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago
from proj03.p3_etl import processo_etl

# Argumentos
default_args ={
    'owner':'luan',
    'depends_on_past':False,
    'start_date':datetime(2025, 11, 22),
    'email':['contatos_luan@hotmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

# DAG
dag = DAG('p3_dag',
        default_args = default_args,
        description = 'Projeto 3',
        schedule_interval = timedelta(minutes=60),
        tags = ['proj03']
)

# PythonOperator
executa_etl = PythonOperator(task_id = 'p3_etl_api',
                             python_callable = processo_etl,
                             dag = dag
)

# Envia a tarefa para execução
executa_etl


