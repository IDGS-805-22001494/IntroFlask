from wtforms import Form # type: ignore
from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, SubmitField, FieldList, RadioField,IntegerField, EmailField # type: ignore
from wtforms import validators # type: ignore


class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='Campo requerido'),
        validators.Length(min=3, max=10, message='Longitud mínima: 3 caracteres, longitud máxima: 10 caracteres')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='Campo requerido'),
    ])
    apellido = StringField('Apellido',[
        validators.DataRequired(message='Campo requerido'),
    ])
    email = EmailField('Email', [
                validators.Email(message='Ingresa un correo inválido')
    ])
