from datetime import date

from app import app
from models import db, Plant

class TestPlant:
    '''Plant model in models.py'''

    def setup_method(self):
        with app.app_context():
            db.session.query(Plant).delete()
            db.session.commit()
            # Add a default plant for tests that need it
            plant = Plant(name="Test Plant", image="http://example.com/image.png", price=10.0)
            db.session.add(plant)
            db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with a name.'''
        p = Plant(name="Douglas Fir")
        assert(p)
    
    def test_can_be_created(self):
        '''can create records that can be committed to the database.'''
        with app.app_context():
            p = Plant(name="Douglas Fir")
            db.session.add(p)
            db.session.commit()
            assert(p.id)

            db.session.delete(p)
            db.session.commit()

    def test_can_be_retrieved(self):
        '''can be used to retrieve records from the database.'''
        with app.app_context():
            p = Plant.query.all()
            assert(p)

    def test_can_be_serialized(self):
        '''can create records with a to_dict() method for serialization.'''
        with app.app_context():
            p = Plant(name="Douglas Fir")
            db.session.add(p)
            db.session.commit()
            p_dict = Plant.query.filter_by(name="Douglas Fir").first().to_dict()
            assert((type(p_dict) == dict) and (p_dict["name"] == "Douglas Fir"))
        
            db.session.delete(p)
            db.session.commit()
