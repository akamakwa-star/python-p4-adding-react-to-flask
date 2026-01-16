from app import app, db
from models import Movie

with app.app_context():
    db.create_all()
    m1 = Movie(title="The Matrix", year=1999)
    m2 = Movie(title="Inception", year=2010)
    db.session.add_all([m1, m2])
    db.session.commit()
