from flask_sqlalchemy import SQLAlchemy

# Initialize db object
db = SQLAlchemy()

class Form1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mobile_number = db.Column(db.String(20))
    email = db.Column(db.String(100))
    date = db.Column(db.String(20))
    dept = db.Column(db.String(50))
    photo_filename = db.Column(db.String(100))
    photo_size = db.Column(db.Integer)  # Size of the photo in bytes
    photo_type = db.Column(db.String(50))  # Type of the photo (e.g., image/png)
