from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class ContatoForm(FlaskForm):
    nome = StringField("Nome",validators=[DataRequired(),Length(max=50)])
    email = StringField("Email",validators=[DataRequired()])
    assunto = StringField("Assunto",validators=[DataRequired(),Length(max=100)])
    mensagem = StringField("Mensagem",validators=[DataRequired(),Length(max=50)])
    btnSubmit = SubmitField("Enviar")