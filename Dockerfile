FROM python:3.9-slim

WORKDIR /app

# 1. On copie d'abord le fichier requirements
# Note le point seul à la fin de la ligne
COPY requirements.txt .

# 2. On lance l'installation sur une nouvelle ligne
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# 3. On copie le reste de l'application
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]