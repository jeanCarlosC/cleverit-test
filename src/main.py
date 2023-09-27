from src.frameworks.http.flask import create_flask_app
# base de datos
from src.frameworks.db.sqlite import SQLiteDB
client = SQLiteDB()
# usecases
from src.tasks.usecases.tasks_usecase import tasks_usecase
from src.users.usecases.users_usecase import users_usecase
# repositories
from src.tasks.repositories.sqlite_repository import sqlite_repository as sqlite_repository_tasks
from src.users.repositories.sqlite_repository import sqlite_repository as sqlite_repository_users
# blueprints
from src.tasks.http.tasks_blueprint import create_tasks_blueprint
from src.users.http.users_blueprint import create_users_blueprint

# iniciamos las intacia a los repositorios
sqlite_repository_users_instance = sqlite_repository_users(client)
sqlite_repository_tasks_instance = sqlite_repository_tasks(client)

# iniciamos los casos de uso
users_usecase_instance = users_usecase(sqlite_repository_users_instance)
tasks_usecase_instance = tasks_usecase(sqlite_repository_tasks_instance, sqlite_repository_users_instance)

blueprints = [
    create_tasks_blueprint(tasks_usecase_instance),
    create_users_blueprint(users_usecase_instance),
]
app = create_flask_app(blueprints)

if __name__ == "__main__":
    app.run(debug=True)