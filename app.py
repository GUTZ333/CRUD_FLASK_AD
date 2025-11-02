from db import db
from routes.tasks_routes import task_routes
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db" # Configurando a url do banco SQLite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True # Desativando o rastreamento de modificações do SQLAlchemy
db.init_app(app)
app.register_blueprint(task_routes)

if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run()