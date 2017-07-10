FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 80
RUN ["python", "tests/tests.py"]
CMD ["python", "api.py"]