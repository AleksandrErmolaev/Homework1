from flask import Flask
from models import db, create_table
from views import ItemView, ItemList, ItemCreate, ItemUpdate, ItemDelete
import os

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = os.urandom(24)
db.init_app(app)

# Создание таблиц
create_table(app)

# Регистрация представлений
app.add_url_rule('/', view_func=ItemList.as_view('item.list', engine=db))
app.add_url_rule('/items/<string:item_id>/', view_func=ItemView.as_view('item.view', engine=db))
app.add_url_rule('/items/create/', view_func=ItemCreate.as_view('item.create', engine=db))
app.add_url_rule('/items/<string:item_id>/update/', view_func=ItemUpdate.as_view('item.update', engine=db))
app.add_url_rule('/items/<string:item_id>/delete/', view_func=ItemDelete.as_view('item.delete', engine=db))

if __name__ == "__main__":
    app.run(debug=True)
