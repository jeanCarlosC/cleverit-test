import sqlite3
import os

class SQLiteDB:
    def __init__(self):
        self.db_name = os.environ.get("DB_NAME")
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Conectado a la base de datos: {self.db_name}")
        except sqlite3.Error as e:
            print("name: ", self.db_name)
            print(f"Error al conectar a la base de datos: {str(e)}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Desconectado de la base de datos: {self.db_name}")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {str(e)}")
            return None

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        response = []
        if cursor:
            results = cursor.fetchall()
            for row in results:
                response.append(row)
        return response

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        return None

# Ejemplo de uso:
# if __name__ == "__main__":
#     db = SQLiteDB("mi_base_de_datos.db")
#     db.connect()

#     # Crear una tabla de ejemplo
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS usuarios (
#         id INTEGER PRIMARY KEY,
#         nombre TEXT,
#         email TEXT
#     );
#     """
#     db.execute_query(create_table_query)

#     # Insertar datos de ejemplo
#     insert_query = "INSERT INTO usuarios (nombre, email) VALUES (?, ?);"
#     db.execute_query(insert_query, ("Usuario de Ejemplo", "usuario@example.com"))

#     # Consultar datos de ejemplo
#     select_query = "SELECT * FROM usuarios;"
#     results = db.fetch_all(select_query)
#     for row in results:
#         print(row)

#     db.disconnect()
