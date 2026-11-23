FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app
COPY app.py .

RUN addgroup --system app && adduser --system --ingroup app app
USER app

EXPOSE 8000
CMD ["python", "app.py"]
