from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
db_config = {
    'host': os.getenv('MYSQL_HOST', 'db'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'rootpassword'),
    'database': os.getenv('MYSQL_DATABASE', 'mydb')
}

@app.route('/')
def hola_mundo():
    try:
        # Conexión a MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT '¡Hola desde MySQL!' AS mensaje")
        result = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"<h1>Hola Mundo desde Flask!</h1><p>{result}</p>"
    except Exception as e:
        return f"<h1>Error de conexión:</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)