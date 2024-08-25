from flask.cli import FlaskGroup
from app import crear_app

app = crear_app()
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()