
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.errors.report_api_error import ReportApiError
from src.frameworks.http.error_handlers import Error_handler, report_api_error_handler


def create_flask_app(blueprints):
    """
    Función para crear una aplicación de Flask con todos sus blueprints
    (controladores) asociados. Asocia además el manejador de errores
    """
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'
    jwt = JWTManager(app)

    api = Api(
        app,
        title='Mi API',
        version='1.0',
        description='Descripción de mi API'
    )

    # manejadores de errores
    app.register_error_handler(ReportApiError, report_api_error_handler)
    app.register_error_handler(Exception, Error_handler)

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix="/v1")

    return app
