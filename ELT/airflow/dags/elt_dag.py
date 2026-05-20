from datetime import datetime
import os
from airflow import DAG
from docker.types import Mount
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

CONN_ID = '4145a049-ed35-4cfd-a792-187fcd1a9b07'


dbt_project_path = os.environ.get("DBT_HOST_PATH")
dbt_profiles_path = os.environ.get("DBT_PROFILES_HOST_PATH")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}





dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2024, 1, 4),
    schedule_interval='@daily',
    catchup=False,
)

t1 = AirbyteTriggerSyncOperator(
    task_id='airbyte_postgres_postgres',
    airbyte_conn_id='airbyte',
    connection_id=CONN_ID,
    asynchronous=False,
    timeout=3,
    dag=dag,
)

t2 = DockerOperator(
    task_id='dbt_run',
    image='ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    command=[
        "run",
        "--profiles-dir", "/root",
        "--project-dir", "/dbt",
        "--full-refresh"
    ],
    auto_remove=True,
    mount_tmp_dir=False,
    docker_url="unix:///var/run/docker.sock",
    network_mode="elt_elt_network",
    mounts=[
        Mount(source=dbt_project_path, target="/dbt", type="bind"),
        Mount(source=dbt_profiles_path, target="/root", type="bind"),   # уже смонтировано compose
    ],
    dag=dag
)

t1 >> t2