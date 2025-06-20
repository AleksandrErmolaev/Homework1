from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Sport(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    sport_type: Mapped[str] = mapped_column(db.String(50), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(db.String(200))

    def __repr__(self):
        return f'<Sport {self.name}>'

def create_table(app: Flask):
    with app.app_context():
        db.create_all()