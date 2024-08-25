from app import crear_app
from flask_migrate import Migrate
from flask.cli import FlaskGroup

app = crear_app()
migrate = Migrate(app, app.extensions['migrate'].db)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()