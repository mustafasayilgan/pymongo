FROM python:3.12-slim

WORKDIR /app

RUN useradd --uid 1000 hepapiuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R hepapiuser:hepapiuser /app
USER hepapiuser

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
