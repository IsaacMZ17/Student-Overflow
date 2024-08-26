from app import crear_app
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from dotenv import load_dotenv

app = crear_app()
migrate = Migrate(app, app.extensions['migrate'].db)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()