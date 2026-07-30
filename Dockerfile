# Gerador de Senha -- imagem de producao (Flask, servido via gunicorn)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home --uid 1000 appuser && chown -R appuser:appuser /app
USER appuser

ENV PORT=5100
EXPOSE 5100

CMD ["gunicorn", "--bind", "0.0.0.0:5100", "--workers", "2", "--timeout", "30", "app:app"]
