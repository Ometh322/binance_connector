FROM python:3.8

ADD binance_connector.py /

RUN pip install websocket
RUN pip install websocket-client

CMD ["python", "-u", "./binance_connector.py"]
