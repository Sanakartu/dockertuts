FROM --platform=linux/amd64 apache/airflow:2.10.5

USER root
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

USER airflow
RUN pip install apache-airflow-providers-docker==3.14.0 psycopg2-binary