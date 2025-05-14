FROM python:3.10-slim

# Crée un utilisateur non-root
RUN useradd -m flaskuser

# Définir le dossier de travail
WORKDIR /app

# Copier et installer les dépendances
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY app/ .

# Donner les permissions
RUN chown -R flaskuser:flaskuser /app

# Passer à l'utilisateur non-root
USER flaskuser

# Exposer le port
EXPOSE 5000

# Lancer l’application
CMD ["python", "app.py"]
