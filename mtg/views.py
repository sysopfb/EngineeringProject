# Import things from flask.
from flask import render_template, request, jsonify

# Import func for case insensitive queries.
from sqlalchemy import func

# Import things from Flask that we need.
from mtg import app, db

# Import needed database model(s)
from models import Card

from flask.views import MethodView

# Routing for the server.
@app.route("/_get_card")
def get_card():
    cardname = request.args.get('cardname')
    card = db.session.query(Card).filter(func.lower(Card.name) == func.lower(cardname)).first()
    #If card isn't found then let jscript know
    if card is None:
        card = dict(found=False)
        return jsonify(card)
    else:
        return jsonify(card.to_json())


@app.route("/")
def index():
    return render_template('index.html',
                           title='Home')
