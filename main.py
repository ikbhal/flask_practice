from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database file path
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    country = db.Column(db.String(20))

    def __init__(self, username, email, country="india"):
        self.username = username
        self.email = email
        self.country = country


@app.route('/')
def index():
    # Perform database operations
    return 'Database operations completed.'


if __name__ == '__main__':
    app.run(debug=True)
