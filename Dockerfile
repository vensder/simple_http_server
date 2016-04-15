FROM python:2-alpine
MAINTAINER Docker Education Team <education@docker.com>
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5555
CMD ["python", "http_server.py"]
