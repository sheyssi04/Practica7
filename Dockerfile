# Usamos imagen oficial de Python
FROM python:3.11-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos código fuente
COPY src/ .

# Instalamos dependencias
RUN pip install --no-cache-dir flask mysql-connector-python

# Exponemos puerto
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]