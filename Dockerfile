FROM python:3
ENV PYTHONUNBUFFERED=1
COPY test-requirements.txt /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r test-requirements.txt
COPY . /usr/src/app
RUN python setup.py install
