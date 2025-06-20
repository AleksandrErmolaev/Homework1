from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class ItemCreateForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired(), Length(min=3, max=50)])
    description = StringField('Описание', validators=[Length(max=200)])
    submit = SubmitField('Создать')

    def validate_name(form, field):
        if 'тест' in form.name.data.lower():
            raise ValidationError('Слово "тест" не разрешено в названии')


class ItemUpdateForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired(), Length(min=3, max=50)])
    description = StringField('Описание', validators=[Length(max=200)])
    submit = SubmitField('Обновить')

    def validate_name(form, field):
        if 'тест' in form.name.data.lower():
            raise ValidationError('Слово "тест" не разрешено в названии')

class ItemDeleteForm(FlaskForm):
    submit = SubmitField('Удалить')

