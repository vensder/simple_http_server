FROM python:2-alpine
MAINTAINER vensder <vensder@gmail.com>
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 80
CMD ["python", "http_server.py"]
