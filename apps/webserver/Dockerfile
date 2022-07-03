FROM python:3.7.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host=0.0.0.0" ]
