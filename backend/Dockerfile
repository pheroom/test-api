FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN useradd -m -u 1000 appuser

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

#EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "60", "app:app"]

CMD gunicorn \
    --bind 0.0.0.0:8000 \
    --workers ${WORKERS:-$(python -c 'import multiprocessing; print(multiprocessing.cpu_count() * 2 + 1)')} \
    --worker-class gevent \
    --worker-connections 1000 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --timeout 120 \
    --graceful-timeout 30 \
    --keep-alive 5 \
    --access-logfile - \
    --error-logfile - \
    --log-level ${LOG_LEVEL:-'info'} \
    --env FORWARDED_ALLOW_IPS='*' \
    app:app