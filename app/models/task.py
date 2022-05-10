from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    completed_at = None # `db.DateTime`

    def to_dict(self):
        return {
            "task": {
                "task_id": self.id,
                "title": self.title,
                "description": self.description,
                "is_complete": self.completed_at
            }
        }
