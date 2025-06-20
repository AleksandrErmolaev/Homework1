from flask import Flask
from models import db, create_table
from views import SportView, SportList, SportCreate, SportUpdate, SportDelete
import os

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = os.urandom(24)
db.init_app(app)

create_table(app)

app.add_url_rule('/', view_func=SportList.as_view('sport.list', engine=db))
app.add_url_rule('/sports/<string:item_id>/', view_func=SportView.as_view('sport.view', engine=db))
app.add_url_rule('/sports/create/', view_func=SportCreate.as_view('sport.create', engine=db))
app.add_url_rule('/sports/<string:item_id>/update/', view_func=SportUpdate.as_view('sport.update', engine=db))
app.add_url_rule('/sports/<string:item_id>/delete/', view_func=SportDelete.as_view('sport.delete', engine=db))

if __name__ == "__main__":
    app.run(debug=True)