FROM --platform=linux/amd64 apache/airflow:2.11.0

USER root
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

ENV PATH="/home/airflow/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin"

USER airflow
RUN pip install --timeout=120 \
    apache-airflow-providers-docker==3.14.0 \
    psycopg2-binary \
    apache-airflow-providers-http \
    apache-airflow-providers-airbyte \
    apache-airflow-providers-docker

USER root
RUN ln -sf /home/airflow/.local/bin/airflow /usr/local/bin/airflow

USER airflow