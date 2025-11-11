USE mydb;
CREATE TABLE IF NOT EXISTS mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(255)
);INSERT INTO mensajes (texto) VALUES ('¡Conexión exitosa!');
