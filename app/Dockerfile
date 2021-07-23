FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev curl \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

COPY wait-for.sh .

WORKDIR /app

RUN pip install -r /app/requirements.txt


COPY ./source .

EXPOSE 5000

CMD ["python", "app.py"]