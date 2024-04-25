from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    first_name = StringField('Имя пользователя', validators=[DataRequired()])
    second_name = StringField('Фамилия пользователя', validators=[DataRequired()])
    num_class = IntegerField('Цифра класса', validators=[DataRequired()])
    alfa_class = StringField('Буква класса', validators=[DataRequired()])
    school = IntegerField('Номер школы', validators=[DataRequired()])
    types = SelectField('Тип учётной записи',  validators=[DataRequired()], choices=['Ученик', "Учитель", "Родитель"])
    submit = SubmitField('Войти')