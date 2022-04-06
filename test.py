"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 4),
    'email': ['thai.pham@onpoint.vn'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
def sleep_t():
    time.sleep(600)

dag = DAG(
    'tutorial', 
    default_args=default_args, 
    schedule_interval=timedelta(days=1))

t1 = PythonOperator(
    task_id='sleep',
    python_callable=sleep_t,
    dag=dag)
t1


