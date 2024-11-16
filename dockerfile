FROM apache/airflow:2.9.2
# copy requirements files to the container
COPY requirements.txt /requirements.txt
# upgrade pip
RUN pip install --upgrade pip
# install packages
RUN pip install --no-cache-dir -r /requirements.txt
