from datetime import datetime
import bcrypt
from src.errors.report_api_error import ReportApiError
from src.users.entities.user import User


class sqlite_repository():
    def __init__(self, sqlitedb):
        self.sqlitedb = sqlitedb

    def validate_user(self, username, password):
        try:
            query = f"SELECT * FROM users WHERE username = '{username}'"
            data = self.sqlitedb.fetch_one(query)
            if not data:
                return None
            if not self.check_password(password, data[2]):
                return None

            return User(id=data[0], username=data[1], email=data[3], first_name=data[4], last_name=data[5], is_active=data[6], created_at=data[7], updated_at=data[8]).to_dict()

        except Exception as e:
            raise ReportApiError(
                f"Error al obtener el usuario: {str(e)}", status_code=500)
    def get_by_id(self, id):
        try:
            data = self.sqlitedb.fetch_one(
                f"SELECT * FROM users WHERE id = {id}")
            if not data:
                return None
            return User(id=data[0], username=data[1], email=data[3], first_name=data[4], last_name=data[5], is_active=data[6], created_at=data[7], updated_at=data[8]).to_dict()
        except Exception as e:
            raise ReportApiError(
                f"Error al obtener el usuario: {str(e)}", status_code=500)

    def create_user(self, user):
        try:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            hashed_password = self.hash_password(user['password'])
            response = self.sqlitedb.execute_query(
                f"INSERT INTO users (username, password, email, first_name, last_name, is_active, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (user['username'], hashed_password, user['email'], user['first_name'], user['last_name'], user['is_active'], created_at))
            id = response.lastrowid
            return User(
                id=id, username=user['username'], email=user['email'], first_name=user['first_name'], last_name=user['last_name'], is_active=user['is_active'], created_at=created_at, updated_at=None).to_dict()
        except Exception as e:
            raise ReportApiError(
                f"Error al crear el usuario: {str(e)}", status_code=500)

    def update_user(self, user_id, user):
        try:
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = f"UPDATE users SET updated_at = '{updated_at}', "
            if "username" in user:
                query += f"username = '{user['username']}', "
            if "password" in user:
                hashed_password = self.hash_password(user['password'])
                query += f"password = '{hashed_password}', "
            if "email" in user:
                query += f"email = '{user['email']}', "
            if "first_name" in user:
                query += f"first_name = '{user['first_name']}', "
            if "last_name" in user:
                query += f"last_name = '{user['last_name']}', "
            if "is_active" in user:
                query += f"is_active = '{user['is_active']}', "
            query = query[:-2]
            query += f" WHERE id = {user_id}"
            self.sqlitedb.execute_query(query)
            return self.get_user(user_id)
        except Exception as e:
            raise ReportApiError(
                f"Error al actualizar el usuario: {str(e)}", status_code=500)

    def delete_user(self, user_id):
        try:
            self.sqlitedb.execute_query(f"DELETE FROM users WHERE id = {user_id}")
            return True
        except Exception as e:
            raise ReportApiError(
                f"Error al eliminar el usuario: {str(e)}", status_code=500)
    def hash_password(self, password_plaintext):
        return bcrypt.hashpw(password_plaintext.encode('utf-8'), bcrypt.gensalt())
    def check_password(self, password_plaintext, stored_password):
        return bcrypt.checkpw(password_plaintext.encode('utf-8'), stored_password)
