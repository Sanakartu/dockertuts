from datetime import datetime
import os
from airflow import DAG
from docker.types import Mount
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

dbt_project_path = os.environ.get("DBT_HOST_PATH")
dbt_profiles_path = os.environ.get("DBT_PROFILES_HOST_PATH")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}


def run_elt_script():
    script_path = "/opt/airflow/elt/elt_script.py"
    result = subprocess.run(["python", script_path],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with error: {result.stderr}")
    else:
        print(result.stdout)


dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2024, 1, 4),
    schedule_interval='@daily',
    catchup=False,
)

t1 = PythonOperator(
    task_id='run_elt_script',
    python_callable=run_elt_script,
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