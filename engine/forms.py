from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Length
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    input_text = StringField("Text to summarize", 
                             validators = [InputRequired(), Length(min = 5, max = 10)],
                             widget = TextArea())
    submit = SubmitField("Summarize!")

#    input_text = TextAreaField("Text to summarize", [validators.length(min = 10, max=200)])
#    submit = SubmitField("Summarize!")

#class ResponseForm(FlaskForm):
#    satisfaction =  RadioField("Are you satisfied with this summary?", 
#                               validators = [DataRequired()],
#                               choices = [("1", "Yes"), 
#                                          ("0", "No")])
#    submit = SubmitField("Submit")
    
class ResponseForm(FlaskForm):
    satisfaction =  RadioField("Are you satisfied with this summary?", 
                               validators = [InputRequired()],
                               choices = [("1", "Yes"), 
                                          ("0", "No")])
    submit = SubmitField("Submit")
