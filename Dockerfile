


FROM amazonlinux:2

RUN yum install -y python3 nano wget curl jq \
&& pip3 install flask

WORKDIR /myspace/

COPY . /myspace/

EXPOSE 5000

CMD ["python3", "webserver.py"]