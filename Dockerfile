FROM python:3

COPY metrics.py ./

RUN pip3 install --no-cache-dir psutil --user

VOLUME [ "/var/metric_answer" ]

CMD [ ./metrics.py, mem, > /var/metric_answer/usage.txt ]

ENTRYPOINT [ "./metrics.py", "cpu", ]