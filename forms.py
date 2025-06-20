from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class SportCreateForm(FlaskForm):
    name = StringField('Имя спортсмена', validators=[DataRequired(), Length(min=3, max=50)])
    sport_type = StringField('Вид спорта', validators=[DataRequired(), Length(min=3, max=50)])
    age = IntegerField('Возраст', validators=[DataRequired()])
    description = StringField('Описание', validators=[Length(max=200)])
    submit = SubmitField('Добавить')

    def validate_name(form, field):
        if 'человек' in form.name.data.lower():
            raise ValidationError('Слово "человек" не разрешено в наименовании спортсмена')


class SportUpdateForm(FlaskForm):
    name = StringField('Имя спортсмена', validators=[DataRequired(), Length(min=3, max=50)])
    sport_type = StringField('Вид спорта', validators=[DataRequired(), Length(min=3, max=50)])
    age = IntegerField('Возраст', validators=[DataRequired()])
    description = StringField('Описание', validators=[Length(max=200)])
    submit = SubmitField('Обновить')

    def validate_name(form, field):
        if 'человек' in form.name.data.lower():
            raise ValidationError('Слово "человек" не разрешено в названии')


class SportDeleteForm(FlaskForm):
    submit = SubmitField('Удалить')