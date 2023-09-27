# cleverit-test
Desafío de cleverit

### Descripción

API de gestión de tareas.

### Construcción 🛠️
* **Tipo:** API Rest
* **Lenguaje:** Python 3.9
* **Framework:** Flask, SQLite
* **Arquitectura:** Clean Architecture

### Autor ✒️
* **Autores:** Jean Carlos Cuadros, cuadrosjean26@gmail.com.

### Información sobre estructura del proyecto 📖

#### Clean Architecture
Se ha utilizado la arquitectura **Clean Architecture** para el desarrollo del proyecto ara garantizar la separación de preocupaciones, la escalabilidad y la facilidad de mantenimiento.

#### Principios de la Clean Architecture

- **Separación de Capas**: La arquitectura se divide en capas, cada una con una responsabilidad específica. Las capas interactúan entre sí mediante interfaces bien definidas.

- **Independencia de Frameworks**: Las capas internas no dependen de frameworks externos, lo que facilita la prueba y el reemplazo de componentes.

- **Dependencias Unidireccionales**: Las dependencias fluyen en una dirección única, desde las capas externas hacia las capas internas. Esto evita acoplamientos indeseados y facilita la modificación de componentes.


### Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `src/`: Contiene la lógica de la aplicación.
- `src/errors`: Contiene la estructura de los errores.
- `src/frameworks`: Contiene la implementación de los frameworks y dependencias externas.
- `src/frameworks/db`: Contiene la implementación de la base de datos.
- `src/frameworks/http`: Contiene la implementación del framework Flask, estructura de respuesta y manejador de errores.
- `src/tasks`: Contiene la implementación de lógica de negocio e interfaces de las tareas.
- `src/tasks/usecases`: Contiene la implementación de los casos de uso donde se encuentra la lógica de negocio.
- `src/tasks/entities`: Contiene la implementación de las entidades (modelos).
- `src/tasks/repositories`: Contiene la implementación de los repositorios, que en este caso es el que tiene interacción con la base de datos.
- `src/tasks/http`: Contiene la implementación de los controladores, donde se encuentra la lógica de los endpoints.
- `src/tasks/http/fields`: Contiene la implementación de los campos que se usan en los endpoints.
- `src/tasks/http/validators`: Contiene la implementación de los validadores para reglas de negocio.
- `src/utils`: Contiene utilidades que se usan en la aplicación. En este caso se usa para la implementación del patrón **Chain of Responsibility** (`utils/create_validator_chain` y `utils/validator_base`), para funciones de utilidad (`utils/functions`), y para la implementación de la clase de validar campos (`utils/input_validator`).
- `src/main.py`: Contiene la inicialización de dependencias para luego iniciar la aplicación.


### Pre-requisitos 📋

- Docker.

### Instalación 🔧

- Clonar proyecto.
- Crear archivo `.env` en la carpeta raíz. Se incluye archivo `.env.example` como referencia, que se puede usar tal cual como está.
- Ejecutar `docker-compose build` para construir las imágenes de Docker. Sólo es necesario hacerlo una vez.
- Ejecutar `docker-compose up` para levantar los servicios. Si se quiere ejecutar en segundo plano, usar `docker-compose up -d`.

### Preparar la base de datos ⚙️
- Ejecutar `docker exec -it my-sqlite-container touch config/tasks.db` para crear la base de datos.
- Ejecutar `docker exec -it api-tasks python create_db.py` para crear las tablas de la base de datos necesarias.

### Información de cómo realizar las peticiones al API 📖

El API se encuentra disponible en la URL `http://localhost:8080`. Para poder hacer uso de los endpoints se debe enviar un token de autorización en el header de la petición, el token se obtiene al hacer login en el endpoint `/login` con el usuario `admin` y la contraseña `admin`.


### Información de los endpoints disponibles del API 📖
En esta sección se detallan los endpoints disponibles en la API.

Todos los endpoints reciben las siguientes cabeceras:
- **Content-Type:** `application/json`

#### Login
**NOTA**: No requiere token de autorización.
- **URL:** `/login`
- **Método:** `POST`
- **Cuerpo(json):**
    - **username(str, requerido):** Nombre de usuario.
    - **password(str, requerido):** Contraseña.
- **Respuesta exitosa:**
```
{
    "status": "Success",
    "message": "Usuario ingresado correctamente",
    "data": {
        "user": {
            "id": 1,
            "username": "admin",
            "email": "admin@localhost",
            "first_name": "admin",
            "last_name": "admin",
            "is_active": 1,
            "created_at": "2023-09-27 13:56:04",
            "updated_at": null
        },
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NTgyNjY2MiwianRpIjoiODI3Yjk3ZGEtOWUzYi00MjI5LTk3NWMtMzQwYzBhNzIzYjkyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AbG9jYWxob3N0IiwiZmlyc3RfbmFtZSI6ImFkbWluIiwibGFzdF9uYW1lIjoiYWRtaW4iLCJpc19hY3RpdmUiOjEsImNyZWF0ZWRfYXQiOiIyMDIzLTA5LTI3IDEzOjU2OjA0IiwidXBkYXRlZF9hdCI6bnVsbH0sIm5iZiI6MTY5NTgyNjY2MiwiZXhwIjoxNjk1ODI4NDYyfQ.azTIUCVPpUwShBVZtJztCvMZwMnR1OkLd2U42TAXkL4"
    }
}
```
- **Respuesta fallida:**
    - **Código:** `401`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "Usuario o contraseña incorrectos",
        "data": {}
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```
#### Crear usuario
- **URL:** `/users`
- **Método:** `POST`
- **Cuerpo(json):**
    - **username(str, requerido):** Nombre de usuario.
    - **password(str, requerido):** Contraseña.
    - **email(str, requerido):** Correo electrónico.
    - **first_name(str, requerido):** Nombre.
    - **last_name(str, requerido):** Apellido.
- **Respuesta exitosa:**
    - **Código:** `201`
    - **Contenido:** 
    ```
    {
        "status": "Success",
        "message": "Usuario creado correctamente",
        "data": {
            "id": 1,
            "username": "admin",
            "email": "admin@localhost",
            "first_name": "admin",
            "last_name": "admin",
            "is_active": 1,
            "created_at": "2023-09-27 13:56:04",
            "updated_at": null
        }
    }
    ```
- **Respuesta fallida:**
    - **Código:** `422`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "El campo last_name es requerido",
        "data": {}
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```

