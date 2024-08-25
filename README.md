# Student Overflow

## primero necesitas instalar el archivo requirements: 
    pip install -r requirements.txt

## en la carpeta 'app' crea un archivo config.py
## "asegurate de tener configurado un usuario con permisos para acceder a la base de datos"

## en tu consola del sistema abre python y ejecuta los siguientes comandos
    import secrets
    // dentro del parentesis en token_hex() por un valor para la longitud de tu token
    secrets.token_hex()
    //copia el token que se genero

## en tu archivo config.py copia lo siguiente
    class Config:
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost:port/database'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = //aqui va el token que generaste
        JWT_ALGORITHM = 'HS256'

## Crea las tablas necesarias en postgresql
    CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

    CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);

    CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    question_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);

    CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    is_upvote BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    answer_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (answer_id) REFERENCES answers(id) ON DELETE CASCADE,
    UNIQUE (user_id, answer_id));

## Inicia un entorno migrations
    flask db init

## Crea una migracion
    flask db migrate -m "Mensaje de descripción de la migración"

## Aplica la migracion a la base de datos
    flask db upgrade

## Configura flask run
    Mac - Linux:
    export FLASK_APP=run.py
    export FLASK_ENV=development

    Windows: 
    set FLASK_APP=run.py
    set FLASK_ENV=development

## Ejecuta flask run
    flask run