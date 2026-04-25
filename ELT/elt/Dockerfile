FROM python:3.8-slim

RUN apt-get update && apt-get install -y wget gnupg \
    && echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y postgresql-client-18



COPY elt_script.py .

CMD ["python", "elt_script.py"]
