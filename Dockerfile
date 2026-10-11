FROM python:3.10-slim
COPY requirements.txt  /app/requirements.txt
RUN pip install -r /app/requirements.txt
WORKDIR /app/src
COPY src/weather.py /app/src/weather.py
COPY src/logs/ /app/src/logs/
CMD ["python", "weather.py"]