from flask import request, url_for, render_template, redirect, flash
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy

from forms import ItemDeleteForm, ItemUpdateForm, ItemCreateForm
from models import Item


class ItemList(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self):
        items: list[Item] = self.engine.session.execute(Item.query).scalars()
        return render_template('item/list.html', items=items)


class ItemView(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    def get(self, item_id: str):
        query = Item.query.where(Item.id == item_id)
        item: Item = self.engine.session.execute(query).scalar()
        if not item:
            return 'Не найдено'
        return render_template('item/read.html', item=item)


class ItemUpdate(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    # GET /items/<item_id>/update/ → загружает Item и показывает форму
    def get(self, item_id: str):
        query = Item.query.where(Item.id == item_id)
        item: Item = self.engine.session.execute(query).scalar()
        if not item:
            return 'Не найдено'
        form = ItemUpdateForm(
            name=item.name,
            description=item.description,
        )
        return render_template('item/update.html', item=item, form=form)

    # POST /items/<item_id>/update/ → сохраняет изменения
    def post(self, item_id: str):
        query = Item.query.where(Item.id == item_id)
        item: Item = self.engine.session.execute(query).scalar()
        if not item:
            return 'Не найдено'

        form = ItemUpdateForm(request.form)
        if form.validate():
            item.name = form.name.data
            item.description = form.description.data
            self.engine.session.commit()

        return redirect(url_for('item.list', item_id=item.id))


class ItemDelete(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    # GET /items/<item_id>/delete/ → показывает форму подтверждения удаления
    def get(self, item_id: str):
        query = Item.query.where(Item.id == item_id)
        item: Item = self.engine.session.execute(query).scalar()
        if not item:
            return 'Не найдено'
        form = ItemDeleteForm()
        return render_template('item/delete.html', item=item, form=form)

    # POST /items/<item_id>/delete/ → удаляет Item из базы
    def post(self, item_id: str):
        query = Item.query.where(Item.id == item_id)
        item: Item = self.engine.session.execute(query).scalar()
        if not item:
            return 'Не найдено'
        form = ItemDeleteForm(request.form)
        if form.validate():
            # удаляет из БД
            self.engine.session.delete(item)
            self.engine.session.commit()

        return redirect(url_for('item.list'))


class ItemCreate(MethodView):
    init_every_request = False

    def __init__(self, engine: SQLAlchemy):
        self.engine = engine

    # GET /items/create/ → показывает форму создания Item
    def get(self):
        form = ItemCreateForm()
        return render_template('item/create.html', form=form)

    # POST /items/create/ → принимает данные, валидирует и создаёт Item в БД.
    def post(self):
        # создаёт объект формы из данных запроса
        form = ItemCreateForm(request.form)
        # проверяет валидность данных
        if form.validate():
            item = Item(
                name=form.name.data,
                description=form.description.data
            )
            # добавляет новый объект в БД
            self.engine.session.add(item)
            self.engine.session.commit()
            flash("Успешно!", category='success')
        else:
            flash("Произошла ошибка при создании", category='error')

        return redirect(url_for('item.list'))
