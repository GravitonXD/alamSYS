# Use alpine since it is lightweight
FROM python:alpine3.16

COPY API /alamAPI/API
COPY DB_model /alamAPI/DB_model
COPY API/routers /alamAPI/API/routers
COPY requirements.txt /alamAPI

ENV PYTHONPATH "${PYTHONPATH}:/alamAPI/API"
ENV PYTHONPATH "${PYTHONPATH}:/alamAPI/DB_module"

WORKDIR /alamAPI

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3","/alamAPI/API/main.py"]
