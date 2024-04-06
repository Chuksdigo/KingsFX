
FROM apache/airflow:2.8.4

# copy the requirements.txt to container
COPY requirements.txt /requirements.txt

# install packages

RUN pip install --no-cache-dir -r /requirements.txt