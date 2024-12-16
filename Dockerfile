FROM python:3.12

RUN pip install BAC0==23.99 netifaces pyasyncore pytz dnspython

WORKDIR /app

CMD ["python", "app.py"]