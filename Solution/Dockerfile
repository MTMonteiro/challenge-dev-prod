FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/code/
WORKDIR /usr/src/code/
RUN apt-get update \
  && apt-get install -y \
  netcat \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install python-dateutil
#ADD data.json /usr/src/code/
ADD csv_to_json.py /usr/src/code/
CMD [ "python", "./csv_to_json.py" ,"`sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' csv-datasource`" ]
