import wtforms as wtf  #ver biblioteca de formularios wtf
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField # recebe arquivos como foto

class UserForm(FlaskForm):
    email = wtf.StringField(
    'Email',
    [wtf.validators.DataRequired(),
    wtf.validators.Email()]
    )
    password = wtf.PasswordField(
    'Senha', [wtf.validators.DataRequired()]
    )
    foto = FileField('Foto')
