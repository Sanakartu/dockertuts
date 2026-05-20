FROM --platform=linux/amd64 apache/airflow:2.10.5

USER root

# Оновлюємо списки, ставимо клієнт і очищаємо кеш apt в один крок
RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Встановлюємо ТІЛЬКИ додаткові пакети в один шар (без перевстановлення самого airflow)
RUN pip install --no-cache-dir \
    apache-airflow-providers-docker==3.14.0 \
    psycopg2-binary \
    apache-airflow-providers-http \
    apache-airflow-providers-airbyte
