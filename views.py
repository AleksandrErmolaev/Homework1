
from flask import request, url_for, render_template, redirect, flash
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from forms import SportCreateForm, SportUpdateForm, SportDeleteForm
from models import Sport



class SportList(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self):
        items = Sport.query.all()
        return render_template('sport/list.html', items=items)


class SportView(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self, item_id: str):
        item = Sport.query.get_or_404(item_id)
        return render_template('sport/info.html', item=item)


class SportUpdate(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self, item_id: str):
        item = Sport.query.get_or_404(item_id)
        form = SportUpdateForm(
            name=item.name,
            sport_type=item.sport_type,
            age=item.age,
            description=item.description
        )
        return render_template('sport/update.html', item=item, form=form)

    def post(self, item_id: str):
        item = Sport.query.get_or_404(item_id)
        form = SportUpdateForm(request.form)
        if form.validate():
            item.name = form.name.data
            item.sport_type = form.sport_type.data
            item.age = form.age.data
            item.description = form.description.data
            self.engine.session.commit()
            flash("Данные спортсмена успешно обновлены!", 'success')
        else:
            flash("Ошибка при обновлении данных", 'error')
        return redirect(url_for('sport.list'))


class SportDelete(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self, item_id: str):
        item = Sport.query.get_or_404(item_id)
        form = SportDeleteForm()
        return render_template('sport/delete.html', item=item, form=form)

    def post(self, item_id: str):
        item = Sport.query.get_or_404(item_id)
        form = SportDeleteForm(request.form)
        if form.validate():
            self.engine.session.delete(item)
            self.engine.session.commit()
            flash("Спортсмен удалён", 'success')
        return redirect(url_for('sport.list'))


class SportCreate(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self):
        form = SportCreateForm()
        return render_template('sport/create.html', form=form)

    def post(self):
        form = SportCreateForm(request.form)
        if form.validate():
            try:
                item = Sport(
                    name=form.name.data,
                    sport_type=form.sport_type.data,
                    age=form.age.data,
                    description=form.description.data
                )
                self.engine.session.add(item)
                self.engine.session.commit()
                flash("Спортсмен успешно добавлен!", 'success')
                return redirect(url_for('sport.list'))
            except Exception as e:
                flash(f"Ошибка при сохранении: {str(e)}", 'error')
        else:
            flash("Ошибка в форме: " + str(form.errors), 'error')
        return render_template('sport/create.html', form=form)