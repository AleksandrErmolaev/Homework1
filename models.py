from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Item(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    description: Mapped[str] = mapped_column(db.String(200))

    def __repr__(self):
        return f'<Item {self.name}>'

def create_table(app: Flask):
    with app.app_context():
        db.create_all()
