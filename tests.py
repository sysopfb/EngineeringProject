#!flask/bin/python
'''
Testing framework for EngineeringProject
13JUN2013 - basic framework layout
14JUN2013 - Added to_json testing
run with:
python tests.py
'''
import os
import unittest

from mtg import app, db
from mtg.models import Card

class TestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath('test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        card = Card(abilities = u'',
                    converted_cost = 2,
                    cost = u'1bb',
                    edition_id = u'',
                    flavor_text = u'',
                    illustrator = u'jason',
                    image_url = u'http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Jasonf.jpg/250px-Jasonf.jpg',
                    legalities = u'',
                    mci_id = u'',
                    name = u'Jason',
                    oracle_text = u'',
                    other_side = u'',
                    power = u'4',
                    rarity = u'5',
                    rulings = u'',
                    sub_types = u'ghoul',
                    toughness = u'1000',
                    type = u'monster',
                    url = u'')
        a = card.id
        assert a == None

    def test_to_json(self):
        c = Card(abilities = u'"Being awesome for a cost of {100}"',
                 converted_cost = 2,
                 cost = u'1bb',
                 edition_id = u'',
                 flavor_text = u'',
                 illustrator = u'jason',
                 image_url = u'http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Jasonf.jpg/250px-Jasonf.jpg',
                 legalities = u'',
                 mci_id = u'',
                 name = u'Jason',
                 oracle_text = u'',
                 other_side = u'',
                 power = u'4',
                 rarity = u'5',
                 rulings = u'',
                 sub_types = u'ghoul',
                 toughness = u'1000',
                 type = u'monster',
                 url = u'')
        b = c.to_json()
        assert b['name'] == 'Jason'

if __name__ == '__main__':
    unittest.main()
