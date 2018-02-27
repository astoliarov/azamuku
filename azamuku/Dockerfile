FROM python:3.6-alpine3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
RUN mkdir /code;
ADD ./requirements.txt /config/

RUN pip install -r /config/requirements.txt

ADD . /code/

WORKDIR /code

CMD ["python", "run.py"]
