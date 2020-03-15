FROM python:3

COPY metrics.py ./

RUN pip3 install --no-cache-dir psutil --user

ENTRYPOINT [ "./metrics.py", "cpu", ]
