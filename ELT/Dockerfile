FROM apache/airflow:2.10.5-python3.11

RUN pip install --upgrade pip setuptools wheel && \
    pip cache purge

RUN pip install apache-airflow-providers-docker==3.14.0 && \
    pip install psycopg2-binary && \
    pip install docker