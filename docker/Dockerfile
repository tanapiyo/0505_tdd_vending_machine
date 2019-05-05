FROM python:3

WORKDIR /var/app
RUN pip install --upgrade pip
RUN pip install pytest
WORKDIR /var/src

CMD [ "python3", "-m", "http.server", "8000" ]
