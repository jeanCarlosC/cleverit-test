from datetime import datetime
from src.errors.report_api_error import ReportApiError
from src.tasks.entities.task import Task


class sqlite_repository():
    def __init__(self, sqlitedb):
        self.sqlitedb = sqlitedb

    def get_tasks(self):
        try:
            data = self.sqlitedb.fetch_all("SELECT * FROM tasks")
            tasks = []
            for task in data:
                tasks.append(self.entity_task(data))
            return tasks
        except Exception as e:
            raise ReportApiError(
                f"Error al obtener las tareas: {str(e)}", status_code=500)

    def get_task(self, task_id):
        try:
            data = self.sqlitedb.fetch_one(
                f"SELECT * FROM tasks WHERE id = {task_id}")
            if not data:
                return None
            return self.entity_task(data)

        except Exception as e:
            raise ReportApiError(
                f"Error al obtener la tarea: {str(e)}", status_code=500)

    def get_task_by_title(self, title):
        try:
            data = self.sqlitedb.fetch_one(
                f"SELECT * FROM tasks WHERE title = '{title}'")
            if not data:
                return None
            return self.entity_task(data)

        except Exception as e:
            raise ReportApiError(
                f"Error al obtener la tarea: {str(e)}", status_code=500)

    def create_task(self, task):
        try:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if 'user_id' not in task:
                task['user_id'] = None
            response = self.sqlitedb.execute_query("INSERT INTO tasks (title, expiration_date, status, user_id, created_at) VALUES (?, ?, ?, ?, ?)", (
                task['title'], task['expiration_date'], task['status'], task['user_id'], created_at))
            id = response.lastrowid
            task = Task(
                id=id, title=task['title'], expiration_date=task['expiration_date'], status=task['status'], user_id=task['user_id'], created_at=created_at, updated_at=None).to_dict()
            return task
        except Exception as e:
            raise ReportApiError(
                f"Error al crear la tarea: {str(e)}", status_code=500)

    def update_task(self, task_id, task):
        try:
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = f"UPDATE tasks SET updated_at = '{updated_at}', "
            if "title" in task:
                query += f"title = '{task['title']}', "
            if "expiration_date" in task:
                query += f"expiration_date = '{task['expiration_date']}', "
            if "status" in task:
                query += f"status = '{task['status']}', "
            if "user_id" in task:
                query += f"user_id = '{task['user_id']}', "
            query = query[:-2]
            query += f" WHERE id = {task_id}"
            self.sqlitedb.execute_query(query)
            return self.get_task(task_id)
        except Exception as e:
            raise ReportApiError(
                f"Error al actualizar la tarea: {str(e)}", status_code=500)

    def delete_task(self, task_id):
        try:
            self.sqlitedb.execute_query(
                f"DELETE FROM tasks WHERE id = {task_id}")
            return True
        except Exception as e:
            raise ReportApiError(
                f"Error al eliminar la tarea: {str(e)}", status_code=500)

    def entity_task(self, data):
        return Task(id=data[0], title=data[1],
                    expiration_date=data[2], status=data[3], user_id=data[4], created_at=data[5], updated_at=data[6]).to_dict()
