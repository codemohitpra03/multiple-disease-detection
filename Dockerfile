FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN pip3 freeze > requirements.txt

COPY ./requirements.txt ./


RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
