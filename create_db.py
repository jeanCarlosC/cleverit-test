import sqlite3
import bcrypt
import datetime
import os

# Se obtiene el nombre de la base de datos desde una variable de entorno
db_name = os.environ.get("DB_NAME")

print(f"conectando a la base de datos: {db_name}")

# Conectarse a la base de datos SQLite
conn = sqlite3.connect(db_name)

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla de tareas
create_table_query_tasks = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    expiration_date TEXT,
    status TEXT,
    user_id INTEGER,
    created_at TEXT,
    updated_at TEXT default null
);
"""

# Crear una tabla de usuarios
create_table_query_users = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT default null
);
"""

# insert into users (name, email) values ('Juan', 'juan@localhost');
# insert into tasks (title, expiration_date, status) values ('Tarea 1', '2021-10-10', 'pendiente');
username = "admin"
password = "admin"
created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
create_user_query = "INSERT into users (username, password, email, first_name, last_name, is_active, created_at) values (?, ?, ?, ?, ?, ?, ?)"
params = (username, hash_password, "admin@localhost", "admin", "admin", 1, created_at)

cursor.execute(create_table_query_users)
cursor.execute(create_user_query, params)
cursor.execute(create_table_query_tasks)
conn.commit()
print("Proceso finalizado")

# Cerrar la conexión
print("Cerrando la conexión a la base de datos")
conn.close()
