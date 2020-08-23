from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    input_text = StringField("Text to summarize", 
                             validators = [DataRequired()],
                             widget = TextArea())
    submit = SubmitField("Summarize!")
   
class ResponseForm(FlaskForm):
    satisfaction =  RadioField("Are you satisfied with this summary?", 
                               validators = [DataRequired()],
                               choices = [("1", "Yes"), 
                                          ("0", "No")])
    submit = SubmitField("Submit")
