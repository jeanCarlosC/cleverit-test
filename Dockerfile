FROM python:3.9

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPYCACHEPREFIX=/tmp

COPY requirements.txt .
COPY requirements_dev.txt .
COPY create_db.py /app/

# Ejecuta el script Python cuando se inicie el contenedor

RUN pip install -r requirements_dev.txt

CMD ["gunicorn", "-b", ":8080", "src.main:app", "--reload"]