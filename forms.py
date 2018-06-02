from wtforms.validators import InputRequired
from wtforms import SelectField, SubmitField, StringField
from flask_wtf import FlaskForm

#Form de Pesquisa

class mainForm(FlaskForm):
    agencia = StringField('Agencia', validators=[InputRequired()])
    estado = StringField('Estado', validators=[InputRequired()])
    cidade = StringField('Cidade', validators=[InputRequired()])
    submit = SubmitField()
