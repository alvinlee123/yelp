__author__ = 'alee'
from flask_wtf import Form
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class Query(Form):
    search = StringField('Search', validators=[DataRequired()])
    star_rating = BooleanField('Four Stars Up', default=True)
    submit = SubmitField('Send')
