FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

ENV PORT=10000

EXPOSE 10000

CMD ["sh", "-c", "gunicorn 'app.app:create_app()' --bind 0.0.0.0:${PORT}"]
