from wtforms import Form, StringField, IntegerField, RadioField, SubmitField, validators
from flask_wtf import FlaskForm

class ZodiacoForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])
    apellidopaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message="El apellido paterno es requerido"),
        validators.Length(min=2, max=50, message="El apellido paterno debe tener entre 2 y 50 caracteres")
    ])
    apellidomaterno = StringField('Apellido Materno', [
        validators.DataRequired(message="El apellido materno es requerido"),
        validators.Length(min=2, max=50, message="El apellido materno debe tener entre 2 y 50 caracteres")
    ])
    dia = IntegerField('Día', [
        validators.DataRequired(message="El día es requerido"),
        validators.NumberRange(min=1, max=31, message="El día debe estar entre 1 y 31")
    ])
    mes = IntegerField('Mes', [
        validators.DataRequired(message="El mes es requerido"),
        validators.NumberRange(min=1, max=12, message="El mes debe estar entre 1 y 12")
    ])
    año = IntegerField('Año', [
        validators.DataRequired(message="El año es requerido"),
        validators.NumberRange(min=1900, max=2025, message="El año debe estar entre 1900 y 2025")
    ])
    sexo = RadioField('Sexo', choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], validators=[
        validators.DataRequired(message="El sexo es requerido")
    ])
    submit = SubmitField('Imprimir')