#### Crear tarea
- **URL:** `/tasks`
- **Método:** `POST`
- **Cuerpo(json):**
    - **tittle(str, requerido):** Título de la tarea.
    - **expiration_date(str, requerido):** Fecha de expiración de la tarea.
    - **status(str, requerido):** Estado de la tarea. Puede ser `TODO`, `IN_PROGRESSS` o `DONE`.
    - **description(str, requerido):** Descripción de la tarea.
    - **user_id(int, opcional):** ID del usuario al que se le asigna la tarea.
- **Respuesta exitosa:**
    - **Código:** `201`
    - **Contenido:** 
    ```
    {
        "status": "Success",
        "message": "Tarea creada correctamente",
        "data": {
            "id": 1,
            "tittle": "Tarea 1",
            "expiration_date": "2023-01-10",
            "status": "TODO",
            "user_id": null
            "created_at": "2023-09-26 19:07:40",
            "updated_at": null
        }
    }
    ```

- **Respuesta fallida:**
    - **Código:** `422`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "El campo last_name es requerido",
        "data": {}
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```
#### Actualizar tarea
- **URL:** `/tasks/<id>`
- **Método:** `PUT`
- **Cuerpo(json):**
    - **tittle(str, opcional):** Título de la tarea.
    - **expiration_date(str, opcional):** Fecha de expiración de la tarea.
    - **status(str, opcional):** Estado de la tarea. Puede ser `TODO`, `IN_PROGRESSS` o `DONE`.
    - **description(str, opcional):** Descripción de la tarea.
- **Respuesta exitosa:**
    - **Código:** `200`
    - **Contenido:** 
    ```
    {
        "status": "Success",
        "message": "Tarea actualizada correctamente",
        "data": {
            "id": 1,
            "tittle": "Tarea 1",
            "expiration_date": "2023-01-10",
            "status": "TODO",
            "created_at": "2023-09-26 19:07:40",
            "updated_at": null
        }
    }
    ```
- **Respuesta fallida:**
    - **Código:** `404`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "La encuesta con id 1 no existe",
        "data": {}
    }
    ```
    - **Código:** `422`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "El usuario con id 111 no existe",
        "data": {}
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```

#### Listar tareas
- **URL:** `/tasks`
- **Método:** `GET`
- **Respuesta exitosa:**
    - **Código:** `200`
    - **Contenido:**
    ```
    {
        "status": "Success",
        "message": "Tareas obtenidas correctamente",
        "data": [
            {
                "id": 1,
                "tittle": "Tarea 1",
                "expiration_date": "2023-01-10",
                "status": "TODO",
                "user_id": null
                "created_at": "2023-09-26 19:07:40",
                "updated_at": null
            },
            {
                "id": 2,
                "tittle": "Tarea 2",
                "expiration_date": "2023-01-10",
                "status": "TODO",
                "user_id": null
                "created_at": "2023-09-26 19:07:40",
                "updated_at": null
            }
        ]
    }
    ```
- **Respuesta fallida:**
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```

#### Obtener tarea
- **URL:** `/tasks/<id>`
- **Método:** `GET`
- **Parámetros(url):**
    - **id(integer):** ID de la tarea.
- **Respuesta exitosa:**
    - **Código:** `200`
    - **Contenido:**
    ```
    {
        "status": "Success",
        "message": "Tarea obtenida correctamente",
        "data": {
            "id": 1,
            "tittle": "Tarea 1",
            "expiration_date": "2023-01-10",
            "status": "TODO",
            "user_id": null
            "created_at": "2023-09-26 19:07:40",
            "updated_at": null
        }
    }
    ```
- **Respuesta fallida:**
    - **Código:** `404`
    - **Contenido:** 
    ```
    {
        "status": "Fail",
        "message": "La encuesta con id 1 no existe",
        "data": {}
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```

#### Eliminar tarea
- **URL:** `/tasks/<id>`
- **Método:** `DELETE`
- **Parámetros(url):**
    - **id:** ID de la tarea.
- **Respuesta exitosa:**
    - **Código:** `200`
    - **Contenido:**
    ```
    {
        "status": "Success",
        "message": "Tarea eliminada correctamente",
        "data": true
    }
    ```
- **Respuesta fallida:**
    - **Código:** `404`
    - **Contenido:** 
    ```
    {
        {
            "status": "Fail",
            "message": "La encuesta con id 1 no existe",
            "data": {}
        }
    }
    ```
    - **Código:** `500`
    - **Contenido:** 
    ```
    {
        "status": "failed",
        "message": "Internal error during request.",
        "data": {}
    }
    ```