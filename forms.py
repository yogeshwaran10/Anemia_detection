from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AnemiaForm(FlaskForm):
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    hemoglobin = StringField('Haemoglobin', validators=[DataRequired()])
    mch = StringField('MCH', validators=[DataRequired()])
    mchc = StringField('MCHC', validators=[DataRequired()])
    mcv = StringField('MCV', validators=[DataRequired()])
    submit = SubmitField('Predict')
