FROM python:3.9-slim

WORKDIR /app

# On copie les requirements en premier pour optimiser le cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le reste de l'application
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]