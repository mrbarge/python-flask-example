from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ThingForm(FlaskForm):
    thing = StringField('Thing', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')
