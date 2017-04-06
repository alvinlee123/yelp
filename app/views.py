__author__ = 'alee'
from flask import render_template, session, request, jsonify, redirect, url_for, flash
from app import app
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from .forms import Query


auth = Oauth1Authenticator(
    consumer_key=app.config['CONSUMER_KEY'],
    consumer_secret=app.config['CONSUMER_SECRET'],
    token=app.config['TOKEN'],
    token_secret=app.config['TOKEN_SECRET']
)
client = Client(auth)

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/search', methods=['GET','POST'])
def search():
    form = Query()
    if request.method == 'POST':
        if form.validate_on_submit():
            result = client.search(form.data['search'])
            business_names = [ result.name for result in result.businesses]
            return render_template('results.html',
                                   businesses=business_names)
        else:
            flash("Invalid Search. Try again")
            return redirect( url_for('search'))
    elif request.method =='GET':
        return render_template('search.html',
                               form=form)
