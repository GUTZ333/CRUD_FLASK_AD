from db import db

class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), nullable=False)

    def json(self):
      return {
         "id": self.id,
         "title": self.title,
         "description": self.description,
         "status": self.status,
      }
