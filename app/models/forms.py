from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, FileField, SubmitField, ValidationError, validators, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length
from app.models.tables import User
from flask_wtf.file import FileRequired, FileAllowed


class RegistrationForm(FlaskForm):
    name = StringField('Nome', [validators.DataRequired(), validators.Length(min=2, max=25)])
    email = StringField('Email', [Email(), validators.Length(min=6, max=35)])
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email já está em uso')
        
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha Não Confere')
    ])
    confirm = PasswordField('Repita a Senha', [validators.DataRequired()])
    accept_tos = BooleanField('Eu Aceito os Termos de Serviço', [validators.DataRequired()])



class LoginForm(FlaskForm):
    email = StringField("Email", [Email(message='Email Não Encontrado') , validators.DataRequired()])

    password = PasswordField("Senha", validators=[DataRequired()])



#animais
class AnimalForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=20)])
    raca = StringField('Raça', validators=[DataRequired(), Length(max=50)])
    especie = SelectField('Espécie',  choices=[('', 'Selecione...'), ('gato', 'Gato'), ('cachorro', 'Cachorro'), ('hamster', 'Hamster')], validators=[DataRequired()])
    cor = StringField('Cor', validators=[DataRequired(), Length(max=50)])
    idade = IntegerField('Idade', validators=[DataRequired()])
    
    def validate_idade(form, field):
        if field.data < 0:
            raise ValidationError("A idade não pode ser negativa.")
    
    def validate_idade(form, field):
        if field.data > 20:
            raise ValidationError("A idade não condiz com a realidade")
        
    descricao = TextAreaField('Descrição', validators=[DataRequired(), Length(max=100)])
    foto = FileField('Foto', validators=[FileRequired(), FileAllowed(['jpeg','jpg', 'png'], 'Arquivo Não Suportado')])
    esterilizado = BooleanField('Esterilizado')
    submit = SubmitField('Registrar')