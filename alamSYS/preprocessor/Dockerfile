# Using Python 3.11
FROM python:3.11.2

COPY main.py /preprocessor/main.py
COPY manual_run.py /preprocessor/manual_run.py
COPY data_collector /preprocessor/data_collector/
COPY utils /preprocessor/utils/
COPY utils/json_data/* /preprocessor/utils/json_data/*
COPY data_processor /preprocessor/data_processor/
COPY data_processor/ml_model /preprocessor/data_processor/ml_model
COPY requirements.txt /preprocessor/requirements.txt

RUN apt-get update && apt-get install -y vim

ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_collector"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_processor"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/utils"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/utils/db_actions.py"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_processor/ml_model"

WORKDIR /preprocessor

RUN pip install --upgrade pip
RUN pip3 install -r /preprocessor/requirements.txt

CMD ["python", "-u", "/preprocessor/main.py"]
