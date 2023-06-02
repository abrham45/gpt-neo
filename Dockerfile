FROM python:3.7.9
WORKDIR /code
COPY . /code/
RUN pip install pip setuptools -U
RUN pip install -r requirements.txt


