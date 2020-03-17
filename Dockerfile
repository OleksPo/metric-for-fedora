FROM python:3

COPY metrics.py ./

RUN pip3 install --no-cache-dir psutil --user

ENTRYPOINT ["python3", "./metrics.py"]