FROM python:3.7.9-slim-buster

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
