from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , TextAreaField , FieldList, SelectMultipleField, FormField , HiddenField , SelectField 
from wtforms.validators import DataRequired
from app.azuretables import azuretabla

class QuestionsForm(FlaskForm):
    initiave_name = StringField('Cloud Initiave Name', validators=[DataRequired()])
    whoassist = StringField('mail',default=azuretabla.mail)
    biwac = BooleanField('Biwac', validators=[DataRequired()])
    status = SelectField(
                u'Status', choices=[('Init', 'Initiated'), ('Closed', 'Closed'), ('Assesment', 'Assesment'), ('Evaluation', 'Evaluation'), ('Cancelled', 'Cancelled'), ('Not Initiated', 'NotInit')])
    nextsteps = TextAreaField('Next Steps:')
    linkteams = StringField('Microsoft Teams Discussion link')
    car_options = SelectField(
                 u'Select Color', choices=[('Red', 'red'), ('Blue', 'blue'), ('Green', 'green')])
    name = StringField('Business Name')
    submit = SubmitField('Register')
    