from wtforms import Form # type: ignore
from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, SubmitField, FieldList, RadioField,IntegerField, EmailField # type: ignore

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    apellido = StringField('Apellido')
    email = EmailField('Email')
