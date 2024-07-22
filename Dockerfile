FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
