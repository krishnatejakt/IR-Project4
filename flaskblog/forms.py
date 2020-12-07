from wtforms import Form, StringField, SelectField, SubmitField
from flask_wtf import FlaskForm

# class POISearchForm(Form):
#     choices = [('Modi', 'Modi'),
#                ('Trump', 'Trump'),
#                ('Amit', 'Amit')]
#     select = SelectField('Search for POI:', choices=choices)
#     search = StringField('')

class covid(FlaskForm):
    search = StringField('searchbar')
    button_submit = SubmitField('Search')

class poi_names(FlaskForm):
    choices = [('',''),('Narendra Modi','Modi'), ('Mike Pence','VP'),('Amit Shah','Amit'),('PMOIndia','PMO')]
    select = SelectField('Search for POI:', choices=choices)
    button_submit = SubmitField('Search')

class country(FlaskForm):
    choices = [('',''),('India','India'),('USA','USA'),('Italy','Italy')]
    select = SelectField('Search for POI:', choices=choices)
    button_submit = SubmitField('Search')

class topic(FlaskForm):
    topics = [('',''),('a','a'),('b','b')]
    select = SelectField('Search for POI:', choices=topics)
    button_submit = SubmitField('Search')
