# Import things from flask.
from flask import render_template, request

# Import func for case insensitive queries.
from sqlalchemy import func

# Import things from Flask that we need.
from mtg import app, db

# Import needed database model(s)
from models import Card


# Routing for the server.
@app.route("/", methods=['GET', 'POST'])
def index():
    card = None
    #Handle POST requests by getting appropriate date
    if request.method == 'POST':
        cardname = request.form['card']
        card = db.session.query(Card).filter(func.lower(Card.name) == func.lower(cardname)).first()
        #if card is Nonetype then we shouldn't call eval on its member field
        if card:
            abilities = eval(card.abilities)
        else:
            abilities = None
        return render_template('index.html',
                               title='Home',
                               card=card,
                               abilities=abilities)
    else:
        return render_template('index.html',
                               title='Home')
